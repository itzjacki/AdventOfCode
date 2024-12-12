with open("12/test.txt", "r") as f:
  garden = [list(row) for row in f.read().split("\n")]


def plot(tile):
  if 0 <= tile[0] < len(garden) and 0 <= tile[1] < len(garden[0]):
    return garden[tile[0]][tile[1]]
  return "."


def neighbors(tile):
  (y, x) = tile
  return [((y - 1, x), "S"), ((y, x - 1), "W"), ((y + 1, x), "N"), ((y, x + 1), "E")]


def side_neighbors(tile_with_direction):
  ((y, x), direction) = tile_with_direction
  if direction == "N" or direction == "S":
    return [(y, x - 1), (y, x + 1)]
  if direction == "E" or direction == "W":
    return [(y - 1, x), (y + 1, x)]


def remove_direction(l, tile_with_dir, ignore=((-1, -1), "N")):
  if tile_with_dir in l and tile_with_dir != ignore:
    l.remove(tile_with_dir)


def number_of_sides(sides):
  sides_list = list(sides)
  for (tile, direction) in sides_list:
    for potential_neighbor in side_neighbors((tile, direction)):
      remove_direction(sides_list, (potential_neighbor, direction),
                       (tile, direction))
  return len(sides_list)


def find_region(tile):
  # print(tile)
  to_search = set()
  searched = set()
  area = 0
  sides = set()

  if plot(tile) != ".":
    to_search.add(tile)

  while to_search:
    current_tile = to_search.pop()
    searched.add(current_tile)
    val = plot(current_tile)
    area += 1

    for (neighbor, direction) in neighbors(current_tile):
      if plot(neighbor) != "." and val == plot(neighbor):
        if neighbor not in searched and neighbor not in to_search:
          to_search.add(neighbor)
      else:
        if neighbor not in searched:
          sides.add((current_tile, direction))

    garden[current_tile[0]][current_tile[1]] = "."
  if number_of_sides(sides) * area > 0:
    print("Sides", number_of_sides(sides), "area", area)
  return number_of_sides(sides) * area


sum = 0
for row in range(len(garden)):
  for col in range(len(garden[row])):
    sum += find_region((row, col))

print(sum)
