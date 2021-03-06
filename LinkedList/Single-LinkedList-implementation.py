

class Node(object):

    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next == None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertAtNth(self, newNode, position):
        if position == 0:
            if self.head == None:
                self.head = newNode
            else:
                nextNode = self.head
                self.head = newNode
                newNode.next = nextNode

        else:
            currentNode = self.head
            currentPosition = 0

            while True:
                if currentPosition == position:
                    prevNode.next = newNode
                    newNode.next = currentNode
                    break

                prevNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1




    def printData(self):

        if self.head == None:
            print("Linkedlist is Empty")
        currentNode = self.head
        while True:
            if currentNode.next == None:
                print(currentNode.value)
                break
            print(currentNode.value)
            currentNode = currentNode.next


a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)
f = Node(1100)
g = Node(0000)
i = Node(33333333)


l = LinkedList()
l.insert(a)
l.insert(b)
l.insert(c)
l.insert(d)
l.insert(e)
l.insertAtNth(f,2)
l.insertAtNth(g,0)
l.insertAtNth(i,0)

l.printData()