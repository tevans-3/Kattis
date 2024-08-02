import random, sys

for _ in range(1000):
    gss = {'A','B','C'}
    first = random.choice('ABC')
    gss.remove(first)
    print(first)
    sys.stdout.flush()
    nxt_ln = input().split()
    door = nxt_ln[0]
    num = int(nxt_ln[1])
    if num: 
        print(door)
        sys.stdout.flush()
    else:
        gss.remove(door)
        print(gss.pop())
        sys.stdout.flush()
    n = input()
