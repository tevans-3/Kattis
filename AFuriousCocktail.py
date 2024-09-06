N,T = map(int, input().split())

times = []
vals = [] 

for i in range(N):
    t = int(input())
    times.append(t) 

times.sort()
times.reverse()

if times[0] - T*(len(times)-1) > 0: 
    print("YES")
else:
    print("NO")
