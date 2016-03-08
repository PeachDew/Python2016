# 2015 Qn 4
# Task 4.1

# Task 4.2
def ValidateUserID():
    ThisUserID = input("Enter an ID for validation: ")
    if ThisUserID == '':
        return 2
    elif len(ThisUserID) != 9:
        return 1
    elif ThisUserID[0:4] != '2015':
        return 'Wrong Year'
    elif ThisUserID[4] != '_':
        return 'Wrong Format'
    try:
        int(ThisUserID[5:])
        int(ThisUserID[0:4])
    except:
        return 3

# print(ValidateUserID())

# Task 4.3
class Queue:
    MAX = 20

    def __init__(self):
        self.queue = [None for x in range(self.MAX)]
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear

    def size(self):
        if self.front > self.rear:
            return self.rear - self.front
        elif self.isEmpty():
            return 0
        else:
            return self.rear + self.MAX - self.front

    def isFull(self):
        return self.size() == self.MAX - 1

    def enqueue(self, data):
        if self.isFull():
            print("Cannot enqueue to full queue")
        else:
            self.queue[self.rear] = data
            self.rear = (self.rear + 1) % self.MAX

    def dequeue(self):
        if self.isEmpty():
            print("Cannot dequeue from empty queue")
        else:
            data = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.MAX
            return data

    def peek(self):
        if self.isEmpty():
            print("Empty Queue")
        else:
            print(self.queue[self.front])

    def display(self):
        if self.isEmpty():
            print("Empty Queue")
        else:
            if self.rear > self.front:
                for i in range(self.front, self.rear):
                    print(self.queue[i], end='')
            else:
                for i in range(self.front, self.MAX):
                    print(self.queue[i], end='')
                for j in range(self.rear):
                    print(self.queue[j], end='')

newQueue = Queue()
newQueue.enqueue(1)
newQueue.enqueue(2)
newQueue.enqueue(3)
newQueue.enqueue(4)
newQueue.display()
newQueue.dequeue()
print()
newQueue.display()
                  
