from collections import defaultdict
with open('Contents.txt', 'r') as file:
    Content = file.read()
    Content = Content.split('\n')


bag_content = {}

for bag in Content:
    bags, contents = bag.split('contain')
    bags = bags.replace('bags', '').replace('bag', '')
    bags = bags.strip()
    contents = contents.replace('bags', '').replace('bag', '').replace('.', '')
    contents = contents.split(',')
    bag_content[bags] = contents


reversed_map = defaultdict(list)

# Now we reverse our Map for Outer Bag -> Inner Bag
for outer_bag, inner_bag in bag_content.items():
    if inner_bag[0] == 'no other':
        continue

    for item in inner_bag:
        item = item.strip()
        item = item.split(' ', 1)
        count, content = item
        reversed_map[content].append(outer_bag)


def dfs(node, visited, graph):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]: 
        dfs(neighbor, visited, graph)


visited = set()
dfs("shiny gold", visited, reversed_map)
visited.remove("shiny gold")
print(len(visited))

# Part 2
bag_contents = defaultdict(list)

for outer, inner in bag_content.items():
    inner_bags = inner.split(", ")

    for inner_bag in inner_bags:
        words = inner_bag.strip().split(" ", 1)
        if words[0] == "no":
            continue
        count, inner_bag_name = words
        count = int(count)
        inner_bag_name = inner_bag_name.rsplit(" ", 1)[0]
        can_contain[inner_bag_name].add(outer)
        bag_contents[outer].append((count, inner_bag_name))


def count_total_bags(bag):
    total = 0
    for count, inner_bag in bag_contents.get(bag, []):
        total += count + count * count_total_bags(inner_bag)
    return total


print(count_total_bags("shiny gold"))
