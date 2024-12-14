import re

with open("14/input.txt", "r") as f:
  splitfile = f.read().split("\n")

board_width = 101
board_height = 103
iterations = 100

robots = [[int(n) for n in re.search("(-*\d+),(-*\d+)[^-\d]+(-*\d+),(-*\d+)",
                                     line).groups()] for line in splitfile]

robots_final = []
board = [[0] * board_width for _ in range(board_height)]

for robot in robots:
  [x, y, vx, vy] = robot
  new_x = (x + iterations * vx) % board_width
  new_y = (y + iterations * vy) % board_height
  robots_final.append((new_x, new_y))
  board[new_y][new_x] += 1

quadrants = [0, 0, 0, 0]

for robot in robots_final:
  if robot[0] + 1 < board_width / 2 and robot[1] + 1 < board_height / 2:
    quadrants[0] += 1
  if robot[0] > board_width / 2 and robot[1] + 1 < board_height / 2:
    quadrants[1] += 1
  if robot[0] + 1 < board_width / 2 and robot[1] > board_height / 2:
    quadrants[2] += 1
  if robot[0] > board_width / 2 and robot[1] > board_height / 2:
    quadrants[3] += 1

for line in board:
  print("".join(["." if n == 0 else str(n) for n in line]))

print(quadrants)
print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
