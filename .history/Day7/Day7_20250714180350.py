with open('Contents.txt','r') as file:
    Content = file.read()
    Content = Content.split('\n')

Example = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags. """ 

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
