'''
RegNo           : AR/96447
ExamNo          : AF/18/14481
NameInitials    : Anupama P.G.P.
Purpose         : Array Based Implementation using numpy array
Date            : 13.06.2021
'''


import numpy as np


class Stack:                                                # Create a class for the Stack
    def __init__(self, limit=10):                           # Constructor
        self.limit = limit
        self.stack = np.array([])

    def push(self, data):                                   # Push data of the stack
        if len(self.stack) < self.limit:
            self.stack = np.append(self.stack, [data])
            return self.stack
        else:
            print("Stack Overflow")
            return

    def pop(self):                                          # Remove last element of the stack
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            self.stack = np.resize(self.stack, (len(self.stack) - 1))

    def top(self):                                          # Return the last Node data
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            Lenght = len(self.stack)
            listTop = self.stack[Lenght - 1]
            return listTop

    def isEmptyStack(self):                                 # Check is Stack Empty
        return len(self.stack) == 0

    def isFullStack(self):                                  # Check is Stack Full
        return len(self.stack) == self.limit

    def size(self):                                         # Get length of the stack
        return len(self.stack)
