import re

with open("08/input.txt", "r") as f:
  splitfile = f.read().split("\n")

instructions = splitfile[0]

parsed_lines = [re.findall("[A-Z]{3}", l) for l in splitfile[2:]]

network_map = {node[0]: (node[1], node[2]) for node in parsed_lines}

step = 0
current = "AAA"

while current != "ZZZ":
  next_step = instructions[step % len(instructions)]

  if next_step == "L":
    current = network_map[current][0]
  elif next_step == "R":
    current = network_map[current][1]
  else: raise ValueError

  step += 1

print(step)
