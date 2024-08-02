n = int(input())
pushes = [int(num) for num in input().split()]

hgst = pushes[len(pushes)-1]
dirtiness = 0 
cleanups = 1
for num in range(len(pushes)-2, -1, -1):
    dirtiness += hgst-pushes[num]
    #print(dirtiness, pushes[num], hgst)
    if dirtiness > 19:
         hgst = pushes[num]
         cleanups += 1
         dirtiness = 0
    #     for num in range(hgst, -1, -1)
print(cleanups)
