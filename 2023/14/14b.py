from functools import cache

with open("14/test.txt", "r") as f:
  splitfile = f.read().split("\n")

square_rocks_l = []
round_rocks_l = []

for row, line in enumerate(splitfile):
  for col, rock in enumerate(line):
    if rock == "#":
      square_rocks_l.append((row, col))
    if rock == "O":
      round_rocks_l.append((row, col))

square_rocks = tuple(square_rocks_l)
round_rocks = tuple(round_rocks_l)


def roll_rock(rock_t, direction, square_rocks, round_rocks):
  rock = list(rock_t)

  [row, col] = rock

  if direction == "north":
    for i in range(row - 1, -1, -1):
      if [i, col] in square_rocks or [i, col] in round_rocks:
        break
      else:
        rock[0] = i
  if direction == "west":
    for i in range(col - 1, -1, -1):
      if [row, i] in square_rocks or [row, i] in round_rocks:
        break
      else:
        rock[1] = i
  if direction == "south":
    for i in range(row + 1, len(splitfile)):
      if [i, col] in square_rocks or [i, col] in round_rocks:
        break
      else:
        rock[0] = i
  if direction == "east":
    for i in range(col + 1, len(splitfile[0])):
      if [row, i] in square_rocks or [row, i] in round_rocks:
        break
      else:
        rock[1] = i

  return tuple(rock)


@cache
def do_round(round_rocks_t):
  global square_rocks
  round_rocks = list(round_rocks_t)
  round_rocks = sorted(round_rocks, key=lambda x: x[0])

  for rock in round_rocks:
    rock = roll_rock(tuple(rock), "north", square_rocks, round_rocks)

  round_rocks = sorted(round_rocks, key=lambda x: x[1])
  for rock in round_rocks:
    rock = roll_rock(tuple(rock), "west", square_rocks, round_rocks)

  round_rocks = sorted(round_rocks, key=lambda x: 0-x[0])
  for rock in round_rocks:
    rock = roll_rock(tuple(rock), "south", square_rocks, round_rocks)

  round_rocks = sorted(round_rocks, key=lambda x: 0-x[1])
  for rock in round_rocks:
    rock = roll_rock(tuple(rock), "east", square_rocks, round_rocks)

  return tuple(round_rocks)


l = []
r = round_rocks
for i in range(1_0):
  r = do_round(r)

  total_load = 0

  for rock in r:
    total_load += len(splitfile) - rock[0]
  l.append(total_load)

print(l)


def print_round(round_rocks, square_rocks):
  for row in range(len(splitfile)):
    for col in range(len(splitfile[0])):
      if [row, col] in round_rocks:
        print("O", end="")
      elif [row, col] in square_rocks:
        print("#", end="")
      else:
        print(".", end="")
    print("\n")


# print(total_load)
# print_round(r, square_rocks)

# print(loads)
