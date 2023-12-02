import re
with open("02/input.txt", "r") as f:
  splitfile = f.read().split("\n")

colors = ["red", "green", "blue"]
power_sum = 0

for i, game in enumerate(splitfile):
  mins={}
  for color in colors:
    mins[color] = 0

  rounds = game.split(";")
  for round in rounds:
    for color in colors:
      matches = re.search("(\d+) " + color, round)

      if matches is not None:
        number_of_color = int(matches.groups()[0])
        if number_of_color > mins[color]:
          mins[color] = number_of_color
  
  power = 1
  for v in mins.values():
    power *= v
  power_sum += power

print(power_sum)