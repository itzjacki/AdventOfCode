with open("10/input.txt", "r") as file:
  f = file.read().splitlines()

register_values = []

for l in f:
  if not bool(register_values):
    register_values.append(1)
  else:
    register_values.append(register_values[-1])
  if l[0] == "a":
    register_values.append(register_values[-1] + int(l[5:]))
    
print(sum(n * register_values[n-2] for n in [20, 60, 100, 140, 180, 220]))