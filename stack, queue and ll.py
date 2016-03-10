class Stack:

    def __init__(self, size):
        self.size = size
        self.top = -1
        self.stack = [None for x in range(size)]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self,data):
        if self.isFull():
            print('Cannot insert to full stack')
            return -1
        else:
            self.top += 1
            self.stack[self.top] = data
            return data

    def pop(self):
        if self.isEmpty():
            print("Cannot remove from empty stack")
            return -1
        else:
            data = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return data

    def display(self):
        if self.isEmpty():
            print("Empty Stack.")
        else:
            print('Stack Contents: ', end = '')
            for i in range(self.top + 1):
                print(self.stack[i], end = '')
            print()
newstack = Stack(10)
newstack.push(1)
newstack.push(2)
newstack.display()
newstack.pop()
newstack.display()


class Queue:

    MAX = 6

    def __init__(self):
        self.rear = 0
        self.front = 0
        self.queue = [None for x in range(self.MAX)]

    def isEmpty(self):
        return self.rear == self.front

    def size(self):
        if self.rear >= self.front:
            return self.rear - self.front
        else:
            return self.rear + self.MAX - self.front

    def isFull(self):
        return self.size() == self.MAX - 1


    def enqueue(self, data):
        if self.isFull():
            print("Cannot enqueue to full queue")
            return -1
        else:
            self.queue[self.rear] = data
            self.rear = (self.rear + 1) % self.MAX
            return 1

    def dequeue(self):
        if self.isEmpty():
            print("Cannot dequeue from empty queue")
            return -1
        else:
            data = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.MAX
            return data

    def display(self):
        if self.isEmpty():
            print("Empty Queue.")
            return - 1
        else:
            print("Queue Contents: ", end = '')
            if self.rear > self.front:
                for i in range(self.front, self.rear):
                    print(self.queue[i], end = '')
            else:
                for i in range(self.front, self.MAX):
                    print(self.queue[i], end = '')
                for j in range(self.rear):
                    print(self.queue[j], end = '')
            print()


newQ = Queue()
newQ.enqueue(1)
newQ.enqueue(2)
newQ.display()
newQ.dequeue()
newQ.display()
newQ.enqueue(3)
newQ.enqueue(4)
newQ.enqueue(5)
newQ.enqueue(6)
newQ.enqueue(5)
newQ.display()
newQ.dequeue()
newQ.enqueue(3)
newQ.display()                    
                

class Node:

    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            prev = None
            while curr and data > curr.data:
                prev = curr
                curr = curr.link
            if curr is None:
                prev.link = newNode
            elif prev is None:
                newNode.link = curr
                self.head = newNode
            else:
                prev.link = newNode
                newNode.link = curr

    def delete(self, target):
        curr = self.head
        prev = None
        while curr and target > curr.data:
            prev = curr
            curr = curr.link
        if curr.data != target:
            print("Ëlement not found.")
            return -1
        elif prev is None:
            self.head = curr.link
        else:
            prev.link = curr.link

    def display(self):
        print("Linked List Contenst: ", end = '')
        curr = self.head
        while curr:
            print(curr.data, end = ' ')
            curr = curr.link
        print()

newL = LinkedList()
a = [5,4,3,2,1]
for i in a:
    newL.insert(i)
newL.display()
b = [5, 1, 3]
for i in b:
    newL.delete(i)
newL.display()

    














