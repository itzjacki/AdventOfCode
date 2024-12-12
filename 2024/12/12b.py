with open("12/input.txt", "r") as f:
  garden = [list(row) for row in f.read().split("\n")]


def plot(tile):
  if 0 <= tile[0] < len(garden) and 0 <= tile[1] < len(garden[0]):
    return garden[tile[0]][tile[1]]
  return "."


def get_neighbor(tile, direction):
  (y, x) = tile
  if direction == "N":
    return (y + 1, x)
  if direction == "E":
    return (y, x + 1)
  if direction == "S":
    return (y - 1, x)
  if direction == "W":
    return (y, x - 1)


def neighbors(tile):
  return [(get_neighbor(tile, "N"), "N"), (get_neighbor(tile, "E"), "E"), (get_neighbor(tile, "S"), "S"), (get_neighbor(tile, "W"), "W")]


def side_directions(direction):
  if direction == "N" or direction == "S":
    return ["W", "E"]
  if direction == "W" or direction == "E":
    return ["N", "S"]


def remove_in_direction(tile_with_direction, direction_to_remove, list_to_remove_from):
  (tile, direction) = tile_with_direction
  next_tile_with_direction = (get_neighbor(
      tile, direction_to_remove), direction)
  if next_tile_with_direction in list_to_remove_from:
    list_to_remove_from.remove(next_tile_with_direction)
    remove_in_direction(next_tile_with_direction,
                        direction_to_remove, list_to_remove_from)


def number_of_sides(sides):
  sides_list = list(sides)
  for tile_with_direction in sides_list:
    sides_to_check = side_directions(tile_with_direction[1])
    remove_in_direction(tile_with_direction, sides_to_check[0], sides_list)
    remove_in_direction(tile_with_direction, sides_to_check[1], sides_list)
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
    print(area, number_of_sides(sides))
  return number_of_sides(sides) * area


sum = 0
for row in range(len(garden)):
  for col in range(len(garden[row])):
    sum += find_region((row, col))

print(sum)
