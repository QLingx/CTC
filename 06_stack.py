
class Stack(object):
    def __init__(self,length):
        self.stack = []
        self.top = -1
        self.length = length
        for k in range(0,length):
            self.stack.append(0)
            
    
    def pop(self):
        if self.top != -1:
            elem = self.stack[self.top]
            self.top -= 1
            return elem
    
    def push(self,elem):
        if self.length - 1 < self.top + 1:
            print("stack full")
        else:
            self.top += 1
            self.stack[self.top] = elem

    def Top(self):
        if self.top == -1:
            print("stack empty")
        else:
            return self.stack[self.top]


if __name__ == '__main__':
    stack = Stack(3)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.Top())
    stack.pop()
    print(stack.Top())
    stack.pop()
    print(stack.Top())
    stack.pop()
    print(stack.Top())
    stack.pop()