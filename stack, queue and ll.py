class Stack:

    def __init__(self, size):
        self.size = size
        self.top = -1
        self.stack = [None for x in range(size)]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, data):
        if self.isFull():
            print("Cannot insert to full stack.")
        else:
            self.top += 1
            self.stack[self.top] = data

    def pop(self):
        if self.isEmpty():
            print("Cannot pop from empty stack.")
        else:
            data = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return data

    def display(self):
        if self.isEmpty():
            print("Empty Stack.")
        else:
            print("Stack Contents: ", end='')
            for i in range(0, self.top + 1):
                print(self.stack[i], end = ' ')
            print()

newstack = Stack(10)
newstack.push(1)
newstack.push(2)
newstack.display()
newstack.pop()
newstack.display()
