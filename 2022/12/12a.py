with open("12/input.txt", "r") as file:
  f = file.read().splitlines()
  
def num_value (letter):
  if letter == "S":
    return ord("a")
  if letter == "E":
    return ord("z")
  return ord(letter)

def find_first_letter (letter):
  for i in range(len(f)):
    for j in range(len(f[i])):
      if f[i][j] == letter:
        return (i, j)

start_pos = find_first_letter("S")
end_pos = find_first_letter("E")

# returns manhattan distance unless needed squares to get to "z"-value is higher than manhattan distance
# in which case, returns minimum needed squares to reach value of "z"
def find_modified_manhattan_distance(pos):
  global start_pos
  global end_pos
  distance_from_end = abs(pos[0] - end_pos[0]) + abs(pos[1] - end_pos[1])
  # return max(distance_from_end, num_value("E") - num_value(f[pos[0]][pos[1]]))
  return distance_from_end

def can_move_to(prev_pos, current_pos, next_pos):
  if next_pos == prev_pos:
    return False
  if not (0 <= next_pos[0] < len(f) and 0 <= next_pos[1] < len(f[0])):
    return False
  if num_value(f[next_pos[0]][next_pos[1]]) - num_value(f[current_pos[0]][current_pos[1]]) > 1:
    return False
  return True

def get_valid_neighbors(prev_pos, current_pos):
  potential_neighbors = [(current_pos[0], current_pos[1] + 1), (current_pos[0] + 1, current_pos[1]), (current_pos[0] - 1, current_pos[1]), (current_pos[0], current_pos[1] - 1)]
  return [pos for pos in potential_neighbors if can_move_to(prev_pos, current_pos, pos)]

def find_path_back(node, path_length=0):
  if node.parent:
    find_path_back(node.parent, path_length+1)
  else:
    print("path length:", path_length)

class Node():
  def __init__(self, parent, position):
    self.parent = parent
    self.position = position

    self.g = 0
    self.h = 0
    self.f = 0

  def __eq__(self, other):
    return self.position == other.position
  
  def __lt__(self, other):
    return self.f < other.f
      

open_list = []
closed_list = []

start_node = Node(None, start_pos)
end_node = Node(None, end_pos)

open_list.append(start_node)

while open_list:
  current_node = min(open_list)
  open_list.remove(current_node)
  closed_list.append(current_node)

  if current_node == end_node:
    find_path_back(current_node)
    break

  children = []
  if current_node.parent:
    for pos in get_valid_neighbors(current_node.parent.position, current_node.position):
      children.append(Node(current_node, pos))
  else:
    for pos in get_valid_neighbors(None, current_node.position):
      children.append(Node(current_node, pos))
  
  for child in children:
    if child.position not in [closed_node.position for closed_node in closed_list]:
    
      child.g = current_node.g + 1
      child.h = find_modified_manhattan_distance(child.position)
      child.f = child.g + child.h

      add_to_open = True
      for open_node in open_list:
        if child.position == open_node.position and child.g >= open_node.g:
          add_to_open = False
      if add_to_open:
        open_list.append(child)
  # print("open list:", len(open_list), "| closed list:", len(closed_list), "| distance to goal:", current_node.h, "| unique positions in closed list", len(set([node.position for node in closed_list])), end="\r")
