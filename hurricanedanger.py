import math

INF = 10**9
EPS = 1e-9

class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    def __eq__(self, other):
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

def dist(p1, p2):
    return math.hypot(p1.x-p2.x, p1.y-p2.y)

class vec:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
def toVec(a, b):
    return vec(b.x-a.x, b.y-a.y)
def scale(v, s):
    return vec(v.x*s, v.y*s)
def translate(p, v):
    return point(p.x+v.x, p.y+v.y)
def dot(a,b):
    return a.x*b.x + a.y*b.y
def norm_sq(v):
    return v.x*v.x + v.y*v.y
def distToLine(p, a, b, c):
    ap = toVec(a, p)
    ab = toVec(a, b)
    u = dot(ap, ab) / norm_sq(ab)
    s = scale(ab, u)
    c.x, c.y = a.x+s.x, a.y+s.y
    return dist(p, c)
    
def main():
    n = int(input())
    for _ in range(n):
        x1,y1,x2,y2 = map(int, input().split())

        a = point(x1, y1)
        b = point(x2, y2)
        c = point()
        cities = int(input())

        mini = INF
        pls = []
        dss = []
        for city in range(cities):
            city_data = input().split()
            name = city_data[0]
            x = int(city_data[1])
            y = int(city_data[2])
            p = point(x, y)
            dist = distToLine(p, a, b, c)
            pls.append(name)
            dss.append(dist)
            if dist <= mini-EPS:
                mini = dist
        out = []
        for i in range(len(dss)):
            if abs(dss[i] - mini) < EPS:
                out.append(pls[i])
        print(*out)

if __name__=="__main__":
    main()
