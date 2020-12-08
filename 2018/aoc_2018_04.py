


f = open("2018_04.txt")
txt = f.readlines()
txt.sort()

guard_asleep = -1
guard = 0
guardlog = {}

for s in txt:
    s = s.split("[")[1]
    dt,action = s.split("]")
    actions = action.split()
    #print(dt, actions[0])
    if actions[0]=="Guard":
        if(guard_asleep > -1):
            print("WTF?")
        guard = actions[1].split("#")[1]
        if guard not in guardlog:
            guardlog[guard] = [0]*60
        print("CHANGEGUARD", guard)
    elif actions[0] == "falls":
        guard_asleep = int(dt.split()[1].split(":")[1])
        print("ASLEEP", guard, guard_asleep)
    elif actions[0] == "wakes":
        guard_awake = int(dt.split()[1].split(":")[1])
        print ("AWAKE", guard, guard_asleep, guard_awake)
        for i in range(guard_asleep, guard_awake):
            guardlog[guard][i] += 1
        guard_asleep = -1

for g in guardlog:
    sleep = 0
    max_minute = 0
    for x in range(60):
        sleep += guardlog[g][x]
        if guardlog[g][x] > guardlog[g][max_minute]:
            max_minute = x
    print(g, sleep, max_minute, guardlog[g][max_minute])

