class Node:
    def __init__(self, elem):
        self.data = elem
        self.next = None


class Staticlist:

    def __init__(self, size):
        self.maxsize = size
        self.link = [Node(None) for i in range(size + 2)]
        self.link[size + 1].data = None
        self.link[size + 1].next = 0

        i = 0
        while i < size:
            self.link[i].next = i + 1
            i += 1

        self.len = 0

    def malloc_sll(self):
        if self.link[0].next is not None:
            i = self.link[0].next
            self.link[0].next = self.link[self.link[0].next].next
            return i
        else:
            raise Exception("列表已满")

    def free_sll(self, location):
        self.link[location].next = self.link[0].next
        self.link[location].data = None
        self.link[0].next = location

    def listlen(self):
        return self.len

    def is_empty(self):
        return self.len == 0

    def list_append(self, elem):
        if self.len > self.maxsize:
            raise Exception("静态列表空间已满")
        else:
            node_index = self.malloc_sll()
            cur = self.link[self.maxsize + 1].next
            print(node_index)
            print(cur)
            if cur == 0:
                self.link[self.maxsize + 1].next = node_index
                self.link[node_index].data = elem
            else:
                count = 1
                while count < self.len:
                    cur = self.link[cur].next
                    count += 1
                self.link[node_index].next = self.link[cur].next
                self.link[node_index].data = elem
                self.link[cur].next = node_index

            self.len += 1

    def list_add(self, elem):
        if self.len > self.maxsize:
            raise Exception("静态列表空间已满")
        else:
            node_index = self.malloc_sll()
            cur = self.link[self.maxsize + 1].next
            if cur == 0:
                self.link[self.maxsize + 1].next = node_index
                self.link[node_index].next = None
                self.link[node_index].data = elem
            else:
                self.link[node_index].next = cur
                self.link[node_index].data = elem
                self.link[self.maxsize + 1].next = node_index

            self.len += 1

    def list_insert(self, location, elem):
        if self.len > self.maxsize:
            raise Exception("静态链表空间已满")
        if location < 1 or location > self.len:
            raise Exception("插入位置非法")
        else:
            if location == 1:
                self.list_add(elem)
            elif location == len:
                self.list_append(elem)
            else:
                node_index = self.malloc_sll()
                cur = self.link[self.maxsize + 1].next
                count = 1
                while count < location - 1:
                    cur = self.link[cur].next
                    count += 1
                self.link[node_index].data = elem
                self.link[node_index].next = self.link[cur].next
                self.link[cur].next = node_index

    def list_delete(self, location):
        if self.len == 0:
            raise Exception("列表为空")
        if location < 1 or location > self.len:
            raise Exception("删除位置非法")
        else:
            cur = self.link[self.maxsize + 1].next
            if location == 1:
                self.link[self.maxsize + 1].next = self.link[cur].next
                self.free_sll(cur)
            else:
                count = 1
                while count < location:
                    if count == location - 1:
                        pre = cur
                    cur = self.link[cur].next
                    count += 1
                self.link[pre].next = self.link[cur].next
                self.free_sll(cur)
            self.len -= 1

    def locate_elem(self, elem):
        cur = self.link[self.maxsize + 1].next
        count = 1
        while count < self.len:
            if self.link[cur].data == elem:
                return count
            else:
                cur = self.link[cur].next
                count += 1
        return -1

    def get_elem(self, location):

        if location < 1 or location > self.len:
            raise Exception("位置非法")
        cur = self.link[self.maxsize + 1].next
        count = 1
        while count < location:
            cur = self.link[cur].next
            count += 1
        return self.link[cur].data

    def list_print(self):
        cur = self.link[self.maxsize + 1].next
        count = 1
        while count < self.len + 1:
            print(self.link[cur].data, end='->')
            cur = self.link[cur].next
            count += 1
