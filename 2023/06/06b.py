with open("06/input.txt", "r") as f:
  splitfile = f.read().split("\n")

# Mac M1 Pro go brrrrrrrrrrrrrrr
# Fuck the quadratic equation, all my homies hate the quadratic equation

time_list = [str(v) for v in splitfile[0].split(" ") if v.isdigit()]
distance_list = [str(v) for v in splitfile[1].split(" ") if v.isdigit()]
time_concatinated = "".join(time_list)
distance_concatinated = "".join(distance_list)

race = {"time": int(time_concatinated), "distance": int(distance_concatinated)}

product = 1

number_of_wins = 0
for t in range(race["time"] + 1):
  speed = t
  distance = speed * (race["time"] - t)
  if distance > race["distance"]:
    number_of_wins += 1
product *= number_of_wins

print(product)