with open("05/input.txt", "r") as f:
  splitfile = f.read().split("\n\n")

def do_step(input, output, start, range):
  if input >= start and input <= start + range: return input - start + output
  else: return None


seeds = [int(seed) for seed in splitfile[0][7:].split(" ")]
unprocessed_steps = [group.split("\n") for group in splitfile[1:]]

steps = []

for unprocessed_step in unprocessed_steps:
  step = [{"output": int(line.split(" ")[0]), "start": int(line.split(" ")[1]), "range": int(line.split(" ")[2])} for line in unprocessed_step[1:]]
  steps.append(step)

locations = []

for seed in seeds:
  value = seed
  for step in steps:
    old_result = value
    for f in step:
      result = do_step(value, f["output"], f["start"], f["range"])
      if result is not None:
        value = result
        break
  locations.append(value)

print(min(locations))
