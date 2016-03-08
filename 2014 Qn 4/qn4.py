from random import randint

class node:

    def __init__(self, data):
        self.data = data
        self.link = None

class pond:

    def __init__(self, length, width, fish = int(input("Number of fishes in pond: "))):
        self.length = length
        self.width = width
        self.size = self.length * self.width
        self.head = None
        self.fish = fish

    def putFish(self):
        count = 0
        while count < self.fish: 
            location = randint(0, self.size)
            currlocation = 0
            curr = self.head
            prev = None
            while curr and currlocation != location:
                prev = curr
                curr = curr.link
                currlocation += 1
            if curr is None: # Repeat if location found already has a stone
                a = ''
            elif curr.data == '.':
                curr.data = 'F'
                count += 1
    
    def fillWater(self): #Fill the next empty space with water
        newNode = node('.')
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            prev = None
            while curr:
                prev = curr
                curr = curr.link
            prev.link = newNode
                
    def waterVolume(self): # Returns the amount of water spaces
        volume = 0
        curr = self.head
        while curr:
            if curr.data == '.':
                volume += 1
            curr = curr.link
        return volume

    def stoneThrow(self):
        while True: 
            location = randint(0, self.size)
            currlocation = 0
            curr = self.head
            prev = None
            while curr and currlocation != location:
                prev = curr
                curr = curr.link
                currlocation += 1
            if curr is None: # Repeat if location found already has a stone
                a = ''
            elif curr.data == '.':
                curr.data = 'x'
                break

    def stoneThrowCoord(self):
        coordx = int(input("X coordinate <1 to 15>"))  
        coordy = int(input("Y coordinate <1 to 8>"))
        location = 0
        if coordy == 1:
            location = coordx - 1
        else:
            location = 15 * (coordy - 1) + coordx - 1
        currlocation = 0
        curr = self.head
        prev = None
        while curr and currlocation != location:
            prev = curr
            curr = curr.link
            currlocation += 1
        if curr is None:
            print("Invalid location.")
        elif curr.data == '.':
            curr.data = 'S'

    def foodThrowCoord(self):
        coordx = int(input("X coordinate <1 to 15>"))  
        coordy = int(input("Y coordinate <1 to 8>"))
        location = 0
        if coordy == 1:
            location = coordx - 1
        else:
            location = 15 * (coordy - 1) + coordx - 1
        currlocation = 0
        curr = self.head
        prev = None
        while curr and currlocation != location:
            prev = curr
            curr = curr.link
            currlocation += 1
        if curr is None:
            print("Invalid location.")
        elif curr.data == '.':
            curr.data = 'P'
        elif curr.data == 'F':
            curr.data = 'H'
    
    def display(self):
        curr = self.head
        count = 0
        while curr:
            if count == self.width:
                print('\n'+curr.data, end='')
                curr = curr.link
                count = 1
            else:
                print(curr.data, end='')
                curr = curr.link
                count += 1
        print()
    def isHappy(self):
        curr = self.head
        while curr:
            if curr.data == 'H':
                return True
            curr = curr.link
        return  False

def fillPool(pool): # Fill an empty pool
    count = 0
    while count < pool.size:
        pool.fillWater()
        count += 1

# Fill pool with stones until pool is full
# 
# while newPond.waterVolume() != 0:
#    newPond.stoneThrow()
#    newPond.display()
#    print(newPond.waterVolume())
#    print()
        


# Task 4.1

newPond = pond(8, 15) # New pond 15 m x 8 m
        
fillPool(newPond)

# newPond.stoneThrowCoord() # Throw a stone with specific coordinates

# newPond.display()

# Task 4.3

# newPond.putFish()
# newPond.display()

# Task 4.4
newPond.putFish()
while not newPond.isHappy():
    newPond.foodThrowCoord()
    newPond.display()

