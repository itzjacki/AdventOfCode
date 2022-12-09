with open("09/input.txt", "r") as file:
  f = file.read().splitlines()

grid_size = 400
rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

visited_squares = [[False for i in range(grid_size)] for j in range(grid_size)]

def cap(n):
  if n > 0:
    return 1
  if n < 0:
    return -1
  return 0
  
def move_tail(diff, rope, i):
  rope[i] = [rope[i][0] + cap(diff[0]), rope[i][1] + cap(diff[1])]

visited_squares[rope[-1][0] + int(grid_size/2)][rope[-1][1] + int(grid_size/2)] = True

for l in f:
  dir = l[0]
  dist = int(l[2:])
    
  for i in range(dist):
    match dir:
      case "U":
        rope[0] = [rope[0][0], rope[0][1] + 1]
      case "R":
        rope[0] = [rope[0][0] + 1, rope[0][1]]
      case "D":
        rope[0] = [rope[0][0], rope[0][1] - 1]
      case "L":
        rope[0] = [rope[0][0] - 1, rope[0][1]]
      
    for i in range(1, len(rope)):
      diff = [rope[i - 1][0] - rope[i][0], rope[i - 1][1] - rope[i][1]]
      if not (-1 <= diff[0] <= 1 and -1 <= diff[1] <= 1):
        move_tail(diff, rope, i)
    visited_squares[rope[-1][0] + int(grid_size/2)][rope[-1][1] + int(grid_size/2)] = True

print(sum(row.count(True) for row in visited_squares))