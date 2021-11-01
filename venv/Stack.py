class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1

    def push(self, elem):
        if self.top == self.size - 1:
            raise Exception("Stack is full")
        self.stack.append(elem)
        self.top += 1

    def pop(self):
        if self.top == -1:
            raise Exception("Stack is Empty")
        self.stack.pop()
        self.top -= 1

    def get_top(self):
        if self.top == -1:
            raise Exception("Stack is Empty")
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def stack_length(self):
        return self.top + 1

    def stack_print(self):
        for i in range(self.top + 1):
            print(self.stack[i])
            i += 1
