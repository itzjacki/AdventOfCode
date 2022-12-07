from collections import defaultdict

f = open("07/input.txt", "r").read().splitlines()

path = ""
directory = defaultdict(int)

def up(path):
  return path[:path.rfind("/")]

for c in f:
  # is command
  if c[0] == "$":
    # is cd command
    if c[2] == "c":
      if c == "$ cd ..":
        # update directory above
        directory[up(path)] += directory[path]
        path = up(path)
      elif c != "$ cd /":
        if path == "" or path[-1] != "/":
          path += "/"
        path += c[5:]
  # is directory
  elif c[0] == "d":
    pass
  # is file
  else:
    file_size = int(c.split(" ")[0])
    directory[path] += file_size

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