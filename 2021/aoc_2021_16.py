# Advent of Code 2021 - Day 16
# https://adventofcode.com/2021/day/16

filename = './2021/input/16.txt'
#filename = './2021/input/16_sample.txt'
f = open(filename)
lines = f.read().splitlines()
f.close()

def process_packet(packet): #result, leftover, returnvalue
    if len(packet) < 6:
        return (0, '')
    version = int(packet[:3],base=2)
    type = int(packet[3:6],base=2)
#    print('   Enter Packet', version, type, packet)
    packet = packet[6:]

    totalversion = version    
    returnvalue = 0
    if type == 4: # literal value
        chklast = 1
        litvalue = 0
        while chklast == 1:
            chklast = int(packet[0])
            litvalue = litvalue * 16 + int(packet[1:5],base=2)
            packet = packet[5:]
        returnvalue = litvalue
#        print('litvalue', litvalue)
    else:
        values = []
        lengthtypeid = int(packet[0])
#        print('   LeghthTypeID', lengthtypeid)
        packet = packet[1:]
        if lengthtypeid == 0:
            length = int(packet[:15], base=2)
#            print('   Leghth', length)
            packet = packet[15:]
            subpacket = packet[:length]
            packet = packet[length:]
            while len(subpacket) > 0:
                result, subpacket, value = process_packet(subpacket)
                values.append(value)
                totalversion += result
        else:
            length = int(packet[:11], base=2)
#            print('   Leghth', length)
            packet = packet[11:]
            for i in range(length):
                result, packet, value = process_packet(packet)
                values.append(value)
                totalversion += result

        #print(type, values)
        if type == 0:
            for v in values:
                returnvalue += v
        elif type == 1:
            returnvalue = 1
            for v in values:
                returnvalue *= v
        elif type == 2:
            returnvalue = sorted(values)[0]
        elif type == 3:
            returnvalue = sorted(values, reverse=True)[0]
        elif type == 5:
            if values[0] > values[1]:
                returnvalue = 1
            else:
                returnvalue = 0
        elif type == 6:
            if values[0] < values[1]:
                returnvalue = 1
            else:
                returnvalue = 0
        elif type == 7:
            if values[0] == values[1]:
                returnvalue = 1
            else:
                returnvalue = 0
        else:
            assert(False)

 #   print('Return', version, type, packet, totalversion)     
    return totalversion, packet, returnvalue


for l in lines:
    buffer = ''.join([bin(int(c, base=16))[2:].zfill(4) for c in l])
#    print(l)
#    print(buffer)
    print(process_packet(buffer))
