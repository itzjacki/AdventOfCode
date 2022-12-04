import re
f = open("04/input.txt", "r").read().splitlines()

numberContained = 0

for line in f:
  result = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", line)
  [a, b, c, d] = [int(n) for n in result.groups()]
  if (a <= c and d <= b) or (c <= a and b <= d):
    numberContained += 1

print(numberContained)