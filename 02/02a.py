with open("02/input.txt", "r") as f:
  splitfile = f.readlines()
  
summedscore = 0

for game in splitfile:
  a = ord(game[0]) - 65
  b = ord(game[2]) - 88

  summedscore += b + 1
  if a == b:
    summedscore += 3
  if (a - b == -1) or (a - b == 2):
    summedscore += 6

print(summedscore)
