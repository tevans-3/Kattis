T = int(input())

for _ in range(T):
    l = input()
    N = int(input())
    C = 0 
    for i in range(N):
        C += int(input())
    if C%N == 0:
        print('YES')
    else:
        print('NO')
