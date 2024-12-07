with open("06/input.txt", "r") as f:
  splitfile = f.read().split("\n")


def tile(pos):
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


tiles_visited = set()
row, col = find_start(splitfile)
direction = "N"
directions = ["N", "E", "S", "W"]

while True:
  tiles_visited.add((row, col))

  if tile(next_tile(row, col, direction)) == "#":
    direction = directions[(directions.index(direction) + 1) % len(directions)]
  elif tile(next_tile(row, col, direction)) == None:
    break

  row, col = next_tile(row, col, direction)

print(len(tiles_visited))
