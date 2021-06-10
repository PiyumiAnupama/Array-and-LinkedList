import numpy as np


class Stack:
    def __init__(self, limit=10):
        self.limit = limit
        self.stack = np.array([])

    def push(self, data):
        if len(self.stack) < self.limit:
            self.stack = np.append(self.stack, [data])
            return self.stack
        else:
            print("Stack Overflow")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            self.stack = np.resize(self.stack, (len(self.stack) - 1))

    def top(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            Lenght = len(self.stack)
            listTop = self.stack[Lenght - 1]
            return listTop

    def isEmptyStack(self):
        return len(self.stack) == 0

    def isFullStack(self):
        return len(self.stack) == self.limit

    def size(self):
        return len(self.stack)
