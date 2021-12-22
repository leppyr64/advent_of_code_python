# Advent of Code 2021 - Day 18
# https://adventofcode.com/2021/day/18

filename = './2021/input/18.txt'
#filename = './2021/input/18_sample.txt'
f = open(filename)
lines = f.read().splitlines()
f.close()

class node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.value = None

    def printnode(self):
        result = ''
        if self.value == None:
            result += '['
            result += self.left.printnode()
            result += ','
            result += self.right.printnode()
            result += ']'
        else:
            result = str(self.value)
        return result

    def magnitude(self):
        result = 0
        if self.value == None:
            result += 3 * self.left.magnitude()
            result += 2 * self.right.magnitude()
        else:
            result = self.value
        return result

    def split(self):
        if self.value == None:
            result = self.left.split()
            if result:
                return result
            return self.right.split()
        elif self.value >= 10:
            # split this node
            self.left = node()
            self.left.parent = self
            self.left.value = self.value // 2
            self.right = node()
            self.right.parent = self
            self.right.value = (self.value + 1) // 2
            self.value = None
            return True
        else:
            return False
    
    def is_right_subtree(self):
        if self.parent == None:
            return False
        return self.parent.right == self

    def is_left_subtree(self):
        if self.parent == None:
            return False
        return self.parent.left == self

    def explode(self, depth):
        if self.value == None and depth == 4:
            # add left value to left
            cur = self
            while cur.is_left_subtree():
                cur = cur.parent
            if not cur.parent == None:
                cur = cur.parent.left
                while cur.value == None:
                    cur = cur.right
                cur.value += self.left.value
                
            # add right value to right
            cur = self
            while cur.is_right_subtree():
                cur = cur.parent

            if not cur.parent == None:
                cur = cur.parent.right
                while cur.value == None:
                    cur = cur.left
                cur.value += self.right.value

            self.left = None
            self.right = None
            self.value = 0
            return True
        elif self.value == None:
            result = self.left.explode(depth + 1)
            if result:
                return result
            return self.right.explode(depth + 1)
        else:
            return False

class tree:
    def __init__(self, s):
        self.root = node()
        cur = self.root
        for c in s:    
            if c == '[':
                cur.left = node()
                cur.left.parent = cur
                cur = cur.left
            elif c == ']':
                cur = cur.parent
            elif c == ',':
                cur = cur.parent
                cur.right = node()
                cur.right.parent = cur
                cur = cur.right
            else:
                cur.value = int(c)

    def printtree(self):
        return self.root.printnode()

    def add(self, othertree):
        cur = node()
        cur.left = self.root
        cur.left.parent = cur
        cur.right = othertree.root
        cur.right.parent = cur
        self.root = cur

    def reduce(self):
        changed = True
        while changed:
            changed = self.root.explode(0)
            if changed == False:
                changed = self.root.split()

t = tree(lines[0])
for l in lines[1:]:
    x = tree(l)
    t.add(x)
    t.reduce()
    #print(t.printtree())
    #print(t.root.magnitude())
print('Part 1', t.root.magnitude())

best = 0
for x in range(len(lines)):
    for y in range(len(lines)):
        if x == y:
            continue
        ta = tree(lines[x])
        tb = tree(lines[y])
        ta.add(tb)
        ta.reduce()
        check = ta.root.magnitude()
        if check > best:
            best = check
print('Part 2', best)
