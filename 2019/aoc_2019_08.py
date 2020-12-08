

f = open("./2019/2019_08.txt")
inp = f.read().strip()
f.close()


layer_width = 25
layer_tall = 6
layer_total = layer_width * layer_tall

chunks, chunk_size = len(inp) // layer_total, layer_total

inp = [ inp[i:i+chunk_size] for i in range(0, len(inp), chunk_size) ]

least_zeroes = None
least_zeroes_string = ""
for a in inp:
    x = a.count("0")
    #print (x, a)
    if least_zeroes == None or x < least_zeroes:
        least_zeroes = x
        least_zeroes_string = a
        
a = least_zeroes_string.count("1")
b = least_zeroes_string.count("2")

print (least_zeroes, a, b, a * b)

s = ""
for x in range(layer_total):
    s += "2"

for a in inp:
    for x in range(layer_total):
        if s[x] == "2" and a[x] != "2":
            print(x, s)
            s = s[:x] + a[x] + s[x+1:]
            print(x, s)

print(s)

