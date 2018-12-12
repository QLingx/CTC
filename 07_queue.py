class Queue(object):
    def __init__(self,length):
        self.length = length
        self.head = -1 
        self.tail = 0
        self.queue = [0 for i in range(0,length)]
    
    def pop(self):
        if self.isEmpty():
            return None
        elem = self.queue[self.head%self.length]
        self.head = self.head%self.length - 1
        return elem
        
    def push(self,elem):
        if self.isFull():
            return None
        self.queue[self.tail%self.length] = elem
        self.head = self.tail + 1
    
    def top(self):
        if self.isEmpty():
            return None
        return self.queue[self.head%self.length]

    def isEmpty(self):
        if self.tail - self.head == 1:
            return True
        else:
            return False
    
    def isFull(self):
        if self.tail - self.head == self.length:
            return True
        else:
            return False

if __name__ == '__main__':
    queue = Queue(3)
    queue.push(1)
    print(queue.head)
    queue.push(2)
    print(queue.head)
    queue.push(3)
    print(queue.head)
    print(queue.top())


    