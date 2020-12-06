#!/usr/local/bin/python3
import itertools
import numpy


with open("./input.txt") as f:
    lines = [x for x in f.read().splitlines()]
fieldwidth = len(lines[0])
fieldheight = len(lines)

trees = 0
v=0
h=0
while v < fieldheight:
    loc=[v,h]
    if lines[loc[0]][loc[1] % fieldwidth] == "#":
        trees += 1
    v += 1
    h += 3
print trees



#!/usr/local/bin/python3


with open("./input.txt") as f:
    lines = [x for x in f.read().splitlines()]
fieldwidth = len(lines[0])
fieldheight = len(lines)


steps = [[1,1], [3,1], [5,1], [7,1], [1,2]]
sumtrees = 1
for step in steps:
    trees = 0
    v=0
    h=0
    while v < fieldheight:
        loc=[v,h]
        if lines[loc[0]][loc[1] % fieldwidth] == "#":
            trees += 1
        v += step[1]
        h += step[0]
    sumtrees = sumtrees * trees
print sumtrees