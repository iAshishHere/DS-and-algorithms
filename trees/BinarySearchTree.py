class Node:
    def __init__(self,value=None):
        self.value=value
        self.leftNode = None
        self.rightNode = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data, cur_node):
        if data < cur_node.value:
            if cur_node.leftNode is None:
                cur_node.leftNode = Node(data)
            else:
                self._insert(data,cur_node.leftNode)

        elif data > cur_node.value:
            if cur_node.rightNode is None:
                cur_node.rightNode = Node(data)
            else:
                self._insert(data,cur_node.rightNode)

        else: print("dublicate value")

    def find(self, data):
        if self.root:
            is_found = self._find(data,self.root)
            if(is_found):
                return True
            else:
                return False
        else :
            return None

    def _find(self,data,cur_node):
        if  data < cur_node.value and cur_node.leftNode:
            return self._find(data,cur_node.leftNode)
        elif data > cur_node.value and cur_node.rightNode:
            return self._find(data,cur_node.rightNode)
        if data == cur_node.value:
            return True

bst = BST()
bst.insert(10)
bst.insert(20)
bst.insert(5)
bst.insert(31)
r=bst.find(0)
print(r)