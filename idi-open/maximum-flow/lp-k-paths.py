#!/usr/bin/python3
# coding=utf-8

import pulp

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

def find_k_paths(nodes, edges, k, s, t):
    # Definer problemet
    model = pulp.LpProblem("KPaths", pulp.LpMinimize)

    print(nodes)
    print(edges)
    print(k)
    print(s)
    print(t)

    vars = {}


    # Skriv din kode her

    # Løs lineærprogrammet
    model.solve()

    # Sjekk om vi har funnet en løsning
    # Status er enten 'Optimal', 'Infeasible', 'Unbounded' eller 'Undefined'
    status = pulp.LpStatus[model.status]
    if status != 'Optimal':
        return None
    else:
        # Hent ut målverdien
        objective_value = pulp.value(model.objective)
        return objective_value


tests = [
     (
         ['a', 'b', 'c', 'd', 'e'],
         [
             ('a', 'b', 1),
             ('a', 'd', 1),
             ('a', 'e', 5),
             ('b', 'c', 1),
             ('b', 'e', 1),
             ('c', 'e', 1),
             ('d', 'e', 1)
         ],
         2,
         'a',
         'e',
         4
     ),
     (
         ['a', 'b', 'c', 'd'],
         [
             ('a', 'b', 2),
             ('b', 'c', 2),
             ('c', 'd', 2)
         ],
         2,
         'a',
         'd',
         None
     ),
     (
         ['a', 'b', 'c', 'd', 'e'],
         [
             ('a', 'b', 1),
             ('b', 'e', 1),
             ('a', 'c', 2),
             ('c', 'e', 2),
             ('a', 'd', 3),
             ('d', 'e', 3)
         ],
         3,
         'a',
         'e',
         12
     ),
     (
         ['a', 'b', 'c', 'd'],
         [
             ('a', 'b', 1),
             ('a', 'c', 1),
             ('b', 'd', 1),
             ('c', 'd', 1),
             ('b', 'c', 5)
         ],
         2,
         'a',
         'd',
         4
     ),
     (
         ['a', 'b', 'c', 'd', 'e'],
         [
             ('a', 'b', 1),
             ('a', 'c', 1),
             ('b', 'd', 1),
             ('c', 'd', 1),
             ('d', 'e', 1)
         ],
         2,
         'a',
         'e',
         None
     )
]

message = "Koden fungerte for alle eksempeltestene."

for nodes, edges, k, s, t, objective_value in tests:
    answer = find_k_paths(nodes, edges, k, s, t)
    if not objective_value:
        if answer is not None:
            message = "Du returnert ikke None selv om det ikke finnes k stier som ikke deler kanter."

    if answer != objective_value:
        message = f"Den totale vekten til de k stiene er ikke riktig.\n" + \
                        f"Koden feilet for testen med noder={nodes},\n" + \
                        f"kanter={edges},\nk={k}, s={s}, t={t}.\n" + \
                        f"Ditt svar: {answer}. Riktig svar: " +\
                        f"{objective_value}."
print("=============================================================================")
print(message)
print("=============================================================================")


