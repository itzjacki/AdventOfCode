import functools

with open("05/input.txt", "r") as f:
  splitfile = f.read().split("\n\n")

restrictions = splitfile[0].split("\n")
updates = [line.split(",") for line in splitfile[1].split("\n")]


def restriction_exists(page1, page2):
  return (page1 + "|" + page2) in restrictions


def compare(page1, page2):
  return -1 if restriction_exists(page1, page2) else 1 if restriction_exists(page2, page1) else 0


def sort_pages(update):
  return sorted(update, key=functools.cmp_to_key(compare))


def sum_updates(updates):
  return sum([int(pages[len(pages) // 2]) for pages in updates])


print(sum_updates(filter(lambda u: u == sort_pages(u), updates)))
