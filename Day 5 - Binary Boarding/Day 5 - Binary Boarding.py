#!/usr/local/bin/python3

def read_input_moves(filename):
    with open("./input.txt") as f:
        INPUT = [[x[0:7],x[7:10]] for x in f.read().splitlines()]
    for bpass in INPUT:
        row = 0
        multiplier = 64
        for i in bpass[0]:
            if i == "B": row += multiplier
            multiplier = multiplier / 2
        column = 0
        multiplier = 4
        for i in bpass[1]:
            if i == "R": column += multiplier
            multiplier = multiplier / 2
        bpasses.append((row, column))


if __name__ == '__main__':


    bpasses = []
    read_input_moves('./input')
    highestBP = 0
    for i in bpasses:
        if i[0]*8+i[1] > highestBP:
            highestBP = i[0]*8+i[1]
    print highestBP

    allSeats = []
    for i in range (0, highestBP+1):
        allSeats.append(i)

    for i in bpasses:
        if i[0]*8+i[1] in allSeats:
            allSeats.remove(i[0]*8+i[1])

    print allSeats




