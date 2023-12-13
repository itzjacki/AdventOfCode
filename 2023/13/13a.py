from timeit import timeit

with open("13/input.txt", "r") as f:
  splitfile = f.read().split("\n\n")
boxes = [[tuple(line) for line in box.split("\n")] for box in splitfile]


def find_mirror(box):
  for i in range(len(box)):
    i_is_mirror = False
    j = 0
    while i + j < len(box) and i - j - 1 >= 0:
      if box[i + j] == box[i - j - 1]:
        i_is_mirror = True
        j += 1
      else:
        i_is_mirror = False
        break

    if i_is_mirror:
      return i
  return False


total_sum = 0
for box in boxes:
  h_mirror = find_mirror(box)
  if h_mirror:
    total_sum += 100 * h_mirror
  else:
    total_sum += find_mirror(tuple(zip(*box)))
print(total_sum)
