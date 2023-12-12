import functools


with open("12/input.txt", "r") as f:
  splitfile = f.read().split("\n")

rows_unprocessed = [(row.split(" ")[0], [int(n) for n in row.split(" ")[1].split(",")])
                    for row in splitfile]
rows = [(tuple("?".join([row[0]]*5)), tuple(row[1] * 5))
        for row in rows_unprocessed]


@functools.cache  # Why reinvent the cache?
def find_variations(s, n, must_be_dot=False, must_be_hashtag=False):

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

    return find_variations(s[1:], n)

  elif s[0] == "#":
    if must_be_dot:
      return 0

    if n[0] == 1:
      return find_variations(s[1:], n[1:], must_be_dot=True)

    elif n[0] > 1:
      return find_variations(s[1:], (n[0] - 1, *n[1:]), must_be_hashtag=True)

  elif s[0] == "?":
    if must_be_dot:
      return find_variations((".", *s[1:]), n)

    elif must_be_hashtag:
      return find_variations(("#", *s[1:]), n)

    else:
      return find_variations((".", *s[1:]), n) + find_variations(("#", *s[1:]), n)


total_variations = 0

for row_index, row in enumerate(rows):
  print("Progress", row_index + 1, "/", len(rows), end="\r")

  num_variations = find_variations(row[0], row[1])
  total_variations += num_variations

print("\n--------------------\nResult:", total_variations)
