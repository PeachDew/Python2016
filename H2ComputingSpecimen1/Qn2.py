
def bubblesort(list):
    for j in range(0, len(list)- 1):
        for i in range(0, len(list) - 1):
            if list[i] > list[i+1]:
                temp = list[i]
                list[i], list[i+1] = list[i+1], list[i]
    return list

print(bubblesort([9,8,7,6,5]))

def effbubblesort(alist):
    passes = len(alist)
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, passes - 1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1],  alist[i]
                swapped = True
        passes -= 1
    return alist

print(effbubblesort([9,8,7,6,5]))

animalfile = open('ANIMALS+SPORTS.txt','r')
lines = animalfile.readlines()
animalarray = []
for i in lines:
    animalarray.append(i.rstrip())
animalfile.close()

print(bubblesort(animalarray))
