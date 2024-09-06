import math, sys
n = []

def multinomial(astring):
    counts = [math.factorial(astring.count(i)) for i in set(astring)]
    x = 1
    for i in counts:
        x *= i  
    return math.factorial(len(astring))//x

n = []
for line in sys.stdin:
    n.append(line.rstrip())

for l in n:
    print(multinomial(l))
