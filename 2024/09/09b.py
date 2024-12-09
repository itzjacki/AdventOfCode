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
  return sum([idx * v if v != "." else 0 for idx, v in enumerate(l)])


def find_free(disk, length):
  counter = 0
  for idx, c in enumerate(disk):
    if c == ".":
      counter += 1
      if counter >= length:
        return idx - length + 1
    else:
      counter = 0
  return -1


disk = make_map()
free_spot = disk.index(".")

buffer = []

for i in range(len(disk) - 1, -1, -1):
  if len(buffer) == 0 or buffer[0] == disk[i]:
    if disk[i] != ".":
      buffer.append(disk[i])
      if i <= disk.index("."):
        break
      disk[i] = "#"
  else:
    spot_index = find_free(disk, len(buffer))
    if spot_index > -1 and spot_index < disk.index("#"):
      disk = disk[:spot_index] + buffer + \
          disk[spot_index + len(buffer):]
      disk = ["." if v == "#" else v for v in disk]
    else:
      disk = disk[:disk.index("#")] + buffer + \
          disk[disk.index("#") + len(buffer):]
    if disk[i] != ".":
      if i <= disk.index("."):
        break
      buffer = [disk[i]]
      disk[i] = "#"
    else:
      buffer = []
print(checksum(disk))
