class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) != 0:
            a = self.stack[len(self.stack)-1]
            del self.stack[len(self.stack)-1]
            return a
        return None # если стек пустой

    def push(self, value):
        self.stack.insert(0,value)
        # ваш код

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[len(self.stack)-1]
        return None # если стек пустой
class Stack_1:
    def __init__(self):
        self.stack = Stack()

    def size(self):
        return self.stack.size()

    def pop(self):
        return self.stack.pop()

    def push(self, value):
        return self.stack.push(value)
        # ваш код

    def peek(self):
        return self.stack.peek()

class Queue:
    def __init__(self):
        self.stack = Stack_1()

    def enqueue(self, item):
        return self.stack.push(item)
        # вставка в хвост

    def dequeue(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

def round(st,N):
    for i in range(N):
        #item = st[st.len() - 1]
        #del st [st.len() - 1]
        st.enqueue(st.dequeue())