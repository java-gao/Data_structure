class Queue:
    def __init__(self):
        self.item = []

    def GetHead(self):
        return self.item[0]

    def Enqueue(self, elem):
        self.item.append(elem)

    def Dequeue(self):
        return self.item.pop(0)

    def QueueEmpty(self):
        return len(self.item) == 0

    def QueueLength(self):
        return len(self.item)
