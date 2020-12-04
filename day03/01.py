def getInput(path):
    return [line.strip() for line in open(path, "r")]

def traverse(map, x, y, right=3, down=1):
    new_x = x + right
    new_y = y + down
    if new_x >= len(map[0]):
        new_x = new_x - len(map[0])
    if new_y >= len(map):
        return ["success", 0, 0]
    #print(new_x, new_y)
    return [new_x, new_y, map[new_y][new_x]]

input = getInput("input.txt")

def traverseSlope(right, down):
    trees = 0
    x = 0
    y = 0

    while x != "success":
        x,y,c = traverse(input, x, y, right, down)
        if x == "success":
            print(trees)
        if c == "#":
            trees+=1
    return trees

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]
product = 1
for r, d in slopes:
    product *= traverseSlope(r, d)

print(product)