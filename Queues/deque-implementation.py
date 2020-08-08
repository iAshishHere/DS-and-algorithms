

class Deque(object):

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.insert(0,item)

    def addRear(self,item):
        self.items.append(item)

    def removeFront(self):
        self.items.pop(0)

    def removeRear(self):
        self.items.pop()

    def firstElement(self):
        print(self.items[0])

    def lastElements(self):
        print(self.items[len(self.items)-1])

    def printElement(self):
        print(self.items)


q = Deque()
q.addFront(1)
q.addFront(2)
q.addFront(3)
q.addFront(4)
q.printElement()
q.firstElement()
q.lastElements()
q.removeRear()
q.printElement()
print(q.size())
