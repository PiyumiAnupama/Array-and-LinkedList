'''
RegNo           : AR/96447
ExamNo          : AF/18/14481
NameInitials    : Anupama P.G.P.
Purpose         : Linked List Based Implementation
Date            : 13.06.2021
'''


class Node:                             # Create a class for the Node
    def __init__(self):                 # Constructor
        self.data = None
        self.next = None

    def setData(self, data):            # Set data of the Node
        self.data = data

    def getData(self):                  # Get data of this Node
        return self.data

    def setNext(self, next):            # Set next of the Node
        self.next = next

    def getNext(self):                  # Get next of this Node
        return self.next

    def hasNext(self):                  # Get if it has a Next
        return self.next is not None


class Stack:                            # Create a class for the Stack
    def __init__(self,limit=10):        # Constructor
        self.head = None
        self.length = 0
        self.limit =limit


    def push(self, data):               # Push data of the stack
        newNode = Node()
        newNode.setData(data)

        if self.length==self.limit:
            print("Stack Overflow")
            return

        elif self.head==0:
            self.head=newNode
            return

        else:
            newNode.setData(data)
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1

    def top(self):                      # Return the head Node data
        if self.head is not None:
            return self.head.getData()
        else:
            print("Stack Underflow")



    def pop(self):                      # Remove element that is in the current head
        if self.head is None:
            print("Stack Underflow")

        else:
            popNode = self.head.getData()
            self.head = self.head.getNext()
            self.length -= 1
            return popNode



    def isEmptyStack(self):             # Check is Stack Empty
        if self.length == 0:
            return True
        else:
            return False

    def isFullStack(self):              # Check is Stack Full
        if self.length == self.limit:
            return True
        else:
            return False

    def size(self):                     # get size of the Stack
        return self.length
