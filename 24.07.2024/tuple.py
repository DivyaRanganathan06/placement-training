#Given an integer, n, and n space-separated integers as input, create a tuple,i, of those  integers.
#Then compute and print the result of hash(t).
#Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
