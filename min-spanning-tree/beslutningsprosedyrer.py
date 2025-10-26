#!/usr/bin/python3
# coding=utf-8

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et lite sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å teste på
# et større sett med 1000 genererte instanser. For å teste på det
# større settet med genererte instanser, må du (1) laste ned filen med
# testene fra øvingssystemet, (2) legge den samme plass som denne
# python-filen og (3) sette variabelen under til True.
use_extra_tests = True

class DisjointStructure:
    def __init__(self):
        self.map = {}

    def make_set(self, str1):
        self.map[str1] = str1
    
    def find_set(self, str1):
        parent = self.map[str1]
        if str1 == parent:
            return parent
        new_parent = self.find_set(parent)
        self.map[str1] = new_parent
        return new_parent
    
    def union(self, str1, str2):
        parent_str1 = self.find_set(str1)
        parent_str2 = self.find_set(str2)
        self.map[parent_str1] = parent_str2

def remove_dup(arr):
    myset = set()
    arr2 = []
    for el in arr:
        element = tuple(el)
        if element in myset:
            continue
        arr2.append(list(el))
        myset.add(element)
    return arr2

class Graph:

    def __init__(self, vert, edges):
        self.vert = {}
        for i, current_vert in enumerate(vert):
            self.vert[current_vert] = i 

        self.adj = [[] for _ in self.vert]

        for edge in edges:
            self.adj[self.vert[edge[0]]].append(self.vert[edge[1]])
        self.color = [False for _ in self.vert]

    def isCyclic(self):
        in_degree = [0] * len(self.vert)
        queue = [-1 for _ in self.vert]
        head = 0
        tail = 0
        visited = 0                       # Count of visited nodes

        #  Calculate in-degree of each node
        for u in range(len(self.vert)):
            for v in self.adj[u]:
                if u == v:
                    return True
                in_degree[v] += 1

        #  Enqueue nodes with in-degree 0
        for u in range(len(self.vert)):
            if in_degree[u] == 0:
                queue[head] = u
                head += 1

        #  Perform BFS (Topological Sort)
        while head != tail:
            u = queue[tail]
            tail += 1
            visited += 1

            # Decrease in-degree of adjacent nodes
            for v in self.adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue[head] = v
                    head += 1

        #  If visited != V, graph has a cycle
        return visited != len(self.vert)

def check(variables, constraints):
    new_constraints = []
    for el in constraints:
        if el[1] == "<":
            new_constraints.append([el[2], ">", el[0]])
        else:
            new_constraints.append(el)
    constraints = new_constraints 

    disjoint_set = DisjointStructure()
    for var in variables:
        disjoint_set.make_set(var)
    for constrain in constraints:
        if constrain[1] == "=":
            disjoint_set.union(constrain[0], constrain[2])

    constraints = remove_dup(list(filter(lambda constraint: constraint[1] != "=", constraints)))
    variables = list(set(map(lambda var: disjoint_set.find_set(var), variables)))

    constraints = list(map(lambda constrain: [disjoint_set.find_set(constrain[0]), disjoint_set.find_set(constrain[2])], constraints))

    graph = Graph(variables, constraints)

    return not graph.isCyclic()


# Hardkodete tester på format: (variables, constraints), riktig svar
tests = [
    (
        (
            ["x1", "x2", "x3"],
            [("x1", "<", "x2"), ("x2", "<", "x3"), ("x1", ">", "x3")],
        ),
        False,
    ),
    ((["x1", "x2"], [("x2", "<", "x1"), ("x1", "=", "x2")]), False),
    ((["x1"], []), True),
    ((["x1", "x2"], [("x1", "=", "x2")]), True),
    ((["x1"], [("x1", ">", "x1")]), False),
    ((["x1"], [("x1", "=", "x1")]), True),
    ((["x1", "x2"], [("x1", "<", "x2")]), True),
    ((["x1", "x2"], [("x2", "<", "x1"), ("x1", "=", "x2")]), False),
    ((["x1", "x2"], [("x2", ">", "x1"), ("x1", "<", "x2")]), True),
    ((["x1", "x2"], [("x1", ">", "x2"), ("x2", ">", "x1")]), False),
    (
        (
            ["x1", "x2", "x3"],
            [("x1", "<", "x2"), ("x2", "<", "x3"), ("x1", ">", "x3")],
        ),
        False,
    ),
    (
        (
            ["x1", "x2", "x3"],
            [("x1", "<", "x2"), ("x3", "=", "x1"), ("x2", "<", "x3")],
        ),
        False,
    ),
    ((["x4", "x0", "x1"], [("x1", "<", "x0")]), True),
    ((["x5", "x8"], [("x8", "<", "x5"), ("x8", "<", "x5")]), True),
    ((["x1", "x0", "x2"], []), True),
    (
        (
            ["x4", "x8", "x5"],
            [("x4", "<", "x5"), ("x8", ">", "x5"), ("x5", "<", "x8")],
        ),
        True,
    ),
    (
        (
            ["x5", "x9", "x0"],
            [
                ("x9", ">", "x5"),
                ("x9", "=", "x0"),
                ("x0", "=", "x9"),
                ("x0", "=", "x9"),
            ],
        ),
        True,
    ),
    (
        (
            ["x0", "x6", "x7"],
            [("x7", "=", "x0"), ("x7", ">", "x0"), ("x6", ">", "x0")],
        ),
        False,
    ),
    ((["x8", "x6", "x0"], []), True),
    (
        (
            ["x8", "x7", "x0"],
            [("x8", "=", "x0"), ("x0", "=", "x8"), ("x0", "=", "x8")],
        ),
        True,
    ),
    (
        (
            ["x8", "x4"],
            [
                ("x4", ">", "x8"),
                ("x4", ">", "x8"),
                ("x8", "<", "x4"),
                ("x4", ">", "x8"),
                ("x8", "=", "x4"),
            ],
        ),
        False,
    ),
    ((["x3", "x8", "x5"], [("x3", ">", "x8")]), True),
]


failed = False
for test_case, answer in tests:
    variables, constraints = test_case
    student = check(variables, constraints)
    if student != answer:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans:
variables: {', '.join(variables)}
constraints:
    {(chr(10) + '    ').join(' '.join(x) for x in constraints)}

Ditt svar: {student}
Riktig svar: {answer}
""")

if use_extra_tests:
    with open("tests_theory_solver.txt") as extra_tests_data:
        extra_tests = []
        for line in extra_tests_data:
            variables, constraints, answer = line.strip().split(" | ")
            variables = variables.split(",")
            constraints = [x.split(" ") for x in constraints.split(",")]
            extra_tests.append(((variables, constraints), bool(int(answer))))

    n_failed = 0
    for test_case, answer in extra_tests:
        variables, constraints = test_case
        student = check(variables, constraints)
        if student != answer:
            n_failed += 1
            if failed and n_failed <= 5:
                print("-"*50)

            failed = True
            if n_failed <= 5:
                print(f"""
Koden feilet for følgende instans:
variables: {', '.join(variables)}
constraints:
    {(chr(10) + '    ').join(' '.join(x) for x in constraints)}

Ditt svar: {student}
Riktig svar: {answer}
""")
                break
            elif n_failed == 6:
                print("Koden har feilet for mer enn 5 av de ekstra testene.")
                print("De resterende feilene vil ikke skrives ut.")

    if n_failed > 0:
        print(f"Koden feilet for {n_failed} av de ekstra testene.")
        

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")
