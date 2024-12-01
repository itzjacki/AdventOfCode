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


def frequency_table(list):
  result = {}
  for val in list:
    if val in result:
      result[val] = result[val] + 1
    else:
      result[val] = 1
  return result


freq = frequency_table(list_b)

sum = 0

for val in list_a:
  if val in freq:
    sum += int(val) * freq[val]

print(sum)
