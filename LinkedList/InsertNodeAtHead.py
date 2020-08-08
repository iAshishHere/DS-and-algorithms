
class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insertAtHead(self,newNode):

        secondNode = self.head
        self.head = newNode
        newNode.next = secondNode

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



