with open("09/input.txt", "r") as f:
  splitfile = f.read()


def make_map():
  disk = []
  for idx, c in enumerate(splitfile):
    if idx % 2 == 0:  # data
      disk.extend(([idx // 2] * int(c)))
    else:
      disk.extend(["."] * int(c))
  return disk


def checksum(l):
  return sum([idx * v for idx, v in enumerate(l)])


disk = make_map()
first_free = disk.index(".")  # small optimization that might pay off


while first_free != -1:
  if disk[-1] == ".":
    disk.pop()
  else:
    disk[first_free] = disk.pop()
  try:
    first_free = disk.index(".", first_free)
  except ValueError:
    first_free = -1

print(checksum(disk))
