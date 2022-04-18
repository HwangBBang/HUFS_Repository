class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, val):
        self.items.append(val)
        
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")
    
S = Stack()
S.push(10)
S.push(2)
print (S)