
#f = open("./2020/input/2020_07_small.txt")
f = open("./2020/input/2020_07.txt")
inp = f.read().splitlines()
f.close()

allbags = {}
visited = {}

def part1(curbag):
    for k in allbags:
        if k not in visited and curbag in allbags[k]:
            visited[k] = 1
            part1(k)
    
def part2(curbag):
    if curbag in visited:
        return visited[curbag]

    result = 0
    for k in allbags[curbag]:
        result += allbags[curbag][k] * (1 + part2(k))
    visited[curbag] = result
    return result

# INPUT
for a in inp:
    b,c = a.split(' contain ')
    bag = b[:-5] # bag
    if bag not in allbags:
        allbags[bag] = {}


    c = c[:-1]
    d = c.split(', ')
    for i in range(len(d)):
        if d[i][-1] == 's':
            d[i] = d[i][:-5]
        else:
            d[i] = d[i][:-4]
        if d[i] == 'no other':
            d.pop(0)
        else:
            d[i] = [  d[i][:d[i].find(' ')], d[i][d[i].find(' ')+1:]]
    
    for n, bag2 in d:
        #print(bag, n, bag2)
        if bag2 not in allbags:
            allbags[bag2] = {}
        allbags[bag][bag2] = int(n)

#print(allbags)
#for k in allbags:
#    print(k, allbags[k])


part1('shiny gold')
print('part1', len(visited))


visited = {}
print('part2', part2('shiny gold'))