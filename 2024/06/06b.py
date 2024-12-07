from collections import defaultdict

with open("06/input.txt", "r") as f:
  splitfile = f.read().split("\n")


def tile(pos, override_tile=(-1, -1)):
  if pos == override_tile:
    return "#"
  if 0 <= pos[0] < len(splitfile) and 0 <= pos[1] < len(splitfile[0]):
    return splitfile[pos[0]][pos[1]]
  return None


def find_start(board):
  for idx, row in enumerate(board):
    if row.find("^") > -1:
      return idx, row.find("^")


def next_tile(y, x, dir):
  if dir == "N":
    return y - 1, x
  elif dir == "E":
    return y, x + 1
  elif dir == "S":
    return y + 1, x
  else:  # W
    return y, x - 1


def get_relevant_tiles(board):
  tiles_visited = set()
  row, col = find_start(splitfile)
  direction = "N"
  directions = ["N", "E", "S", "W"]

  while True:
    if tile((row, col)) == ".":
      tiles_visited.add((row, col))

    if tile(next_tile(row, col, direction)) == "#":
      direction = directions[(directions.index(
          direction) + 1) % len(directions)]
    elif tile(next_tile(row, col, direction)) == None:
      break

    row, col = next_tile(row, col, direction)

  return tiles_visited


def is_loop(board, override_tile):
  tiles_visited = defaultdict(list)
  row, col = find_start(board)
  direction = "N"
  directions = ["N", "E", "S", "W"]

  while True:
    if direction in tiles_visited[(row, col)]:
      return True
    else:
      tiles_visited[(row, col)].append(direction)

    if tile(next_tile(row, col, direction), override_tile) == "#":
      direction = directions[(directions.index(
          direction) + 1) % len(directions)]
    elif tile(next_tile(row, col, direction), override_tile) == None:
      return False

    row, col = next_tile(row, col, direction)


loops = 0

tiles_to_check = get_relevant_tiles(splitfile)

for index, (row_index, col_index) in enumerate(tiles_to_check):
  if is_loop(splitfile, (row_index, col_index)):
    loops += 1
  print(index, "/", len(tiles_to_check))

print(loops)
