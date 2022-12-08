with open("06/input.txt", "r") as file:
  f = file.read().splitlines()
n_uniques = 14

buffer = [None] * n_uniques
counter = 0

for i in range(len(f)):
  buffer.pop(0)
  counter += 1
  
  if f[i] in buffer:
    reversed_buffer = buffer.copy()
    reversed_buffer.reverse()
    counter = min(reversed_buffer.index(f[i]) + 1, counter)

  buffer.append(f[i])

  if counter >= n_uniques:
    print("found marker:", i + 1)
    break