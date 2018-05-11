from __future__ import print_function

def printN(n):
    arr = []
    for i in range(1,n + 1):
        arr.append(i)
    print("".join(str(x) for x in arr))
if __name__ == '__main__':
    n = int(raw_input())
    printN(n)

