#!/bin/env python
import itertools

data = {
  "BTCUSDT": { "bid": 10000.0, "ask": 10010.0 },
  "ETHUSDT": { "bid": 500.0, "ask": 501.0 },
  "SOLUSDT": { "bid": 20.0, "ask": 20.1 },
  "ETHBTC": { "bid": 0.0505, "ask": 0.0506 },
  "SOLBTC": { "bid": 0.002, "ask": 0.00201 },
  "SOLETH": { "bid": 0.0397, "ask": 0.0398 }
}

# Build graph
currencies = set()
for pair in data.keys():
    base, quote = pair[:3], pair[3:]
    currencies.add(base)
    currencies.add(quote)
currencies = list(currencies)

# Adjacency matrix storing both bid/ask
adj = {}
for c in currencies:
    adj[c] = {}
    for d in currencies:
        adj[c][d] = None

for pair, prices in data.items():
    base, quote = pair[:3], pair[3:]
    adj[base][quote] = {"bid": prices["bid"], "ask": prices["ask"]}
    adj[quote][base] = {"bid": 1/prices["ask"], "ask": 1/prices["bid"]}

import json
print(json.dumps(adj, indent=4))
