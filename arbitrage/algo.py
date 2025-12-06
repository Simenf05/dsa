#!/bin/env python

import numpy as np
import json

"""
conv(ETH, USDT) -> bid(ETHUSDT)
conv(USDT, ETH) -> ask(ETHUSDT)
"""


class Graph:
    def __init__(self, map):
        self.size = len(map)
        self.map = map
        self.pairs = {}
        self.adj = [[float() for _ in range(self.size)] for _ in range(self.size)]

    def add_pair(self, currencies: str, ask: float, bid: float):
        base, quote = currencies.split("/")

        def add_edge(i, j, rate):
            self.adj[i][j] = rate

        base_index = self.map.index(base)
        quote_index = self.map.index(quote)

        pair = self.pairs.get(base, list())
        pair.append(quote)
        self.pairs[base] = pair

        add_edge(base_index, quote_index, ask)
        add_edge(quote_index, base_index, bid)

    def ask(self, base_asset, quote_asset):
        quote_index = self.map.index(quote_asset)
        base_index = self.map.index(base_asset)
        return self.adj[base_index][quote_index]

    def bid(self, base_asset, quote_asset):
        quote_index = self.map.index(quote_asset)
        base_index = self.map.index(base_asset)
        return self.adj[quote_index][base_index]

    def convert(self, amount, from_asset, to_asset):

        from_is_base = to_asset in self.pairs.get(from_asset, [])
        if from_is_base:
            base = from_asset
            quote = to_asset
            return amount * self.bid(base, quote)
        else:
            base = to_asset
            quote = from_asset
            return amount / self.ask(base, quote)

    def check_triage(self, currency_A, currency_B, currency_C):
        start_amount_A = float(100000.0)
        amount_B = self.convert(start_amount_A, currency_A, currency_B)
        amount_C = self.convert(amount_B, currency_B, currency_C)
        final_A = self.convert(amount_C, currency_C, currency_A)
        profit = final_A - start_amount_A
        return profit 


with open("data2.json", "r") as f:
    data = json.load(f)

map = []

for key, exchange in data.items():
    currency_A, currency_B = key.split("/")
    if currency_A not in map: 
        map.append(currency_A)
    if currency_B not in map: 
        map.append(currency_B)

graph = Graph(map)

for name, exchange in data.items():
    graph.add_pair(name, exchange["ask"], exchange["bid"])
np.set_printoptions(precision=4)
np.set_printoptions(suppress=True)
# print(graph.map)
# print(np.array(graph.adj))

# print(graph.pairs)

# print(f"ETH BTC SOL: {graph.check_triage('ETH', 'BTC', 'SOL')}")
print()
print(f"USDT BTC ETH: {graph.check_triage('USDT', 'ETH', 'BTC')}")

# def conv(amount, curr1, curr2):
    # return graph.convert(amount, curr1, curr2)

# print(conv(conv(1, 'USDT', 'BTC'), 'BTC', 'USDT'))
# print(conv(conv(conv(1, 'USDT', 'BTC'), 'BTC', 'ETH'), 'ETH', 'USDT'))

# final = conv(conv(conv(1, 'USDT', 'BTC'), 'BTC', 'ETH'), 'ETH', 'USDT')
# print(f"final: {final}")

# print(graph.convert(1, 'BTC', 'USDT'))
# print(graph.convert(98250, 'USDT', 'BTC'))



