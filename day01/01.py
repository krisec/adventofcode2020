def find_sum(x,y):
    if x + y == 2020:
        return x*y
    return False

def find_three_sum(x,y,z):
    if x + y + z == 2020:
        return x*y*z
    return False

inputs = open("./01input.txt", "r")

numbers = [int(input) for input in inputs]

print(numbers)



# This approach is horrible, don't do this!
# Good learning lesson, however. Wish I had time to do a more optimized version :)
for x in numbers:
    for y in numbers:
        for z in numbers:
            multiple = find_three_sum(x,y,z)
            if not multiple == False:
                print("Found:", x,y,z, " Gives: ", multiple)