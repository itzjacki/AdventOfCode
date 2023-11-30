with open("01/input.txt", "r") as f:
  splitfile = f.read().split("\n\n")

highest_score = 0

for single_elf in splitfile:
  inventory = single_elf.split("\n")
  sum_of_inventory = 0
  for calorie in inventory:
    if calorie != '':
      sum_of_inventory += int(calorie)
  if sum_of_inventory > highest_score:
    highest_score = sum_of_inventory

print("Highest single elf calorie number", highest_score)
