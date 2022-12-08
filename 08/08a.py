f = open("08/input.txt", "r").read().splitlines()
# assumes quadratic grid
length = len(f[0])

visible_trees = [[False for i in range(length)] for j in range(length)]
cardinal_directions = ["n", "e", "s", "w"]

def tree (direction, n1, n2):
  match direction:
    case "n":
      return [n2, n1]
    case "e":
      return [n1, length - (n2 + 1)]
    case "s":
      return [length - (n2 + 1), n1]
    case "w":
      return [n1, n2]


for dir in cardinal_directions: 
  highest_tree = [-1] * length
  for n1 in range(length):
    for n2 in range(length):
      tree_height = int(f[tree(dir, n1, n2)[0]][tree(dir, n1, n2)[1]])
      if tree_height > highest_tree[n1]:
        visible_trees[tree(dir, n1, n2)[0]][tree(dir, n1, n2)[1]] = True
        highest_tree[n1] = tree_height
    
print(sum(row.count(True) for row in visible_trees))