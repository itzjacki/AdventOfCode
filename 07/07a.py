f = open("07/input.txt", "r").read().splitlines()

path = ""
directory = {}

# adds size to path in dict, creates new dict entry if needed
def add_to_path(path, size):
  if path not in directory:
      directory.update({path: 0})
  directory.update({path: directory[path] + size})

def up(path):
  return path[:path.rfind("/")]

for c in f:
  # is command
  if c[0] == "$":
    # is cd command
    if c[2] == "c":
      if c == "$ cd ..":
        # update directory above
        add_to_path(up(path), directory[path])
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
    add_to_path(path, file_size)

# return to root path, update backwards along the way
while path != "":
  temp_path = path
  while temp_path != "":
    add_to_path(up(temp_path), directory[temp_path])
    temp_path = up(temp_path)
  path = up(path)

sum = sum(dir for dir in directory.values() if dir <= 100_000)

print(sum)