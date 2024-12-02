with open("17/test.txt", "r") as f:
  splitfile = f.read().split("\n")

blocks = [[int(n) for n in line] for line in splitfile]
