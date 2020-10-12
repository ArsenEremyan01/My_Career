class MyLinkedList:

    def __init__(self):

        self.head = []

    def get(self, index: int) -> int:
        if index >= len(self.head):
            return -1
        return self.head[index]

    def addAtHead(self, val: int) -> None:

        self.head.insert(0,val)

    def addAtTail(self, val: int) -> None:
        self.head.append(val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index == len(self.head):
            self.head.append(val)
        elif index > len(self.head):
            pass
        else:
            self.head.insert(index,val)
    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.head):
            self.head.pop(index)


listt = MyLinkedList()
listt.addAtHead(1)
listt.addAtTail(3)
listt.addAtIndex(1,2)
listt.get(1)
listt.deleteAtIndex(1)
listt.get(1)
print()