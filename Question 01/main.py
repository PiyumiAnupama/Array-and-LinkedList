from Stack import Stack

myStack=Stack(9)
print(myStack.size())
print(myStack.isEmptyStack())
print(myStack.isFullStack())
print(myStack.top())
print(myStack.pop())

myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")

print(myStack.stack)

myStack.pop()

print(myStack.stack)

print(myStack.top())

print(myStack.size())
myStack.push("E")
myStack.push("F")
myStack.push("G")
myStack.push("H")

myStack.pop()
myStack.pop()
print(myStack.top())
myStack.push("I")
myStack.push("J")
myStack.push("K")
myStack.push("L")
myStack.push("M")

print(myStack.stack)
print(myStack.isEmptyStack())
print(myStack.isFullStack())