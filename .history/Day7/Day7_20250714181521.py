from collections import defaultdict

with open('Contents.txt','r') as file:
    Sentences = file.read()
    Sentences = Sentences.split('\n')
    
bag_dict = defaultdict(set)

# Outer Map
for i in Sentences:
    bag, content = i.split(" contain ")
    bag = bag.rsplit(" ", 1)[0]
    bag_dict[bag] = content 


# Reverse Map
can_contain = defaultdict(set)
bag_contents = defaultdict(list)

for outer, inner in bag_dict.items():
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


def dfs(node, visited, graph):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]: 
        dfs(neighbor, visited, graph)

        
visited = set()
dfs("shiny gold", visited, can_contain)

visited.remove("shiny gold")
print(len(visited))