#!/usr/local/bin/python3
import itertools
import numpy


with open("./input.txt") as f:
    lines = [x.split(":") for x in f.read().splitlines()]

validcount = 0
for i in lines:
    charcount = i[1].count(i[0].split()[1])
    if charcount <= int(i[0].split()[0].split("-")[1]) and charcount >= int(i[0].split()[0].split("-")[0]):
        validcount += 1
print validcount

validcount = 0
for i in lines:
    a = i[1][int(i[0].split()[0].split("-")[0])] == i[0].split()[1]
    b = i[1][int(i[0].split()[0].split("-")[1])] == i[0].split()[1]
    if  a ^ b:
        validcount += 1
print validcount




