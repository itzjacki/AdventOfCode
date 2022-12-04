f = open("03/input.txt", "r").read().split("\n")

def toPriority(letter):
  if ord(letter) > 91:
    return ord(letter) - 96 
  return ord(letter) - 38

totalPriority = 0
for i in range(int(len(f)/3)):
  for item in f[i * 3]:
    if item in f[i * 3 + 1] and item in f[i * 3 + 2]: 
      print(item)
      totalPriority += toPriority(item)
      break

print(totalPriority)
