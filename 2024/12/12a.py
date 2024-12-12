with open("12/input.txt", "r") as f:
  garden = [list(row) for row in f.read().split("\n")]


def plot(tile):
  if 0 <= tile[0] < len(garden) and 0 <= tile[1] < len(garden[0]):
    return garden[tile[0]][tile[1]]
  return "."


def neighbors(tile):
  (y, x) = tile
  return [(y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)]


def find_region(tile):
  # print(tile)
  to_search = set()
  searched = set()
  perimeter, area = 0, 0

  if plot(tile) != ".":
    to_search.add(tile)

  while to_search:
    current_tile = to_search.pop()
    searched.add(current_tile)
    val = plot(current_tile)
    area += 1

    for neighbor in neighbors(current_tile):
      if plot(neighbor) != "." and val == plot(neighbor):
        if neighbor not in searched and neighbor not in to_search:
          to_search.add(neighbor)
      else:
        if neighbor not in searched:
          perimeter += 1

    garden[current_tile[0]][current_tile[1]] = "."

  # print("Perimiter", perimeter, "Area", area)
  return perimeter * area


sum = 0
for row in range(len(garden)):
  for col in range(len(garden[row])):
    sum += find_region((row, col))

print(sum)
