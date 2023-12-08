from collections import Counter

with open("07/input.txt", "r") as f:
  splitfile = f.read().split("\n")

hand_size = 5

def value_from_label(label):
  match label:
    case "A": return 14
    case "K": return 13
    case "Q": return 12
    case "J": return 1
    case "T": return 10
  return int(label)
  
def rank_from_type(hand):
  multiplier = 100 ** hand_size

  jokers = hand.count("J")

  hand_frequency = sorted(list(Counter(hand.replace("J", "")).values()), reverse=True)
  while len(hand_frequency) < 5: hand_frequency.append(0)

  if hand_frequency[0] + jokers == 5: return 7 * multiplier
  elif hand_frequency[0]  + jokers == 4: return 6 * multiplier
  elif hand_frequency[0] + jokers == 3 and hand_frequency[1] == 2: return 5 * multiplier
  elif hand_frequency[0] + jokers == 3: return 4 * multiplier
  elif hand_frequency[0] + jokers == 2 and hand_frequency[1] == 2: return 3 * multiplier
  elif hand_frequency[0] + jokers == 2: return 2 * multiplier
  else: return 1 * multiplier

def find_rank(hand):
  rank = rank_from_type(hand)
  for i, label in enumerate(hand):
    rank += (100 ** (hand_size - 1 - i)) * value_from_label(label)
  return rank

hands = [{"hand": l.split(" ")[0], "bet": l.split(" ")[1]} for l in splitfile]
for hand in hands:
  hand["rank"] = find_rank(hand["hand"])

sorted_hands = sorted(hands, key=lambda k: k["rank"])

winnings = 0

for i, sh in enumerate(sorted_hands):
  winnings += (i + 1) * int(sh["bet"])

print(winnings)