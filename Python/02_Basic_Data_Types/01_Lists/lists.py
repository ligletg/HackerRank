
def makeList():
    N = int(raw_input())
    theList = []
    for i in range(0, N):
        input = raw_input().split(" ")
        command = input[0]
        if command == "insert":
            theList.insert(int(input[1]), int(input[2]))
        elif command == "remove":
            theList.remove(int(input[1]))
        elif command == "append":
            theList.append(int(input[1]))
        elif command == "print":
            print(theList)
        elif command == "sort":
            theList.sort()
        elif command == "pop":
            theList.pop()
        elif command == "reverse":
            theList.reverse()

if __name__ == '__main__':
    makeList()
