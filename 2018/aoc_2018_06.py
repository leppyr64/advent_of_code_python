class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({self.x},{self.y})'.format(self=self)

    def distance(self, b):
        return(abs(self.x - b.x) + abs(self.y - b.y))


f = open("./2018_06.txt")
lines = f.read().splitlines()
xs = []
ys = []
ps = []

for a in lines:
    xs.append(int(a.split(",")[0]))
    ys.append(int(a.split(",")[1]))
    ps.append(Point(int(a.split(",")[0]), int(a.split(",")[1])))

xs = sorted(xs)
ys = sorted(ys)

count = 0
for x in range(-160, 560):
    for y in range(-160, 560):
        sum = 0
        p = Point(x,y)
        for z in range(50):
            sum += p.distance(ps[z])
        if sum <= 10000:
            count += 1
print (count)
