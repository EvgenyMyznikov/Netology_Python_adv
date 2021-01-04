class Stack:
    def __init__(self):
        self.elements = []

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.elements == []

    def push(self, elem):
        self.elements.append(elem)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[len(self.elements) - 1]




