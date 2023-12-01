import re

with open("01/input.txt", "r") as f:
  splitfile = f.read().split("\n")

sum = 0

def convert_to_number(text):
  if text.isnumeric():
    return text
  match text:
    case "one":
      return 1
    case "two":
      return 2
    case "three":
      return 3
    case "four":
      return 4
    case "five":
      return 5
    case "six":
      return 6
    case "seven":
      return 7
    case "eight":
      return 8
    case "nine":
      return 9

def find_number_as_string(text, reversed):
  raw_matches = re.finditer(r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))', text)
  matches = [match.group(1) for match in raw_matches]
  if reversed:
    result = matches[-1]
  else:
    result = matches[0]
  result = convert_to_number(result)
  return str(result)

for line in splitfile:
  if line != "":
    first = find_number_as_string(str(line), False)
    last = find_number_as_string(str(line), True)
    sum += int(first + last)

print(sum)