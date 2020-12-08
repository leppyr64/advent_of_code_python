
from collections import deque
# 412 players; last marble is worth 71646 points

marbles = deque([1,0,2])
scores = [0 for i in range(412)]

players = 412
maxmarble = 7164600
cur_plr = 2

for cur_mbl in range(3,maxmarble+1):
    if cur_mbl % 23 == 0:
        #score
        marbles.rotate(7)
        #print ("SCORE?", marbles)
        score = cur_mbl + marbles.pop()
        scores[cur_plr % players] += score
        
        marbles.rotate(-1)
        #print("READY?", marbles)
    else:
        #place
        marbles.rotate(-1)
        marbles.append(cur_mbl)
    #print (marbles)
    cur_plr += 1


print (sorted(scores[:players]))


    

