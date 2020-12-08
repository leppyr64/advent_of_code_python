nodes = [{"p":-1,"nc": 1, "nm": 0, "children":[], "meta":[1]}]

def nodevalue(idx):
    sum = 0
    if nodes[idx]["nc"] == 0:
        for a in nodes[idx]["meta"]:
            sum += a
    else:
        for a in nodes[idx]["meta"]:
            if a <= len(nodes[idx]["children"]):
                sum += nodevalue(nodes[idx]["children"][a-1])
    print(idx, sum)
    return (sum)


f = open("./2018_08.txt")
txt = f.readline().split()
txt = [int(a) for a in txt]
print (txt)
print (len(txt))


idx = 0
curnode = 0
sum_meta = 0

while idx < len(txt):
    if len(nodes[curnode]["children"]) < nodes[curnode]["nc"]:
        nodes.append({"p":curnode, "nc": txt[idx], "nm": txt[idx+1], "children":[], "meta":[]})
        nodes[curnode]["children"].append(len(nodes) - 1)
        idx += 2
        curnode = len(nodes) - 1
    else:
        for i in range(nodes[curnode]["nm"]):
            nodes[curnode]["meta"].append(txt[idx])
            sum_meta += txt[idx]
            idx += 1
        curnode = nodes[curnode]["p"]

for a in nodes:
    print (a)
print(sum_meta)

x = nodevalue(0)


