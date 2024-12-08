from collections import defaultdict

with open("08/input.txt", "r") as f:
  splitfile = f.read().split("\n")

antennas = defaultdict(list)
antenodes = set()


def sub_tuples(tup1, tup2):
  return (tup1[0] - tup2[0], tup1[1] - tup2[1])


def find_antenode(antenna1, antenna2, num):
  vec = sub_tuples(antenna2, antenna1)
  return sub_tuples(antenna1, (num * vec[0], num * vec[1]))


def within_bounds(coords):
  return 0 <= coords[0] < len(splitfile) and 0 <= coords[1] < len(splitfile[0])


def find_antenodes(antenna_list):
  for antenna1 in antenna_list:
    for antenna2 in antenna_list:
      if antenna1 != antenna2:
        i = 0
        while within_bounds(find_antenode(antenna1, antenna2, i)):
          antenodes.add(find_antenode(antenna1, antenna2, i))
          i += 1


for row_index, row in enumerate(splitfile):
  for col_index, sign in enumerate(row):
    if sign != ".":
      antennas[sign].append((row_index, col_index))

for letter in antennas:
  find_antenodes(antennas[letter])

print(len(antenodes))
