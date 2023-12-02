import re
with open("02/input.txt", "r") as f:
  splitfile = f.read().split("\n")

colors = ["red", "green", "blue"]
color_limits = {"red": 12, "green": 13, "blue": 14}
id_sum = 0

for i, game in enumerate(splitfile):
  game_possible = True
  rounds = game.split(";")
  for round in rounds:
    for color in colors:
      matches = re.search("(\d+) " + color, round)

      if matches is not None:
        if int(matches.groups()[0] )> color_limits[color]:
          game_possible = False
  
  if game_possible:
    id_sum += i + 1

print(id_sum)