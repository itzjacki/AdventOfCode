with open("09/input.txt", "r") as file:
  f = file.read().splitlines()

grid_size = 400
h = [0, 0]
t = [0, 0]

visited_squares = [[False for i in range(grid_size)] for j in range(grid_size)]

def cap(n):
  if n > 0:
    return 1
  if n < 0:
    return -1
  return 0
  
def move_tail(diff):
  global t
  t = [t[0] + cap(diff[0]), t[1] + cap(diff[1])]
  visited_squares[t[0] + int(grid_size/2)][t[1] + int(grid_size/2)] = True

visited_squares[t[0] + int(grid_size/2)][t[1] + int(grid_size/2)] = True

for l in f:
  dir = l[0]
  dist = int(l[2:])
    
  for i in range(dist):
    match dir:
      case "U":
        h = [h[0], h[1] + 1]
      case "R":
        h = [h[0] + 1, h[1]]
      case "D":
        h = [h[0], h[1] - 1]
      case "L":
        h = [h[0] - 1, h[1]]

    diff = [h[0] - t[0], h[1] - t[1]]
    if not (-1 <= diff[0] <= 1 and -1 <= diff[1] <= 1):
      move_tail(diff)

print(sum(row.count(True) for row in visited_squares))