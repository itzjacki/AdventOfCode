from itertools import chain

with open("09/input.txt", "r") as f:
  splitfile = f.read().split("\n")


def do_round(l):
  results = []

  def recursive_search(num_list):
    if all(n == 0 for n in num_list): 
      results.append(0)

    else:
      results.append(num_list[-1])
      new_list = []
      for i in range(len(num_list) - 1):
        new_list.append(num_list[i + 1] - num_list[i])
      recursive_search(new_list)
  
  recursive_search(l)
  return results


numbers = [[int(n) for n in l.split(" ")] for l in splitfile]

my_sum = 0

for n in numbers:
  result_list = do_round(n)
  my_sum += sum(result_list)

print(my_sum)