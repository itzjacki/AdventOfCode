import time
import re

with open("14/input.txt", "r") as f:
  splitfile = f.read().split("\n")

board_width = 101
board_height = 103

for iterations in range(97, 10000, 101):

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

  print("\n\nITERATIO:N", iterations, "\n\n")
  for line in board:
    print("".join(["." if n == 0 else str(n) for n in line]))

  time.sleep(0.5)
