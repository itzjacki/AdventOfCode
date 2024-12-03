import re

with open("03/input.txt", "r") as f:
  file = f.read().replace("\n", "")

processed_text = file.replace(
    "don't()", "\nNOGO").replace("do()", "\n").split("\n")

sum = 0

for line in processed_text:
  if line[0:4] != "NOGO":
    matches = re.findall("mul\(\d{1,3},\d{1,3}\)", line)
    for match in matches:
      muls = re.findall("\d+", match)
      sum += int(muls[0]) * int(muls[1])

print(sum)
