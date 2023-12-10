with open("10/input.txt", "r") as f:
  splitfile = f.read().split("\n")

pipes = [[x for x in y] for y in splitfile]

def pipe(position):
  return pipes[position[0]][position[1]]

path = []
start_pos = None

for y, row in enumerate(pipes):
  for x, col in enumerate(row):
    if col == "S":
      start_pos = (y, x)

pos = start_pos
from_direction = None
back_at_start = False

# I don't like this either
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
    if from_direction == "west":
      go("east")
    if from_direction == "east":
      go("west")
  elif current_pipe == "|":
    if from_direction == "north":
      go("south")
    if from_direction == "south":
      go("north")
  elif current_pipe == "7":
    if from_direction == "west":
      go("south")
    if from_direction == "south":
      go("west")
  elif current_pipe == "L":
    if from_direction == "north":
      go("east")
    if from_direction == "east":
      go("north")
  elif current_pipe == "J":
    if from_direction == "north":
      go("west")
    if from_direction == "west":
      go("north")
  elif current_pipe == "F":
    if from_direction == "east":
      go("south")
    if from_direction == "south":
      go("east")

  back_at_start = pos == start_pos

print(len(path)//2)