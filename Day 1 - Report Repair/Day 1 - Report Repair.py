#!/usr/local/bin/python3
import itertools
import numpy


with open("./input.txt") as f:
    lines = [int(x) for x in f.readlines()]

for p in itertools.product(lines, lines):
    if sum(p) == 2020:
        print numpy.prod(p)
        break

for p in itertools.product(lines, lines, lines):
    if sum(p) == 2020:
        print numpy.prod(p)
        break

