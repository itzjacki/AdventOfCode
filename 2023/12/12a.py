with open("12/input.txt", "r") as f:
  splitfile = f.read().split("\n")

rows = [(list(row.split(" ")[0]), [int(n) for n in row.split(" ")[1].split(",")]) for row in splitfile]

def check_list(l, nums):
  result = []
  buffer = 0
  for c in l:
    if c == "#":
      buffer += 1
    else:
      if buffer > 0:
        result.append(buffer)
      buffer = 0
  if buffer > 0:
    result.append(buffer)
  return result == nums

total_sum = 0

for row in rows:
  springs = row[0]
  numbers = row[1]

  def make_variations(l):
    if "?" in l:
      first_unknown = l.index("?")
      make_variations(["." if i == first_unknown else c for i, c in enumerate(l)])
      make_variations(["#" if i == first_unknown else c for i, c in enumerate(l)])
    else:
      if check_list(l, numbers):
        global total_sum
        total_sum += 1

  make_variations(springs)

print(total_sum)