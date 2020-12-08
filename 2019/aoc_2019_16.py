
f = open("./2019/2019_16.txt")
inp = f.read().splitlines()[0]
f.close()

N = len(inp)

mul = []
z = [0, 1, 0, -1]

for n in range(N):
    mul.append([])
    x = N // ((n + 1) * 4) + 1
    
    for i in range(x):
        for j in range(4):
            for k in range(n + 1):
                mul[n].append(z[j])
    
    mul[n] = mul[n][1:N + 1]
    if n < 20:
        print(mul[n][:20])

for p in range(100):
    d = [int(a) for a in inp]
    inp = ''
    for i in range(N):
        res = 0
        for j in range(N):
            res += d[j] * mul[i][j]
            # print (d[j] , mul[i][j])
        # print('r', res, res % 10)
        inp += str(abs(res) % 10)
    print (inp[:8])


print (np.fft.fft(inp))