def find_seat(boarding_pass):
    lower_bound = 1
    currentPartition = 128
    for c in boarding_pass[:7]: # First do front/back partitioning
        currentPartition /= 2
        if c == "B":
            lower_bound += currentPartition
    row = lower_bound
    lower_bound = 1
    currentPartition = 8
    for c in boarding_pass[7:]:
        currentPartition /= 2
        if c == "R":
            lower_bound += currentPartition
    col = lower_bound

    return row - 1, col - 1

def get_seat_id(row, col):
    return row * 8 + col

file = open("input.txt", "r")
maxID = -1
seatIDs = []
for boarding_pass in file:
    row, col = find_seat(boarding_pass.strip())
    seatId = get_seat_id(row, col)
    seatIDs.append(seatId)

seatIDs.sort()
for index, seatID in enumerate(seatIDs):
    if index > 0:
        if seatID - seatIDs[index-1] > 1:
            print(seatIDs[index-1])
