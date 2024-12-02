with open("02/input.txt", "r") as f:
  splitfile = f.read().split("\n")

number_safe = 0

for report in splitfile:
  levels = [int(num) for num in report.split()]

  increasing = levels[0] < levels[1]
  boundaries = (1, 3) if increasing else (-3, -1)
  safe = True

  for i in range(len(levels) - 1):
    if not boundaries[0] <= levels[i + 1] - levels[i] <= boundaries[1]:
      safe = False

  if safe:
    number_safe += 1

print(number_safe)
