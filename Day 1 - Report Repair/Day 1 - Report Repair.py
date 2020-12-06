#!/usr/local/bin/python3
import itertools
import numpy


with open("./input.txt") as f:
    INPUT = f.readlines()

lines = [int(x) for x in INPUT]


for r in itertools.product(lines, lines):
    if sum(r) == 2020:
        print numpy.prod(r)
        break

lines = [int(x) for x in INPUT]
for r in itertools.product(lines, lines, lines):
    if sum(r) == 2020:
        print numpy.prod(r)
        break

