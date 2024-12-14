import re

with open("13/input.txt", "r") as f:
  splitfile = f.read().split("\n\n")

sum = 0

for machine in splitfile:
  [ax, ay, bx, by, x, y] = [int(n) for n in re.findall("\d+", machine)]

  a = (x * by - y * bx) / (ax * by - ay * bx)
  b = (x * ay - y * ax) / (bx * ay - by * ax)

  if a == int(a) and b == int(b):
    sum += int(a * 3 + b)

print(sum)
