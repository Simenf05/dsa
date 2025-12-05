#!/usr/bin/python3
# coding=utf-8
import random
import math

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nedre, og muligheten for å generere
# tilfeldige instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å justere på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = True
# Antall tilfeldige tester som genereres.
random_tests = 100
# Lavest mulig antall oppgaver i generert instans.
tasks_lower = 5
# Høyest mulig antall oppgaver i generert instans.
tasks_upper = 20
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0

time = 0

def dfs_visit(vert, visited, discover, finish, finish_list, edge_adj):
    global time
    time += 1
    discover[vert.i] = time
    visited[vert.i] = True

    for v in edge_adj[vert.i]:
        if not visited[v.i]:
            dfs_visit(v, visited, discover, finish, finish_list, edge_adj)
    time += 1
    finish[vert.i] = time
    finish_list.insert(0, vert)

def dfs(tasks, finish_list, edge_adj):
    global time

    visited = [False for _ in tasks]
    discover = [0 for _ in tasks]
    finish = [0 for _ in tasks]

    time = 0

    for vert in tasks:
        if not visited[vert.i]:
            dfs_visit(vert, visited, discover, finish, finish_list, edge_adj)

def topo_sort(tasks, edge_adj):
    finish_list = []
    dfs(tasks, finish_list, edge_adj)
    return finish_list

def building_time(tasks):

    edge_adj = [[] for _ in tasks]
    for task in tasks:
        for dep in task.depends_on:
            edge_adj[dep.i].append(task)

    topo_sorted_tasks = topo_sort(tasks, edge_adj)
    dist_vec = [float("inf") for _ in range(len(tasks))]
    dist_vec[topo_sorted_tasks[0].i] = 0

    print(list(map(lambda task: task.i, topo_sorted_tasks)))

    task_time = [-1 for _ in topo_sorted_tasks]

    for task in topo_sorted_tasks:
        dep_time = list(map(lambda task2: task_time[task2.i], task.depends_on))
        dep_time.append(0)
        task_time[task.i] = task.time + max(dep_time)

    return max(task_time)


class Task:
    def __init__(self, time, depends_on, i):
        self.time = time
        self.depends_on = depends_on
        self.i = i

    def __str__(self):
        depends_on_str = ", ".join(
            "Task " + str(task.i) for task in self.depends_on
        )
        return "Task {:}: {{time: {:}, depends_on: ".format(
            self.i, self.time
        ) + "[{:}]}}".format(depends_on_str)

    def __repr__(self):
        return str(self)

# Hardkodete tester på format: tasks, svar
tests = [
    ([(2, [2, 3]), (3, [3]), (3, [3]), (5, [])], 10),
    ([(4, [])], 4),
    ([(1, []), (4, [2]), (5, [])], 9),
    ([(3, [])], 3),
    ([(2, [1, 2]), (1, [2]), (4, [])], 7),
    ([(4, [])], 4),
    ([(4, [])], 4),
    ([(1, [])], 1),
    ([(1, [1]), (3, [])], 4),
    ([(1, [1]), (3, [2]), (3, [])], 7),
]


def test_case_from_list(tasks_arr):
    tasks = [Task(task[0], [], i) for i, task in enumerate(tasks_arr)]
    for i in range(len(tasks_arr)):
        for j in tasks_arr[i][1]:
            tasks[i].depends_on.append(tasks[j])
    return tasks


def gen_examples(k, nl, nu):
    for _ in range(k):
        n = random.randint(nl, nu)
        tasks = []
        D = [-1]*n
        for i in range(n):
            nd = random.randint(0, math.ceil(math.log(i + 1, 2)))
            dep = list(random.sample(range(i), k=nd))
            t = random.randint(1, max(1, n))
            tasks.append((t, dep))
            D[i] = max([0] + [D[d] for d in dep]) + t

        u = list(range(n))
        random.shuffle(u)
        M = {i: j for i, j in enumerate(u)}
        MD = {j: i for i, j in enumerate(u)}
        shuffled_tasks = [
            (tasks[M[i]][0], [MD[j] for j in tasks[M[i]][1]])
            for i in range(n)
        ]
        tasks = test_case_from_list(shuffled_tasks)
        yield tasks, max(D)


tests = [
    (test_case_from_list(test_case), answer)
    for test_case, answer in tests
]

if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        tasks_lower,
        tasks_upper,
    ))


failed = False
for tasks, answer in tests:
    student = building_time(tasks)
    if student != answer:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans.
tasks:
    {(chr(10) + '    ').join(map(str, tasks))}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden fungerte for alle eksempeltestene.")
