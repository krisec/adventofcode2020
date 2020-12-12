import collections

def mark_group(group):
    answered_questions = []
    for person in group:
        for c in person:
            if not c in answered_questions and c != "\n":
                answered_questions.append(c)
    return len(answered_questions)

def mark_group_where_all_yes(group):
    group_answers = {}
    
    for person in group:
        for c in person:
            if c != "\n":
                if c in group_answers.keys():
                    group_answers[c] += 1
                else:
                    group_answers[c] = 1
    return [1 if group_answers[count]==len(group) else 0 for count in group_answers]



def get_input(path="input.txt"):
    file = open(path, "r")
    groups = []
    group = []
    for line in file:
        if line == "\n":
            groups.append(group)
            group = []
        else:
            group.append(line)

    return groups

groups = get_input()
#marked_question = [mark_group(group) for group in groups]

#print("Task 1: ", sum(marked_question))

marked_questions = [mark_group_where_all_yes(group) for group in groups]

print("Task 2: ", sum([sum(group) for group in marked_questions]))
