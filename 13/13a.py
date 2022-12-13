import ast

with open("13/input.txt", "r") as file:
  pairs = [[ast.literal_eval(packet) for packet in pair.splitlines()] for pair in file.read().split("\n\n")]

# Checks if 1 or more elements are a certain type (list, int, etc)
def check_type (type, *elements):
  for e in elements:
    if not isinstance (e, type):
      return False
  return True

def eval_lists(e1, e2):
  for c1, c2 in zip(e1, e2):
    recursive_check = eval_elements(c1, c2)
    if recursive_check != None:
      return recursive_check
  if len(e1) < len(e2):
    return True
  if len(e1) > len(e2):
    return False

def eval_elements(e1, e2):
  # both are int
  if check_type(int, e1, e2):
    if e1 < e2:
      return True
    if e1 > e2:
      return False
  
  # both are list
  if check_type(list, e1, e2):
    list_comparison = eval_lists(e1, e2)
    if list_comparison != None:
      return list_comparison

  if check_type(list, e1) and check_type(int, e2):
    list_comparison = eval_lists(e1, [e2])
    if list_comparison != None:
      return list_comparison
  
  if check_type(int, e1) and check_type(list, e2):
    list_comparison = eval_lists([e1], e2)
    if list_comparison != None:
      return list_comparison

running_sum = 0
for index, pair in enumerate(pairs, start=1):
  is_correct = eval_elements(pair[0], pair[1])
  if is_correct:
    running_sum += index

print(running_sum)