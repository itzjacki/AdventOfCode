with open("15/input.txt", "r") as f:
  [board, moves] = f.read().split("\n\n")

board = [list(line) for line in board.split("\n")]
moves = moves.replace("\n", "")


def sum_tuples(t1, t2):
  return tuple(sum(x) for x in zip(t1, t2))


def tile(coords):
  return board[coords[0]][coords[1]]


def set_tile(coords, value):
  board[coords[0]][coords[1]] = value


def get_change_vector(move):
  if move == "^":
    return (-1, 0)
  if move == ">":
    return (0, 1)
  if move == "v":
    return (1, 0)
  if move == "<":
    return (0, -1)


def find_space(pos, change):
  new_pos = sum_tuples(pos, change)
  tile_on_new_pos = tile(new_pos)
  if tile_on_new_pos == "#":
    return False
  if tile_on_new_pos == ".":
    return new_pos
  if tile_on_new_pos == "O":
    return find_space(new_pos, change)


def robot():
  for row_idx, row in enumerate(board):
    for col_idx, v in enumerate(row):
      if v == "@":
        return (row_idx, col_idx)


robot_pos = robot()

for move in moves:
  change_vector = get_change_vector(move)
  next_free = find_space(robot_pos, change_vector)
  neighbor_tile = sum_tuples(robot_pos, change_vector)
  if next_free == False:
    continue
  if next_free == neighbor_tile:
    set_tile(robot_pos, ".")
    set_tile(next_free, "@")
    robot_pos = next_free
  else:
    set_tile(robot_pos, ".")
    set_tile(neighbor_tile, "@")
    set_tile(next_free, "O")
    robot_pos = neighbor_tile

gps_sum = 0

for row_idx, row in enumerate(board):
  for col_idx, v in enumerate(row):
    if v == "O":
      gps_sum += 100 * row_idx + col_idx

print(gps_sum)
