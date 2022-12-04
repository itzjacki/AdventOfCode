f = open("input.txt", "r")
splitfile = f.read().split("\n\n")
summedfile = []
highest_three = [0, 0, 0]

for single_elf in splitfile:
  inventory = single_elf.split("\n")
  sum_of_inventory = 0
  for calorie in inventory:
    if calorie != '':
      sum_of_inventory += int(calorie)
  if sum_of_inventory > min(highest_three):
    highest_three[highest_three.index(min(highest_three))] = sum_of_inventory

print("Highest single elf calorie number", max(highest_three))
print("Sum of highest three elf calorie scores", sum(highest_three))
