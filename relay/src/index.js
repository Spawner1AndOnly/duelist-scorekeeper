// Duelist Scorekeeper – online relay (Cloudflare Workers + Durable Objects, WebSocket Hibernation API)
// One Durable Object per room code. Two seats: 0 = the player who created the room, 1 = the player who joined.
// The relay only passes messages from one phone to the other; it stores no game state, only who sits where.
import { DurableObject } from "cloudflare:workers";

const CODE_RX = /^[A-Z2-9]{5}$/;     // room codes: 5 letters/digits without look-alikes
const MAX_MSG = 64 * 1024;           // a full game state is ±4-15 KB
const ROOM_TTL = 24 * 60 * 60 * 1000; // rooms are wiped 24 h after they were created

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    const m = url.pathname.match(/^\/room\/([A-Za-z0-9]+)$/);
    if (!m) return new Response("Duelist Scorekeeper relay", { status: 200 });
    if (req.headers.get("Upgrade") !== "websocket") return new Response("Expected a WebSocket", { status: 426 });
    const code = m[1].toUpperCase();
    if (!CODE_RX.test(code)) return new Response("Bad room code", { status: 400 });
    return env.ROOMS.get(env.ROOMS.idFromName(code)).fetch(req);
  },
};

export class Room extends DurableObject {
  constructor(ctx, env) {
    super(ctx, env);
    // keep-alive pings are answered without waking the room up (costs nothing)
    this.ctx.setWebSocketAutoResponse(new WebSocketRequestResponsePair("ping", "pong"));
  }

  async fetch(req) {
    const url = new URL(req.url);
    const seat = url.searchParams.get("seat") === "1" ? 1 : 0;
    const cid = (url.searchParams.get("cid") || "").slice(0, 40);
    const create = url.searchParams.get("create") === "1";
    if (!cid) return new Response("Missing cid", { status: 400 });

    const seats = (await this.ctx.storage.get("seats")) || [null, null];
    let err = "";
    if (create) {
      if (seats[0] && seats[0] !== cid) err = "taken"; // that code is in use, the app picks another one
    } else if (!seats[0]) err = "notfound";
    else if (seats[seat] && seats[seat] !== cid) err = "full";

    const pair = new WebSocketPair();
    const [client, server] = Object.values(pair);
    this.ctx.acceptWebSocket(server, [String(seat)]);
    if (err) {
      server.send(JSON.stringify({ t: "err", err }));
      server.close(4000, err);
      return new Response(null, { status: 101, webSocket: client });
    }
    if (!seats[seat]) {
      seats[seat] = cid;
      await this.ctx.storage.put("seats", seats);
      if (seat === 0) await this.ctx.storage.setAlarm(Date.now() + ROOM_TTL);
    }
    server.serializeAttachment({ seat, cid });
    // the same phone reconnecting: close its old connection
    for (const ws of this.ctx.getWebSockets(String(seat))) if (ws !== server) try { ws.close(4001, "replaced"); } catch (e) {}
    const other = this.ctx.getWebSockets(String(1 - seat));
    server.send(JSON.stringify({ t: "hello", seat, peer: other.length > 0 }));
    for (const ws of other) try { ws.send(JSON.stringify({ t: "peer", on: true })); } catch (e) {}
    return new Response(null, { status: 101, webSocket: client });
  }

  async webSocketMessage(ws, msg) {
    const a = ws.deserializeAttachment();
    if (!a) return;
    if (typeof msg !== "string" || msg.length > MAX_MSG) return;
    if (msg === '{"t":"leave"}') { // a player leaves the room for good: free the seat
      const seats = (await this.ctx.storage.get("seats")) || [null, null];
      seats[a.seat] = null;
      await this.ctx.storage.put("seats", seats);
    }
    for (const o of this.ctx.getWebSockets(String(1 - a.seat))) try { o.send(msg); } catch (e) {}
  }

  async webSocketClose(ws, code) {
    const a = ws.deserializeAttachment();
    if (!a) return;
    try { ws.close(code === 1005 ? 1000 : code, "bye"); } catch (e) {}
    const still = this.ctx.getWebSockets(String(a.seat)).some(o => o !== ws);
    if (!still) for (const o of this.ctx.getWebSockets(String(1 - a.seat))) try { o.send(JSON.stringify({ t: "peer", on: false })); } catch (e) {}
  }

  async webSocketError(ws) { await this.webSocketClose(ws, 1011); }

  async alarm() { // 24 h after the room was made: forget it
    for (const ws of this.ctx.getWebSockets()) try { ws.close(4002, "expired"); } catch (e) {}
    await this.ctx.storage.deleteAll();
  }
}
