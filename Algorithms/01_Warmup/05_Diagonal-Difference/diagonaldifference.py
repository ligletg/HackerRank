#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a, n):
    #
    # Write your code here.
    #
    diag1 = 0
    diag2 = 0
    j = n - 1
    for i in range(0, n):
        diag1 = diag1 + a[i][i]
        diag2 = diag2 + a[i][j]
        i = i + 1
        j = j - 1
    print(diag1)
    print(diag2)
    return abs(diag1 - diag2)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    a = []

    for _ in xrange(n):
        a.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(a, n)

    f.write(str(result) + '\n')

    f.close()

