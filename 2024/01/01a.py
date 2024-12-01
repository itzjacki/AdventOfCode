with open("01/input.txt", "r") as f:
  splitfile = f.read().split("\n")

list_a = []
list_b = []
for line in splitfile:
  values = line.split()
  list_a.append(values[0])
  list_b.append(values[1])

list_a.sort()
list_b.sort()


def diff_sum(a, b):
  sum = 0

  for idx, a_val in enumerate(a):
    sum += abs(int(a_val) - int(b[idx]))

  print(sum)


diff_sum(list_a, list_b)
