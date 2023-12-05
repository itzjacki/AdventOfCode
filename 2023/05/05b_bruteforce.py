with open("05/input.txt", "r") as f:
  splitfile = f.read().split("\n\n")

def do_step(input, output, start, range):
  if input >= start and input <= start + range: return input - start + output
  else: return None

seed_array = splitfile[0][7:].split(" ")
seeds = [(int(seed_array[i * 2]), int(seed_array[i * 2 + 1])) for i in range(int(len(seed_array)/2))]
unprocessed_steps = [group.split("\n") for group in splitfile[1:]]

seeds_processed = 0
total_seeds = sum([seed_tuple[1] for seed_tuple in seeds])

steps = []

for unprocessed_step in unprocessed_steps:
  step = [{"output": int(line.split(" ")[0]), "start": int(line.split(" ")[1]), "range": int(line.split(" ")[2])} for line in unprocessed_step[1:]]
  steps.append(step)

smallest_location = float('inf')

for seed_tuple in seeds:
  for seed in range(seed_tuple[0], seed_tuple[0] + seed_tuple[1]):
    value = seed
    for step in steps:
      old_result = value
      for f in step:
        result = do_step(value, f["output"], f["start"], f["range"])
        if result is not None:
          value = result
          break
    if value < smallest_location:
      smallest_location = value
    seeds_processed += 1
    print("Seeds processed: " + str(seeds_processed) + ", Seeds total: " + str(total_seeds) + ", Smallest so far: " + str(smallest_location), end='\r\r\r')
