import re
f = open("04/input.txt", "r").read().splitlines()

number_overlapped = 0

for line in f:
  result = re.search(r"(\d+)-(\d+),(\d+)-(\d+)", line)
  [a, b, c, d] = [int(n) for n in result.groups()]
  if c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b:
    number_overlapped += 1

print(number_overlapped)