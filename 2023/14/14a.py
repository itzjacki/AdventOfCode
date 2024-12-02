with open("14/input.txt", "r") as f:
  splitfile = f.read().split("\n")

square_rocks = []
round_rocks = []

for row, line in enumerate(splitfile):
  for col, rock in enumerate(line):
    if rock == "#":
      square_rocks.append([row, col])
    if rock == "O":
      round_rocks.append([row, col])


def roll_rock(rock):
  global square_rocks, round_rocks

  [row, col] = rock
  new_row = row

  for i in range(row - 1, -1, -1):
    if [i, col] in square_rocks or [i, col] in round_rocks:
      break
    else:
      new_row = i

  rock[0] = new_row


for rock in round_rocks:
  roll_rock(rock)


total_load = 0

for rock in round_rocks:
  total_load += len(splitfile) - rock[0]


def print_round(round_rocks):
  for row in range(len(splitfile)):
    for col in range(len(splitfile[0])):
      if [row, col] in round_rocks:
        print("O", end="")
      else:
        print(".", end="")
    print("\n")


# print_round(round_rocks)
print(total_load)
print(len(round_rocks))
