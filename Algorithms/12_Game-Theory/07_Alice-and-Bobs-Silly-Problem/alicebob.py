#!/bin/python

from __future__ import print_function

import os
import sys

def isPrime(n):
     if n <= 1:
        return False
     elif n <= 3:
        return True
     elif n % 2 == 0 or n % 3 == 0:
        return False
     i = 5
     while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
     return True

def getPrimes(n):
    count = 0
    primeSet = []
    while count <= n:
	if isPrime(count) == True:
	    primeSet.append(count)
    	count = count + 1
    return primeSet

def getPrimesLength(n, primeSet):
    count = 0
    for value in primeSet:
        if value > n:
            print(count)
            return count
        count = count + 1
    return count

def sillyGame(n, primeSet):
    primesLength = getPrimesLength(n, primeSet)
    if primesLength % 2 == 0:
	   return "Bob"
    else:
	   return "Alice"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    primeSet = getPrimes(100000)
    g = int(raw_input())
    for g_itr in xrange(g):
        n = int(raw_input())

        result = sillyGame(n, primeSet)

        # fptr.write(result + '\n')
        print(result + '\n')
    # fptr.close()



