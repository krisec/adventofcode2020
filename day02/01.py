def get_inputs(path):
    inputFile = open(path, "r")
    inputs = []
    for line in inputFile:
        first_split = line.split("-")
        second_split = first_split[1].split(" ")
        i = [int(first_split[0]), int(second_split[0]), second_split[1][0], second_split[2]]
        inputs.append(i)
    return inputs

def check_password_task_1(password):
    minOccurences = password[0]
    maxOccurences = password[1]
    targetChar = password[2]
    occurences = 0
    for c in password[3]:
        if c == targetChar:
            occurences +=1
    if occurences < minOccurences or occurences > maxOccurences:
        return False
    else: return True


def check_password_task_2(password):
    first_pos = password[0]
    second_pos = password[1]
    targetChar = password[2]
    word = password[3]
    if word[first_pos-1] == targetChar or word[second_pos-1] == targetChar:
        return word[first_pos-1] != word[second_pos-1]
    else: return False

inputs = get_inputs("input.txt")
#print(inputs)

correctPasswords = 0
for password in inputs:
    if check_password_task_2(password):
        correctPasswords += 1

print(correctPasswords)