with open("10/input.txt", "r") as f:
  splitfile = f.read().split("\n")

pipes = [[x for x in y] for y in splitfile]

def pipe(position):
  return pipes[position[0]][position[1]]

path = []
tiles_inside = []
start_pos = None

for y, row in enumerate(pipes):
  for x, col in enumerate(row):
    if col == "S":
      start_pos = (y, x)

pos = start_pos
from_direction = None
back_at_start = False

# I don't like this either. I thought scoped worked kinda differently in python
# #JustJSDevThings
def go(direction):
  match direction:
    case "east":
      globals()["pos"] = (globals()["pos"][0], globals()["pos"][1] + 1)
      globals()["from_direction"] = "west"
    case "west":
      globals()["pos"] = (globals()["pos"][0], globals()["pos"][1] - 1)
      globals()["from_direction"] = "east"
    case "north":
      globals()["pos"] = (globals()["pos"][0] - 1, globals()["pos"][1])
      globals()["from_direction"] = "south"
    case "south":
      globals()["pos"] = (globals()["pos"][0] + 1, globals()["pos"][1])
      globals()["from_direction"] = "north"


while not back_at_start:
  path.append(pos)
  current_pipe = pipe(pos)
  
  if current_pipe == "S":  # We assume we can go east from the start
    go("east")
  elif current_pipe == "-":
    # We assume we're moving clockwise around the loop
    if from_direction == "west":
      tiles_inside.append((pos[0] + 1, pos[1]))
      go("east")
    if from_direction == "east":
      tiles_inside.append((pos[0] - 1, pos[1]))
      go("west")
  elif current_pipe == "|":
    if from_direction == "north":
      tiles_inside.append((pos[0], pos[1] - 1))
      go("south")
    if from_direction == "south":
      tiles_inside.append((pos[0], pos[1] + 1))
      go("north")
  elif current_pipe == "7":
    if from_direction == "west":
      go("south")
    if from_direction == "south":
      tiles_inside.append((pos[0] - 1, pos[1]))
      tiles_inside.append((pos[0], pos[1] + 1))
      go("west")
  elif current_pipe == "L":
    if from_direction == "north":
      tiles_inside.append((pos[0] + 1, pos[1]))
      tiles_inside.append((pos[0], pos[1] - 1))
      go("east")
    if from_direction == "east":
      go("north")
  elif current_pipe == "J":
    if from_direction == "north":
      go("west")
    if from_direction == "west":
      tiles_inside.append((pos[0] + 1, pos[1]))
      tiles_inside.append((pos[0], pos[1] + 1))
      go("north")
  elif current_pipe == "F":
    if from_direction == "east":
      tiles_inside.append((pos[0] - 1, pos[1]))
      tiles_inside.append((pos[0], pos[1] - 1))
      go("south")
    if from_direction == "south":
      go("east")

  back_at_start = pos == start_pos

# Now we expand our selection so we find the ones not just directly touching the path
# We take the unique, non-path tiles that are touching the path on the inside
tiles_to_add = [p for p in list(dict.fromkeys(tiles_inside)) if p not in path]
final_tiles = []

while len(tiles_to_add) != 0:
  new_tiles = []

  for tile in tiles_to_add:
    if tile not in final_tiles and tile not in path:
      final_tiles.append(tile)
      new_tiles.append((tile[0] + 1, tile[1]))
      new_tiles.append((tile[0] - 1, tile[1]))
      new_tiles.append((tile[0], tile[1] + 1))
      new_tiles.append((tile[0], tile[1] - 1))
  
  tiles_to_add = new_tiles

print(len(final_tiles))