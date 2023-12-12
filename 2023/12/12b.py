with open("12/input.txt", "r") as f:
  splitfile = f.read().split("\n")

rows_unprocessed = [(row.split(" ")[0], [int(n) for n in row.split(" ")[1].split(",")])
                    for row in splitfile]
rows = [(list("?".join([row[0]]*5)), row[1] * 5) for row in rows_unprocessed]

total_variations = 0
cache = {}


def cache_result(value, cache_key):
  global cache
  cache[cache_key] = value
  return value


def find_variations(s, n, must_be_dot=False, must_be_hashtag=False, debug_use_cache=True):
  cache_key = ",".join(
      s) + ",".join([str(num) for num in n]) + str(must_be_dot) + str(must_be_hashtag)

  global cache
  if cache_key in cache and debug_use_cache:
    return cache[cache_key]

  # Early exit if branch has been processed to completion
  if len(s) == 0 and len(n) == 0:
    return 1

  elif len(s) > 0 and len(n) == 0:
    if "#" in s:
      return 0
    else:
      return 1

  elif len(s) == 0 and len(n) > 0:
    return 0

  # Processing of next character
  if s[0] == ".":
    if must_be_hashtag:
      return 0

    return cache_result(find_variations(s[1:], n), cache_key)

  elif s[0] == "#":
    if must_be_dot:
      return 0

    if n[0] == 1:
      return cache_result(find_variations(s[1:], n[1:], must_be_dot=True), cache_key)

    elif n[0] > 1:
      return cache_result(find_variations(s[1:], [n[0] - 1, *n[1:]], must_be_hashtag=True), cache_key)

  elif s[0] == "?":
    if must_be_dot:
      return cache_result(find_variations([".", *s[1:]], n), cache_key)

    elif must_be_hashtag:
      return cache_result(find_variations(["#", *s[1:]], n), cache_key)

    else:
      return cache_result(find_variations([".", *s[1:]], n) + find_variations(["#", *s[1:]], n), cache_key)


for row_index, row in enumerate(rows):
  print("Progress", row_index + 1, "/", len(rows), end="\r")

  num_variations = find_variations(row[0], row[1])
  total_variations += num_variations

print("\n--------------------\nResult:", total_variations)
