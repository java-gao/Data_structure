class Sqlist:
    def __init__(self,maxsize=10):
        self.curlen = 0
        self.maxsize = maxsize
        self.data = [None]*self.maxsize

    def is_empty(self):
        return self.curlen == 0

    def is_full(self):
        return self.curlen == self.maxsize

    def length(self):
        return self.curlen

    def clearlist(self):
        self.__init__()

    def getElem(self,location):
        if 0 <= location < self.curlen:
            return self.data[location]
        else:
            raise Exception('第i个元素不存在')

    def locateElem(self,elem):
        for j in self.data:
            if self.data[j] == elem:
                return j
        if j == self.curlen:
            return -1

    def listAppend(self,elem):
        if self.curlen == self.maxsize:
            raise Exception('列表已满')
        else:
            self.data[self.curlen] = elem
            self.curlen += 1

    def listInsert(self,location,elem):
        if self.curlen >= self.maxsize:
            raise Exception('列表已满')

        if 0 <= location <= self.curlen:
            for j in range(self.curlen,location,-1):
                self.data[j] = self.data[j-1]

            self.data[location] = elem
            self.curlen += 1
        else:
            raise Exception('插入位置非法')

    def listDelete(self,location):
        if 0 <= location < self.curlen:
            for j in range(location,self.curlen):
                if j == self.curlen - 1:
                    self.data[j] = None
                else:
                    self.data[j] = self.data[j+1]
            self.curlen -= 1
        else:
            raise Exception('删除位置非法')

    def listPrint(self):
        for i in range(self.curlen):
            print(self.data[i])
