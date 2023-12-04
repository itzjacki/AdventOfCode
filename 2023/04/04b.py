with open("04/input.txt", "r") as f:
  splitfile = f.read().split("\n")

cards = {}

def make_list(string):
  return [n for n in string.split(" ") if n != ""]

def number_of_winnings(line):
  numbers = line.split(":")[1]
  winning = make_list(numbers.split("|")[0])
  have = make_list(numbers.split("|")[1])
  score = 0

  for n in have:
    if n in winning:
      score += 1

  return score

def get_card_number(line):
  return int(line.split(":")[0].split(" ")[-1])

for line in splitfile:
  card_number = get_card_number(line)
  cards[card_number] = (number_of_winnings(line), 1)

for (card, (winnings, amount)) in cards.items():
  for i in range(winnings):
    cards[card + i + 1] = (cards[card + i + 1][0], cards[card + i + 1][1] + amount)

total_card_number = 0
for (card, (winnings, amount)) in cards.items():
  total_card_number += amount
print(total_card_number)