import re
import sys

# Version of 5b in the progress of being modified to support the processing of
# a very large version of the input file

f = open("05/secondary_input.txt", "r").read().splitlines()

# prep by finding size of crate array
crate_array=[]
crate_height=0
for line in f:
  if line[1] == "1":
    break
  crate_height += 1
for i in range(9):
  crate_array.append([])

# input crates
for i in range(crate_height - 1, -1, -1):
  for j in range(1, 34, 4):
    crate = f[i][j]
    if crate != " ":
      crate_array[int((j-1)/4)].append(crate)

# define move action
# in and out crates are 0 indexed
def move(n, out_crate, in_crate):
  crate_array[in_crate - 1].extend(crate_array[out_crate - 1][-(n):])
  del crate_array[out_crate - 1][-(n):]

# execute move actions
for i in range(crate_height + 2, len(f), 1):
  sys.stdout.write(f"\rProgress {i-crate_height}/{len(f)-crate_height}, {(i-crate_height)*100/(len(f)-crate_height):.4f}%" )
  result = re.search(r"move (\d+) from (\d+) to (\d+)", f[i])
  cap_num = [int(e) for e in result.groups()]
  move(*cap_num)

# print result
result_string = ""
for crate_stack in crate_array:
  result_string += crate_stack[-1]
print(result_string)