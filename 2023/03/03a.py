import re

with open("03/input.txt", "r") as f:
  splitfile = f.read().split("\n")

part_sum = 0

def symbol_around(line_number, start, length):
  symbol_found = False
  if start > 0:
    if splitfile[line_number][start - 1] != ".":
      symbol_found = True
  if start + length < len(line):
    if splitfile[line_number][start + length] != ".":
      symbol_found = True
  return symbol_found

def symbol_above_below(line_number, start, length):
  if line_number > 0:
    match = re.search("[^\d\.]", splitfile[line_number - 1][max(start-1, 0):min(start + length + 1, len(splitfile[line_number]))])
    if match is not None:
      return True
  if line_number < len(splitfile) - 1:
    match = re.search("[^\d\.]", splitfile[line_number + 1][max(start-1, 0):min(start + length + 1, len(splitfile[line_number]))])
    if match is not None:
      return True
  return False
  

for i in range(len(splitfile)):
  line = splitfile[i]
  numbers = re.findall("\d+", line)
  
  for number in numbers:
    position = line.find(number)
    number_counts = symbol_around(i, int(position), len(number)) or symbol_above_below(i, int(position), len(number))
    # print(number, number_counts)
    if number_counts:
      part_sum += int(number)

print(part_sum)