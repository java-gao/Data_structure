class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class Linklist:

    def __init__(self,node=None):
        self._head = node
        self.len = 0

    def listLength(self):
        return self.len

    def listAdd(self,elem):
        '''头插法'''
        node = Node(elem)
        node.next = self._head
        self._head = node
        self.len += 1

    def listAppend(self,elem):
        '''尾插法'''
        node = Node(elem)
        cur = self._head
        if cur is None:
            self._head = node
        else:
            while cur.next:
                cur = cur.next
            cur.next = node
        self.len += 1

    def listInsert(self,location,elem):
        '''在指定的位置插入元素'''
        if location <= 1:
            self.listAdd(elem)
        elif location >self.len:
            self.listAppend(elem)
        else:
            node = Node(elem)
            cur = self._head
            count = 1
            while count < location -1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node
            self.len += 1

    def listDelete(self,location):
        cur = self._head
        pre = None
        if self._head is None:
            raise Exception('列表为空')

        if location < 1 or location > self.len:
            raise Exception('删除位置非法')
        elif location == 1:
            self._head = cur.next
        else:
            count = 1
            while count < location:
                if count == location - 1:
                    pre = cur
                cur = cur.next
                count += 1
            pre.next = cur.next

        self.len -= 1

    def locateElem(self,elem):
        count = 1
        cur = self._head
        while cur:
            if cur.elem == elem:
                return count
            else:
                count += 1
                cur = cur.next
        return -1

    def getElem(self,location):
        cur = self._head
        if location < 1 or location > self.len:
            raise Exception('位置非法')
        count = 1
        while count < location:
            cur = cur.next
            count += 1
        return cur.elem

    def listPrint(self):
        cur = self._head
        while cur:
            print(cur.elem, end = '->')
            cur = cur.next

    @property
    def head(self):
        return self._head