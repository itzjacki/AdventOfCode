import re

with open("04/input.txt", "r") as f:
  splitfile = f.read().split("\n")


def transpose(matrix):
  return list(zip(*matrix))


def mirror(matrix):
  return [line[::-1] for line in matrix]


def diagonal_transpose(matrix):
  result = []
  for i in range(len(matrix)):
    top_left_row = []
    bottom_right_row = []
    for j in range(i + 1):
      top_left_row.append(matrix[i - j][j])
      # Make sure middle diagonal isn't counted twice
      if i < len(matrix) - 1:
        bottom_right_row.append(
            matrix[len(matrix) - j - 1][len(matrix) - i + j - 1])

    result.append(top_left_row)
    if len(bottom_right_row) > 0:
      result.append(bottom_right_row)

  return result


def count_in_matrix(matrix):
  sum = 0
  for line in matrix:
    hits = re.findall("XMAS", "".join(line))
    reverse_hits = re.findall("XMAS", "".join(line[::-1]))
    sum += len(hits) + len(reverse_hits)
  return sum


sum = 0
sum += count_in_matrix(splitfile)
sum += count_in_matrix(transpose(splitfile))
sum += count_in_matrix(diagonal_transpose(splitfile))
sum += count_in_matrix(diagonal_transpose(mirror(splitfile)))
print(sum)
