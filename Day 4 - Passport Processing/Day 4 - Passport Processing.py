#!/usr/local/bin/python3
import re

def makePassport(ppString):
    data = {}
    for i in ppString.split():
        data[i.split(":")[0]] = i.split(":")[1]
    passports.append(data)

def read_input_moves(filename):
    with open("./input.txt") as f:
        INPUT = [x for x in f.read()]
    buffer = []
    for i in range(0, len(INPUT)):
        if INPUT[i] != "\n":
            buffer.append(INPUT[i])
        else:
            buffer.append(" ")
        if (INPUT[i] == "\n" and INPUT[i+1] == "\n") or i+1 == len(INPUT):
            makePassport(''.join(buffer))
            buffer = []

def checkifVadid_star1(passport):
    valid = True
    if len(passport) < 8:
        valid = False
        if ("cid" not in passport.keys()) and (len(passport) == 7):
            valid = True
    return valid

def checkifVadid_star2(passport):
    if checkifVadid_star1(passport):
        if byr_valid(passport):
            if iyr_valid(passport):
                if eyr_valid(passport):
                    if hgt_valid(passport):
                        if hcl_valid(passport):
                            if ecl_valid(passport):
                                if pid_valid(passport):
                                    if cid_valid(passport):
                                        return True

def byr_valid(passport):
    if 1920 <= int(passport['byr']) <= 2002:
        return True
    return False

def iyr_valid(passport):
    if 2010 <= int(passport['iyr']) <= 2020:
        return True
    return False

def eyr_valid(passport):
    if 2020 <= int(passport['eyr']) <= 2030:
        return True
    return False

def hgt_valid(passport):
    m = re.search( r'([0-9]*)([a-z]*)', passport['hgt'])
    if m.group(2) == "cm":
        if 150 <= int(m.group(1)) <= 193:
            return True
    if m.group(2) == "in":
        if 59 <= int(m.group(1)) <= 76:
            return True
    return False

def hcl_valid(passport): #TODO
    valid = True
    if passport['hcl'][0] != "#":
        print passport['hcl']
        return False
    return True

def ecl_valid(passport):
    if  passport['ecl'] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return True
    return False

def pid_valid(passport):
    if len(passport['pid']) != 9:
        return False
    return True

def cid_valid(passport):  #IGNORE
    return True





if __name__ == '__main__':
    passports = []
    read_input_moves('./input')
    validpp = 0
    for i in passports:
        if checkifVadid_star1(i): validpp += 1
    print validpp
    validpp = 0
    for i in passports:
        if checkifVadid_star2(i): validpp += 1
    print validpp






