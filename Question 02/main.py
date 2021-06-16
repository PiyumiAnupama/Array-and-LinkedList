from Stack import Stack

myStack=Stack(6)
print("Number of Stack's Nodes : ",myStack.size())

print(" ")

print(myStack.top())
print(myStack.pop())

print(" ")

print(myStack.isFullStack())
print(myStack.isEmptyStack())

print(" ")

myStack.push(5)
myStack.push(10)
myStack.push(15)
myStack.push(20)
myStack.push(25)
print("Remove Node is : ",myStack.pop())
print("Remove Node is : ",myStack.pop())

print(" ")

print("Top Node is : ",myStack.top())
print("Number of Stack's Nodes : ",myStack.size())
myStack.push(30)
myStack.push(35)
myStack.push(40)
myStack.push(45)
print("Number of Stack's Nodes : ",myStack.size())

print(" ")

print(myStack.isFullStack())
print(myStack.isEmptyStack())
