#!/bin/env python
import asyncio
import websockets
import json
import time

"""
possible exchange markets:
- bitstamp
- bybit
- kraken
- okx
- Deribit

"wss://ws.kraken.com/"
"wss://ws.bitstamp.net/"
"wss://ws-auth.kraken.com/v2"
"""

def clear():
    print('\033c')

async def connect(uri, dump, average_list):
    async with websockets.connect(uri) as ws:
        start_time = time.perf_counter()
        await ws.send(dump)

        response = await ws.recv()
        
        end_time = time.perf_counter()
        
        rtt_ms = (end_time - start_time) * 1000
        average_list.append(rtt_ms)
        return response

async def ping_all():
    uri1 = "wss://kapi1.btloginc.com:9082"
    uri2 = "wss://ws.bitstamp.net/"
    uri3 = "wss://stream.bybit.eu/v5/public/misc/status"

    dump_kraken = json.dumps(
{
"action": "KeepLive"
}
    )
    dump_bybit = json.dumps({"op": "ping"})
    dump_bitstamp = json.dumps({"event": "bts:heartbeat"})


    map = {
        "kraken": [],
        "bitstamp": [],
        "bybit": []
    }

    resp1 = ""
    resp2 = ""
    resp3 = ""

    while True:
        clear()
        try:
            print(f"RTT: {sum(map['kraken'])/len(map['kraken']):.2f} ms")
            # print(f"RTT: {sum(map['bitstamp'])/len(map['bitstamp']):.2f} ms")
            # print(f"RTT: {sum(map['bybit'])/len(map['bybit']):.2f} ms")
            print(resp1)
            # print(resp2)
            # print(resp3)
        except:
            print("waiting...")

        resp1 = await connect(uri1, dump_kraken, map["kraken"])
        # resp2 = await connect(uri2, dump_bitstamp, map["bitstamp"])
        # resp3 = await connect(uri3, dump_bybit, map["bybit"])



asyncio.run(ping_all())
