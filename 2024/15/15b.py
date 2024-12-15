with open("15/input.txt", "r") as f:
  [board, moves] = f.read().split("\n\n")


def extend_board(board):
  result = []
  for line in board:
    new = []
    for c in line:
      if c == ".":
        new.extend([".", "."])
      if c == "#":
        new.extend(["#", "#"])
      if c == "@":
        new.extend(["@", "."])
      if c == "O":
        new.extend(["[", "]"])
    result.append(new)
  return result


moves = moves.replace("\n", "")
board = extend_board([list(line) for line in board.split("\n")])


def sum_tuples(t1, t2):
  return tuple(sum(x) for x in zip(t1, t2))


def scalar_x_tuple(t, s):
  return tuple(s * v for v in t)


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


def move_into_free_space(pos, move):
  if tile(sum_tuples(pos, move)) == ".":
    set_tile(sum_tuples(pos, move), "@")
    set_tile(pos, ".")
    return True
  return False


# Returns position of other half of box
def get_other_box_pos(pos):
  if tile(pos) == "[":
    return sum_tuples(pos, (0, 1))
  elif tile(pos) == "]":
    return sum_tuples(pos, (0, -1))
  else:
    print("Position wrongly assumed to be box part turned out to be", tile(pos))
    raise ValueError


# Checks if crate in direction move from position pos is blocked from moving
def is_blocked(pos, move):
  # Horizontal move
  if move[0] == 0:
    behind_block = tile(sum_tuples(pos, scalar_x_tuple(move, 3)))
    if behind_block == "#":
      return True
    if behind_block == ".":
      return False
    return is_blocked(sum_tuples(pos, move), move)
  # Vertical move
  else:
    box_pos = sum_tuples(pos, move)
    if tile(box_pos) == "[" or tile(box_pos) == "]":
      other_box_pos = get_other_box_pos(box_pos)

      # Check for box immediately behind
      if tile(sum_tuples(other_box_pos, move)) == "#" or tile(sum_tuples(box_pos, move)) == "#":
        return True
      if tile(sum_tuples(other_box_pos, move)) == "." and tile(sum_tuples(box_pos, move)) == ".":
        return False
      return is_blocked(box_pos, move) or is_blocked(other_box_pos, move)
    else:
      return False


# Pushes block at pos in direction move
def push_block(pos, move):

  # Horizontal move
  if move[0] == 0:
    if tile(pos) == "[" or tile(pos) == "]":
      push_block(sum_tuples(pos, move), move)
      set_tile(sum_tuples(pos, move), tile(pos))
      set_tile(pos, ".")

  # Vertical move
  else:
    if tile(pos) == "[" or tile(pos) == "]":
      other_box_pos = get_other_box_pos(pos)
      if tile(pos) == "[" or tile(pos) == "]":
        push_block(sum_tuples(pos, move), move)
        set_tile(sum_tuples(pos, move), tile(pos))
        set_tile(pos, ".")
      if tile(other_box_pos) == "[" or tile(other_box_pos) == "]":
        push_block(sum_tuples(other_box_pos, move), move)
        set_tile(sum_tuples(other_box_pos, move), tile(other_box_pos))
        set_tile(other_box_pos, ".")


def robot():
  for row_idx, row in enumerate(board):
    for col_idx, v in enumerate(row):
      if v == "@":
        return (row_idx, col_idx)


robot_pos = robot()

for move in moves:
  change_vector = get_change_vector(move)

  # There is free space in front of the robot
  if move_into_free_space(robot_pos, change_vector):
    robot_pos = sum_tuples(robot_pos, change_vector)

  # The robot is facing a wall
  elif tile(sum_tuples(robot_pos, change_vector)) == "#":
    continue

  # The robot is facing crates which cannot be moved
  elif is_blocked(robot_pos, change_vector):
    continue

  # The robot is facing crates which can be moved
  else:
    push_block(sum_tuples(robot_pos, change_vector), change_vector)
    move_into_free_space(robot_pos, change_vector)
    robot_pos = sum_tuples(robot_pos, change_vector)


gps_sum = 0

for row_idx, row in enumerate(board):
  for col_idx, v in enumerate(row):
    if v == "[":
      gps_sum += 100 * row_idx + col_idx

print(gps_sum)
