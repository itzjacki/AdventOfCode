with open("04/input.txt", "r") as f:
  splitfile = f.read().split("\n")

# Oh man i really regret my choices in part 1 now...
sum = 0

for row in range(1, len(splitfile) - 1):
  for col in range(1, len(splitfile[row]) - 1):
    if splitfile[row][col] == "A":
      # This makes me want to see how my eyes react to having napalm poured on them
      if ((splitfile[row - 1][col - 1] == "M" and splitfile[row + 1][col + 1] == "S") or (splitfile[row - 1][col - 1] == "S" and splitfile[row + 1][col + 1] == "M")) and ((splitfile[row + 1][col - 1] == "M" and splitfile[row - 1][col + 1] == "S") or (splitfile[row + 1][col - 1] == "S" and splitfile[row - 1][col + 1] == "M")):
        sum += 1

print(sum)
