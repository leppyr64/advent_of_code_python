import hashlib


# f = open("./2015/2015_03.txt")
# inp = f.read().splitlines()[0]
# f.close()

def getresult(inp, match):
    for i in range(100000000):
        x = inp + str(i)
        y = hashlib.md5(x.encode()) .hexdigest()
        if y[:len(match)] == match:
            return i

# print(getresult('abcdef'))
# print(getresult('pqrstuv'))
print(getresult('yzbqklnj', '00000'))
print(getresult('yzbqklnj', '000000'))