f = open("03/input.txt", "r").read().split("\n")
sacks = [[sack[:int(len(sack)/2)], sack[int(len(sack)/2):]] for sack in f]

def toPriority(letter):
  if ord(letter) > 91:
    return ord(letter) - 96 
  return ord(letter) - 38

totalPriority = 0
for sack in sacks:
  for item in sack[0]:
    if item in sack[1]:
      print(item)
      totalPriority += toPriority(item)
      break

print(totalPriority)
