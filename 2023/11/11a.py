with open("11/test.txt", "r") as f:
  splitfile = f.read().split("\n")

universe = [[c for c in row] for row in splitfile]

initial_height = len(universe)
initial_width = len(universe[0])
rows_empty = [True] * initial_height
cols_empty = [True] * initial_width

# Expand universe
# There is a much more elgant way to solve this problem that doesn't involve
# expanding my string and reading it over and over again, but i think i can
# implement this one faster. Hope it doesn't come back to bite me in part 2

for row_n, row in enumerate(universe):
  for col_n, col in enumerate(row):
    if col == "#":
      rows_empty[row_n] = False
      cols_empty[col_n] = False

for row_n in range(len(rows_empty) - 1, -1, -1):
  if rows_empty[row_n]:
    universe.insert(row_n, ["."] * initial_width)

for col_n in range(len(cols_empty) - 1, -1, -1):
  if cols_empty[col_n]:
    for row_n in range(len(universe)):
      universe[row_n].insert(col_n, ".")

# Find galaxies

galaxies = []

for row_n, row in enumerate(universe):
  for col_n, col in enumerate(row):
    if col == "#":
      galaxies.append((row_n, col_n))

sum = 0

for i, galaxy in enumerate(galaxies):
  if i + 1 < len(galaxies):
    for other_galaxy in galaxies[(i + 1):]:
      sum += abs(other_galaxy[0] - galaxy[0]) + abs(other_galaxy[1] - galaxy[1])

print(sum)