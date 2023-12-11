with open("11/input.txt", "r") as f:
  splitfile = f.read().split("\n")

universe = [[c for c in row] for row in splitfile]
expansion = 1_000_000

initial_height = len(universe)
initial_width = len(universe[0])
rows_empty = [True] * initial_height
cols_empty = [True] * initial_width

# Expand universe
# Well, well, well, if it isn't the consequences of my own actions...

for row_n, row in enumerate(universe):
  for col_n, col in enumerate(row):
    if col == "#":
      rows_empty[row_n] = False
      cols_empty[col_n] = False

rows_to_expand = [i for i, row in enumerate(rows_empty) if row]
cols_to_expand = [i for i, col in enumerate(cols_empty) if col]
# Find galaxies

galaxies = []

for row_n, row in enumerate(universe):
  for col_n, col in enumerate(row):
    if col == "#":
      galaxies.append((row_n, col_n))

# Account for expansion in galaxy positions

new_galaxies = []

for galaxy in galaxies:
  rows_expanded = sum([1 for row in rows_to_expand if row < galaxy[0]])
  cols_expanded = sum([1 for col in cols_to_expand if col < galaxy[1]])
  new_galaxies.append((galaxy[0] + rows_expanded * (expansion - 1), galaxy[1] + cols_expanded * (expansion - 1)))
  

# Find distance

sum = 0

for i, galaxy in enumerate(new_galaxies):
  if i + 1 < len(new_galaxies):
    for other_galaxy in new_galaxies[(i + 1):]:
      sum += abs(other_galaxy[0] - galaxy[0]) + abs(other_galaxy[1] - galaxy[1])

print(sum)