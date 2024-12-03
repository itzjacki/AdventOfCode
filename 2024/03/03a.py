import re

with open("03/input.txt", "r") as f:
  splitfile = f.read().split("\n")

sum = 0

for line in splitfile:
  matches = re.findall("mul\(\d{1,3},\d{1,3}\)", line)

  for match in matches:
    muls = re.findall("\d+", match)
    sum += int(muls[0]) * int(muls[1])

print(sum)
