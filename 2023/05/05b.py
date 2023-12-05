with open("05/input.txt", "r") as f:
  splitfile = f.read().split("\n\n")

def do_step(input, output, start, range):
  if input >= start and input <= start + range: return input - start + output
  else: return None


seed_array = splitfile[0][7:].split(" ")
seeds = [(int(seed_array[i * 2]), int(seed_array[i * 2 + 1])) for i in range(int(len(seed_array)/2))]

steps = []

def check_in_seeds(num):
  for seed_tuple in seeds:
    if seed_tuple[0] <= num <= seed_tuple[0] + seed_tuple[1]:
      return True
  return False

unprocessed_steps = [group.split("\n") for group in splitfile[1:]]
for unprocessed_step in unprocessed_steps:
  step = [{"start": int(line.split(" ")[0]), "output": int(line.split(" ")[1]), "range": int(line.split(" ")[2])} for line in unprocessed_step[1:]]
  steps.insert(0, step)

hit_location = None
n = 0

while(hit_location is None):
  value = n
  for step in steps:
    old_result = value
    for f in step:
      result = do_step(value, f["output"], f["start"], f["range"])
      if result is not None:
        value = result
        break
  if check_in_seeds(value):
    hit_location = n
  print(str(n), end="\r")
  n += 1

print("found hit: " + str(hit_location))