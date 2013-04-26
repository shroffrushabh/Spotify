#!/bin/usr/python

def decToBin(x):
    return int(bin(x)[2:])

def binReverse():
        number = int(raw_input())
        binNum = decToBin(number)
        print int(str(binNum)[::-1],2)

if __name__ == "__main__":
        binReverse()

