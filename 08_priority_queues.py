

class PriorityQueues(object):
    self.queues = []
    self.length = 0

    def pop(self):
        if self.length == 0:
            return None
        else:
            res = self.queues[0]
            self.queues[0] = self.queues[self.length-1]
            self.length -= 1
            self.heapifyDown(0)
            return res
    
    def push(self,elem):
        self.queues.append(elem)
        self.heapifyUp(self.length)
        self.length += 1

    
    def heapify(self,queues):
        for index in range(self.length,-1,-1):
            self.heapifyUp(index)
            

    def heapifyUp(self,i):
        p = self.parent(i)
        if p > 0 and self.queues[p] < self.queues[i]:
            self.queues[p],self.queues[i] = self.queues[i],self.queues[p]
            heapifyUp(p)

    
    def heapifyDown(self,i):
        lc = self.left(i)
        rc = self.right(i)
        max = i
        if lc < self.length and self.queues[lc] < self.queues[max]:
            max = lc
        if rc < self.length and self.queues[rc] < self.queues[max]:
            max = rc
        if i != max:
            self.queues[i],self.queues[max] = self.queues[max],self.queues[i]
            self.heapifyDown(max)


    def parent(self,index):
        return (index-1) / 2

    def left(self,index):
        return index * 2 + 1

    def right(self,index):
        return index * 2 + 2


if __name__ == '__main__':
