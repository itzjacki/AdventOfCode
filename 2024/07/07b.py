with open("07/input.txt", "r") as f:
  splitfile = f.read().split("\n")


def parse(line):
  result, numbers = line.split(": ")
  return int(result), [int(n) for n in numbers.split(" ")]


def calc(numbers):
  if len(numbers) > 1:
    return [*calc([numbers[0] + numbers[1], *numbers[2:]]), *calc([int(str(numbers[0]) + str(numbers[1])), *numbers[2:]]), *calc([numbers[0] * numbers[1], *numbers[2:]])]
  return [numbers[0]]


sum = 0

for line in splitfile:
  result, numbers = parse(line)
  if result in calc(numbers):
    sum += result

print(sum)
