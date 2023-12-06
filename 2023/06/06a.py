with open("06/input.txt", "r") as f:
  splitfile = f.read().split("\n")

time_list = [int(v) for v in splitfile[0].split(" ") if v.isdigit()]
distance_list = [int(v) for v in splitfile[1].split(" ") if v.isdigit()]

races = [{"time": time_list[i], "distance": distance_list[i]} for i in range(len(time_list))]

product = 1

for race in races:
  number_of_wins = 0
  for t in range(race["time"] + 1):
    speed = t
    distance = speed * (race["time"] - t)
    if distance > race["distance"]:
      number_of_wins += 1
  product *= number_of_wins

print(product)