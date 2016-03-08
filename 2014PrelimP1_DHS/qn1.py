# Task 1.1

runfile = open("RACE.txt", 'r')
lines = runfile.readlines()
arrayrun = []
for i in lines:
    arrayrun.append(i.rstrip())
arrayrunners = []
arrayfinish = []
arraychip = []
for i in arrayrun:
    arrayrunners.append(i[0:5])
    arrayfinish.append(i[5:13])
    arraychip.append(i[13:])

fastestchip = 1000000
fastestchipid = 0
fastestman = ''
counter = 0
for i in arraychip:
    chiptime = int(i[0:2]) * 60 * 60 + int(i[3:5]) * 60 + int(i[6:8])
    if chiptime < fastestchip:
        fastestchip = chiptime
        fastestchipid = counter
        fastestman = arrayrunners[counter]
    counter += 1

print("Fastest runner id:", fastestman, "Chip time:", arraychip[fastestchipid])
runfile.close()

# Task 1.2

def bubblerun(chiparray):
    passes = len(chiparray) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, passes):
            currchiptime = int(chiparray[i][0:2]) * 60 * 60 + int(chiparray[i][3:5]) * 60 + int(chiparray[i][6:8])
            nextchiptime = int(chiparray[i+1][0:2]) * 60 * 60 + int(chiparray[i+1][3:5]) * 60 + int(chiparray[i+1][6:8])
            if currchiptime > nextchiptime:
                arrayrunners[i], arrayrunners[i+1] = arrayrunners[i+1], arrayrunners[i]
                arraychip[i], arraychip[i+1] = arraychip[i+1], arraychip[i]
                swapped = True
        passes -= 1
    return arrayrunners, arraychip

def topthree(chiparray):
    winners = []
    placings = []
    winners.append(chiparray[0])
    placings.append(1)
    determined = 1
    for i in range(1, len(chiparray)):
        if 4 in placings:
            break
        elif chiparray[i] in winners:
            placings.append(determined)
        else:
            winners.append(chiparray[i])
            placings.append(determined + 1)
            determined += 1
    return placings
for i in (topthree(arraychip)):
    if i == 4:
        break
    print(i, '.', arrayrunners[i], arraychip[i])


            
