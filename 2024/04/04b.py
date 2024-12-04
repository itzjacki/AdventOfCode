with open("04/input.txt", "r") as f:
  splitfile = f.read().split("\n")

# Oh man i really regret my choices in part 1 now...
sum = 0


def tile(row, col):
  return splitfile[row][col]


def val(letter):
  return 1 if letter == 'M' else 2 if letter == 'S' else 0


def is_mas_cross(row, col):
  if tile(row, col) != 'A':
    return False
  checksum = (val(tile(row - 1, col - 1)) + val(tile(row + 1, col + 1)),
              val(tile(row + 1, col - 1)) + val(tile(row - 1, col + 1)))
  return checksum == (3, 3)


for row in range(1, len(splitfile) - 1):
  for col in range(1, len(splitfile[row]) - 1):
    if is_mas_cross(row, col):
      sum += 1

print(sum)
