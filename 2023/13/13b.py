with open("13/input.txt", "r") as f:
  splitfile = f.read().split("\n\n")
boxes = [[tuple(line) for line in box.split("\n")] for box in splitfile]


def translate_index(index, box):
  # Translates a 1d-index to 2d-coordinates
  return index // len(box[0]), index % len(box[0])


def other_symbol(symbol):
  if symbol == "#":
    return "."
  return "#"


def make_variation(box, symbol_index):
  # This is giga messy, but simply put it returns a box identical to the input
  # with the exception of a single flipped symbol, with the given index.
  chosen_row, chosen_col = translate_index(symbol_index, box)
  new_symbol = other_symbol(box[chosen_row][chosen_col])
  return [tuple([new_symbol if chosen_row == row and chosen_col == col else box[row][col] for col in range(len(box[row]))]) for row in range(len(box))]


def find_mirror(box, ignore):
  for i in range(len(box)):
    i_is_mirror = False
    j = 0

    # Check if position i gives mirror
    while i + j < len(box) and i - j - 1 >= 0:
      if box[i + j] == box[i - j - 1]:
        i_is_mirror = True
        j += 1
      else:
        i_is_mirror = False
        break
    if i_is_mirror and i != ignore:
      return i
  return False


def find_part_1(box):
  h_mirror = find_mirror(box, -1)
  if h_mirror != False:
    return 100 * h_mirror
  else:
    return find_mirror(tuple(zip(*box)), -1)


total_sum = 0
for box in boxes:
  # Iterate through all possible variations of box
  # Stop when a variation is found
  for variation in range(len(box) * len(box[0])):
    variation_box = make_variation(box, variation)
    part_1 = find_part_1(box)
    h_mirror = 100 * find_mirror(variation_box, part_1 // 100)
    v_mirror = find_mirror(tuple(zip(*variation_box)), part_1)

    if h_mirror:
      total_sum += h_mirror
      break
    elif v_mirror:
      total_sum += v_mirror
      break

print(total_sum)
