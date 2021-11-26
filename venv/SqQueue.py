class SqQueue:

    def __init__(self, size):
        self.front = 0
        self.rear = 0
        self.maxsize = size
        self.len = 0
        self.item = [None for i in range(size)]

    def GetHead(self):
        if self.len == 0:
            raise Exception("队列为空")
        else:
            return self.item[self.front]

    def Enqueue(self, elem):
        if (self.rear + 1) % self.maxsize == self.front:
            raise Exception("队列已满")
        else:
            self.item[self.rear] = elem
            self.rear = (self.rear + 1) % self.maxsize
            self.len += 1

    def Dequeue(self):
        if self.rear == self.front:
            raise Exception("队列为空")
        else:
            data = self.item[self.front]
            self.front = (self.front + 1) % self.maxsize
            self.len -= 1
            return data

    def QueueEmpty(self):
        return self.rear == self.front

    def QueueLength(self):
        return self.len

    def QueuePrint(self):
        front = self.front
        for i in range(self.len):
            print(self.item[front], end='->')
            front = (front + 1) % self.maxsize
            i += 1