#!/usr/local/bin/python3

def read_input_moves(filename):
    with open("./input.txt") as f:
        INPUT = [x for x in f.read()]
    buffer = []
    for i in range(0, len(INPUT)):
        if INPUT[i] != "\n":
            buffer.append(INPUT[i])
        if (INPUT[i] == "\n" and INPUT[i+1] == "\n") or i+1 == len(INPUT):
            buffer = []
            groups.append(buffer)

def read_input_moves2(filename):
    with open("./input.txt") as f:
        INPUT = [x for x in f.read()]
        INPUT.append("\n")
        INPUT.append("\n")
#    print INPUT
    answers = []
    answergroup = []
    for i in range(0, len(INPUT)):
        if INPUT[i] != "\n":
            answers.append(INPUT[i])
        else:
            if len(answers)==0:
                allgroups.append(answergroup)
                answergroup = []
            else:
                answergroup.append(answers)
                answers = []






if __name__ == '__main__':
    groups = []
    read_input_moves('./input')
    sum = 0
    for i in groups:
        sum += len(set(i))
    print sum
    print("====")

    allgroups = []
    read_input_moves2('./input')
    sumk = 0
    for group in allgroups:
        answers = {}
        for person in group:
            for answer in person:
                if answer in answers:
                    answers[answer] += 1
                else:
                    answers[answer] = 1
        for k in answers.keys():
            if answers[k]==len(group):
                sumk+=1
    print sumk












