# Advent of Code 2019 - Day 3
# https://adventofcode.com/2019/day/3
# --- Day 3: Crossed Wires ---

# O(Lines in Wire #1 * Lines in Wire #2) = O(n^2)
# There is an O(n log n)-ish algorithm
# See Bentley-Ottmann Algorithm
# https://en.wikipedia.org/wiki/Bentley%E2%80%93Ottmann_algorithm

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({self.x},{self.y})'.format(self=self)

    def distance(self, b):
        return(abs(self.x - b.x) + abs(self.y - b.y))

class Line(object):
    def __init__(self, a, b, d):
        self.a = a
        self.b = b
        self.d = d

    def __str__(self):
        return '({self.a.x},{self.a.y})->({self.b.x},{self.b.y})'.format(self=self)

    def intersection(self, c):

        # Intersection with Point
        if isinstance(c, Point):
            if c.distance(self.a) + c.distance(self.b) == self.a.distance(self.b):
                return c
            else:
                return None

        #Intersection with Line
        elif isinstance(c, Line): 
            x1, y1, x2, y2 = self.a.x, self.a.y, self.b.x, self.b.y
            x3, y3, x4, y4 = c.a.x, c.a.y, c.b.x, c.b.y
            
            d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if d != 0:
                px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) // d
                py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) // d
                p = Point(px, py)
                if self.intersection(p) == c.intersection(p):
                    return self.intersection(p)
            else:
                # not handling overlapping lines unless I have to
                # okay... I didn't need to... 
                # result will be a line segment, but the point solution would be different based on the distance vs time method
                # for distance - want the point on the segment closest to (0,0) for distance
                # for time - want the point that minimizes pd_a + pd_b + d_a + d_b
                return (None)
            return (None)
        
        # Intersection with something else???
        else:
            return (None)


def ON2_Algorithm(lines):
    # O(n^2) algorithm
    bestdist = 2000000
    besttime = 2000000
    origin = Point(0,0)
    for i in range(0,len(lines[0])):
        for j in range(0,len(lines[1])):
            if i > 0 or j > 0:            
                p = lines[0][i].intersection(lines[1][j])
                if p != None:
                    dist = p.distance(origin)
                    time = lines[0][i].d + lines[0][i].a.distance(p) + lines[1][j].d + lines[1][j].a.distance(p)
                
                    bestdist = min(dist, bestdist)
                    besttime = min(time, besttime)
                    #print(lines[0][i], lines[1][j], p, dist, time)

    print (bestdist, besttime)

# Ugly Parsing as per usual   
f = open("./2019_03.txt")
lines = f.read().splitlines() 
f.close()
lines = [a.split(",") for a in lines]
for i in range(2):
    x, y, d = 0, 0, 0
    for j in range(len(lines[i])):
        px, py = x, y
        c,n = lines[i][j][:1], int(lines[i][j][1:])
        
        if c == "U":
            y += n
        elif c == "D":
            y -= n
        elif c == "L":
            x -= n
        elif c == "R":
            x += n
        lines[i][j] = Line(Point(px, py), Point(x, y), d)
        d += n

ON2_Algorithm(lines)