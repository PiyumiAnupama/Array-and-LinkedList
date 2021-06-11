class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next is not None


class Stack:
    def __init__(self, limit=10):
        self.head = None
        self.length = 0
        self.limit = limit

    def push(self, data):
        newNode = Node()
        newNode.setData(data)

        if self.length==self.limit:
            print("Stack Overflow")
            return
        elif self.length < self.limit:
            self.head = newNode
        else:
            newNode.setData(data)
            newNode.setNext(self.head)
            self.head = newNode
        self.length += 1

    def pop(self):
        if self.length == 0:
            print("Stack Underflow")
            return
        else:
            popNode = self.head.getData()
            self.head = self.head.getNext()
            self.length -= 1
            return popNode




    def isEmptyStack(self):
        if self.length == 0:
            return True
        else:
            return False

    def isFullStack(self):
        if self.length == self.limit:
            return True
        else:
            return False

    def size(self):
        return self.length
