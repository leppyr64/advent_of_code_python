


f = open("./2019_06.txt")
inp = f.read().splitlines()
f.close()

planets = dict()

def set_depth(p):
    sum = 0
    for c in planets[p]["children"]:
        planets[c]["depth"] = planets[p]["depth"] + 1
        sum += set_depth(c)
        
    return planets[p]["depth"] + sum

def path_to_root(p):
    if p == None:
            return []
    return [p] + path_to_root(planets[p]["parent"])



for s in inp:
    a, b = s.split(")")
    #print (s, a, b)
    if a not in planets.keys():
        planets[a] = {"parent": None, "children": [], "depth": 0}
    if b not in planets.keys():
        planets[b] = {"parent": None, "children": [], "depth": 0}
    
    assert planets[b]["parent"] == None

    planets[b]["parent"] = a
    planets[a]["children"].append(b)

for p in planets:
    if planets[p]["parent"] == None:
        print(set_depth(p))

a = path_to_root(planets["YOU"]["parent"])
b = path_to_root(planets["SAN"]["parent"])

i = len(a) - 1
j = len(b) - 1
while i >= 0 and j >= 0 and a[i] == b[j]:
    i -= 1
    j -= 1

print (i + j + 2)