#!/usr/bin/python3
import pulp as p

# Definer problemet
model = p.LpProblem('HammersAndNails', p.LpMaximize)

# Her skal du definere beslutningsvariablene

# Eksempel:
x = p.LpVariable("x", lowBound = 0)
y = p.LpVariable("y", upBound = 10)

# Her skal du legge til den linÃ¦re funksjonen som skal optimeres

# Eksempel:
model += 3000 * x + 1000 * y

# Her skal du legge til de lineÃ¦re ulikhetene som pÃ¥ oppfylles

# Eksempel:

model += x >= 0 and y >= 0 
model += 3000 * x + 1000 * y <= 180

# Print modellen
# print(model)

# LÃ¸s det lineÃ¦re programmet
status = model.solve()

# Print lÃ¸sningen

# Print verdien til en beslutningsvariabel:
print(p.value(x))

# Print optimal verdi:
print(p.value(model.objective))
