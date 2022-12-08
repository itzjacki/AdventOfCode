from collections import defaultdict

with open("07/input.txt", "r") as file:
  f = file.read().splitlines()

path = ""
directory = defaultdict(int)

def up(path):
  return path[:path.rfind("/")]

for c in f:
  # is file
  if c[0].isnumeric():
    file_size = int(c.split(" ")[0])
    directory[path] += file_size
  # is cd .. command
  elif c == "$ cd ..":
    # update directory above
    directory[up(path)] += directory[path]
    path = up(path)
  # is cd command, not to root
  elif c[2] == "c" and c != "$ cd /":
    if path == "" or path[-1] != "/":
      path += "/"
    path += c[5:]
  # ls commands and dir results are ignored

# return to root path, update backwards along the way
while path != "":
  temp_path = path
  while temp_path != "":
    directory[up(temp_path)] += directory[temp_path]
    temp_path = up(temp_path)
  path = up(path)

available_space = 70_000_000 - directory[""]
space_needed = 30_000_000 - available_space
smallest_dir = min(dir for dir in directory.values() if dir > space_needed)

print("need", space_needed, "deleting directory of size", smallest_dir)