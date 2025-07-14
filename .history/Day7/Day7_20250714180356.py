with open('Contents.txt','r') as file:
    Content = file.read()
    Content = Content.split('\n')

Example = """light red bags contain 1 bright white bag, 2 muted yellow bags.


lines = Example.split('\n')
bag_content = {}

for bag in Content:
    bags, contents = bag.split('contain')
    bags = bags.replace('bags','').replace('bag','')
    bags = bags.strip()
    contents = contents.replace('bags','').replace('bag','').replace('.','')
    contents = contents.split(',')
    bag_content[bags] = contents


reversed_map = defaultdict(list)

# Now we reverse our Map for Outer Bag -> Inner Bag
for outer_bag, inner_bag in bag_content.items():
    if inner_bag[0] == 'no other':
        continue

    for item in inner_bag:
        item = item.strip()
        item = item.split(' ',1) 
        count, content = item
        reversed_map[content].append(outer_bag)
