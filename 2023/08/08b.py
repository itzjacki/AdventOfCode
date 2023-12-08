import re

with open("08/input.txt", "r") as f:
  splitfile = f.read().split("\n")

# I originally wrote this code to be quite a bit more complex, but found the
# following assumptions that let me simplify as I was writing:
# - All the patterns repeat in the same way in the same number of steps
# - The number of steps never factorizes into more than one of the same factor

instructions = splitfile[0]

parsed_lines = [re.findall("[0-9A-Z]{3}", l) for l in splitfile[2:]]
network_map = {node[0]: (node[1], node[2]) for node in parsed_lines}

current = [{"current": node, "steps": None} for node in list(network_map.keys()) if node[-1] == "A"]
step = 0

while not all(node["steps"] != None for node in current):
  next_step = instructions[step % len(instructions)]
  step += 1
  for node in current:
    if node["steps"] == None:
      if next_step == "L":
        node["current"] = network_map[node["current"]][0]
      elif next_step == "R":
        node["current"] = network_map[node["current"]][1]
      else: raise ValueError
      if node["current"][2] == "Z":
        node["steps"] = step

def factorize(num_to_factorize):
  n = num_to_factorize
  factors = []
  while n > 1:
    for i in range(2, n + 1):
      if n % i == 0:
        n //= i
        factors.append(i)
  return factors

all_factors = []

for node in current:
  for factor in factorize(node["steps"]):
    if factor not in all_factors: all_factors.append(factor)

product = 1
for factor in all_factors:
  product *= factor
print(product)