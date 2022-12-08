with open("08/input.txt", "r") as file:
  f = file.read().splitlines()
# assumes quadratic grid
length = len(f[0])

scores = [[0 for i in range(length)] for j in range(length)]
cardinal_directions = ["n", "e", "s", "w"]

def find_distance (direction, n1, n2):
  own_height = int(f[n1][n2])
  highest_seen = -1
  number_seen = 0
  while own_height > highest_seen:
    number_seen += 1
    match direction:
      case "n":
        if n1 - number_seen < 0:
          number_seen -= 1
          break
        highest_seen = int(f[n1 - number_seen][n2])
      case "e":
        if n2 + number_seen >= length:
          number_seen -= 1
          break
        highest_seen = int(f[n1][n2 + number_seen])
      case "s":
        if n1 + number_seen >= length:
          number_seen -= 1
          break
        highest_seen = int(f[n1 + number_seen][n2])
      case "w":
        if n2 - number_seen < 0:
          number_seen -= 1
          break
        highest_seen = int(f[n1][n2 - number_seen])
  return number_seen


for n1 in range(length):
  for n2 in range(length):
    tree_score = 1
    for dir in cardinal_directions:
      tree_score *= find_distance(dir, n1, n2)
    scores[n1][n2] = tree_score

print(max(max(row) for row in scores))