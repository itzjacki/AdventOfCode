from numpy import prod
with open("11/input.txt", "r") as file:
  f = [block.splitlines() for block in file.read().split("\n\n")]


# monke parse
parsed_monkeys = []
for monkey_info in f:
  monkey = {
    "number": int(monkey_info[0][7:-1]),
    "items": [int(item) for item in monkey_info[1][18:].split(", ")],
    "operation": (monkey_info[2][23], monkey_info[2][25:]),
    "test_divisor": int(monkey_info[3][21:]),
    "true_throw_to": int(monkey_info[4][29:]),
    "false_throw_to": int(monkey_info[5][30:]),
    "times_inspected": 0
  }
  parsed_monkeys.append(monkey)

divisors = [monkey["test_divisor"] for monkey in parsed_monkeys]
divisor_prod = prod(divisors)

def do_operation(item, operation):
  operand = item
  if operation[1].isnumeric():
    operand = int(operation[1])
  if operation[0] == "*":
    return item * operand % divisor_prod
  return item + operand

def process_monkey(monkey, monkeys):
  for item in monkey["items"]:
    monkey["times_inspected"] += 1
    new_item = do_operation(item, monkey["operation"])
    if new_item % monkey["test_divisor"] == 0:
      monkeys[monkey["true_throw_to"]]["items"].append(new_item)
    else:
      monkeys[monkey["false_throw_to"]]["items"].append(new_item)
  monkey["items"] = []

def do_round(monkeys):
  for monkey in monkeys:
    process_monkey(monkey, monkeys)

def print_monkey_status(monkeys):
  for monkey in monkeys:
    print("Monkey", monkey["number"], "items:", monkey["items"])

for i in range(10000):
  do_round(parsed_monkeys)
  # if i in [0, 19, 999, 1999, 2999, 3999, 4999, 5999, 6999, 7999, 8999, 9999]:
  #   print("== Round", i + 1, "==")
  #   print([monkey["times_inspected"] for monkey in parsed_monkeys])

times_list = [monkey["times_inspected"] for monkey in parsed_monkeys]
times_list.sort()
print(times_list[-1] * times_list[-2])