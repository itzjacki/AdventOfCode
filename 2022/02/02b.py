with open("02/input.txt", "r") as f:
  splitfile = f.readlines()
  
summedscore = 0

for game in splitfile:
  a = ord(game[0]) - 64
  b = ord(game[2]) - 87
  if b == 1: # X LOSE
    summedscore += 0 + (a - 1 - 1) % 3 + 1
  if b == 2: # Y DRAW
    summedscore += 3 + a
  if b == 3: # Z WIN
    summedscore += 6 + (a - 1 + 1) % 3 + 1

print(summedscore)
