with open("04/input.txt", "r") as f:
  splitfile = f.read().split("\n")

score = 0

def make_list(string):
  return [n for n in string.split(" ") if n != ""]

for line in splitfile:
  card_score = 0

  numbers = line.split(":")[1]
  winning = make_list(numbers.split("|")[0])
  have = make_list(numbers.split("|")[1])

  for n in have:
    if n in winning:
      if card_score == 0:
        card_score = 1
      else:
        card_score *= 2

  score += card_score

print(score)