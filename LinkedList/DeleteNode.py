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

    def deleteNthElement(self, position):

        if position == 0:
            currentNode = self.head.next
            presentNode = self.head
            self.head = currentNode
            presentNode.next = None

            return


        currentPosition = 0
        currentElement = self.head

        while True:

            if currentPosition == position:
                prevElement.next = currentElement.next
                currentElement.next = None
                break


            prevElement = currentElement
            currentElement = currentElement.next
            currentPosition += 1




    def deleteLastElement(self):

        if self.head.next == None:
            self.head = None
            return
        currentNode = self.head
        while currentNode.next is not None:
            prevNode = currentNode
            currentNode = currentNode.next
        del currentNode
        prevNode.next = None

    def printData(self):
        if self.head == None:
            print("Linkedlist is Empty")
            return
        currentNode = self.head
        while True:
            if currentNode.next == None:
                print(currentNode.value)
                break
            print(currentNode.value)
            currentNode = currentNode.next


#Operations
a = Node(10)
b = Node(20)
c = Node(30)
l = LinkedList()
l.insert(a)
l.insert(b)
l.insert(c)
l.deleteNthElement(0)
l.printData()