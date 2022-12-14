from functools import cmp_to_key

with open("13/input.txt", "r") as file:
  lines = [eval(line) for line in file.read().splitlines() if line] + [[[2]]] + [[[6]]]

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

def compare(item1, item2):
  correct_order = eval_elements(item1, item2)
  if correct_order == None:
    return 0
  if correct_order == True:
    return -1
  if correct_order == False:
    return 1

lines.sort(key=cmp_to_key(compare))

print((lines.index([[2]]) + 1) * (lines.index([[6]]) + 1))