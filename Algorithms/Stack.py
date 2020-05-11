class Stack:
    def __init__(self):
        self.items = []
    def append(self,a):
        self.items.append(a)

    def pop(self):
        return self.items.pop()

    def length(self):
        return len(self.items)

    def check(self):
        if self.items:
            return True
        else:
            return False


s = Stack()

s.append("Arsen")
s.append("Arman")
s.append("Rudolf")
print(s.check())
print(s.pop())
print(s.length())
