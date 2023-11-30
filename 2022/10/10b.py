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

def isLitPixel(pos):
  registry_pos = 1
  if pos > 0:
    registry_pos = register_values[pos - 1]
  return abs(pos % 40 - registry_pos) <= 1

screen_output = []
# render row
for i in range(6):
  screen_output.append("")
  #render pixel
  for j in range(40):
    if isLitPixel(i * 40 + j):
      screen_output[i] += "#"
    else:
      screen_output[i] += "."

for line in screen_output:
  print(line)