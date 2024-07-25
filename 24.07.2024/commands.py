#Consider a list (list = []). You can perform the following commands:
#1.	insert i e: Insert integer  at position .
#2.	print: Print the list.
#3.	remove e: Delete the first occurrence of integer .
#4.	append e: Insert integer  at the end of the list.
#5.	sort: Sort the list.
#6.	pop: Pop the last element from the list.
#7.	reverse: Reverse the list.
#Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.


if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        command, *rest = input().split()
        for i in range(len(rest)):
            rest[i] = int(rest[i])
        if command == "insert":
            list.insert(rest[0], rest[1])
        elif command == "print":
            print(list)
        elif command == "remove":
            list.remove(rest[0])
        elif command == "append":
            list.append(rest[0])
        elif command == "sort":
            list.sort()
        elif command == "pop":
            list.pop(-1)
        elif command == "reverse":
            list.reverse()
