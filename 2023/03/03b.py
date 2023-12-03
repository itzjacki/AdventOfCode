# Disclaimer: This is not a general soltuion, I did a quick regex scan
# of the input and checked that there were no numbers with more than 3
# digits. This solution only works for 1-3 digit numbers.

import re

with open("03/input.txt", "r") as f:
  splitfile = f.read().split("\n")

gear_ratio_sum = 0

def numbers_around_position(line, position):
  adjacent = []

  is_digit = [False, line[position].isnumeric(), False]
  if position > 0:
    is_digit[0] = line[position - 1].isnumeric()
  if position + 1 < len(line):
    is_digit[2] = line[position + 1].isnumeric()

  if is_digit == [True, False, False]:
    adjacent.append(int(re.search("\d+$", line[:position]).group()))

  if is_digit == [False, False, True]:
    adjacent.append(int(re.search("^\d+", line[position + 1:]).group()))

  if is_digit == [True, True, False]:
    adjacent.append(int(re.search("\d+$", line[:position + 1]).group()))
  
  if is_digit == [False, True, True]:
    adjacent.append(int(re.search("^\d+", line[position:]).group()))

  if is_digit == [True, False, True]:
    adjacent.append(int(re.search("\d+$", line[:position]).group()))
    adjacent.append(int(re.search("^\d+", line[position + 1:]).group()))

  if is_digit == [False, True, False]:
    adjacent.append(int(line[position]))

  if is_digit == [True, True, True]:
    adjacent.append(int(line[position - 1 : position + 2]))
  
  return adjacent

for i in range(len(splitfile)):
  line = splitfile[i]
  gears = re.findall("\*", line)
  
  for gear_pos in [match.start() for match in re.finditer("\*", line)]:

    numbers = []
    if i > 0:
      numbers += numbers_around_position(splitfile[i - 1], gear_pos)
    numbers += numbers_around_position(line, gear_pos)
    if i + 1 < len(splitfile):
      numbers += numbers_around_position(splitfile[i + 1], gear_pos)

    print(numbers)
    if len(numbers) == 2:
      gear_ratio_sum += numbers[0] * numbers[1]

print(gear_ratio_sum)
