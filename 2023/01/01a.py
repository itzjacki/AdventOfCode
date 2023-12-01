import re

with open("01/input.txt", "r") as f:
  splitfile = f.read().split("\n")

sum = 0

def find_number_as_string(text, reversed):
  matches = re.findall("\d", text)
  if reversed:
    result = matches[-1]
  else:
    result = matches[0]
  return str(result)

for line in splitfile:
  if line != "":
    first = find_number_as_string(str(line), False)
    last = find_number_as_string(str(line), True)
    sum += int(first + last)

print(sum)
