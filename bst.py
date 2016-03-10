class BST:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data > self.data:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert(data)
        else:
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert(data)

    def search(self, data):
        if data == self.data:
            print("Data found.")
            return 1
        elif data < self.data:
            if self.left is None:
                print("Data not found.")
                return -1
            else:
                self.left.search(data)

        else:
            if self.right is None:
                print("Data not found.")
                return -1
            else:
                self.right.search(data)

    def lookup(self, data, parent = None):
        if data == self.data:
            return self, parent
        elif data < self.data:
            if self.left is None:
                return None, None
            else:
                return self.left.lookup(data, self)
        else:
            if self.right is None:
                return None, None
            else:
                return self.right.lookup(data, self)

    def delete(self, data):
        node, parent = self.lookup(data)
        if node is not None:
            if node.left == None and node.left == node.right:
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                    del node
                else:
                    node.data = None
                    del node
            elif node.left == None and node.left != node.right:
                if parent:
                    if node.left:
                        n = node.left
                    else:
                        n = node.right
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                else:
                    if node.left:
                        node = node.left
                    else:
                        node = node.right
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.right == successor:
                    parent.right = successor.right
                else:
                    parent.left = successor.right

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end = ' ')
        if self.right:
            self.right.inorder()





















                        

















            


            

        

nBST = BST(50)
nBST.insert(25)
nBST.insert(75)
nBST.inorder()
print()
nBST.insert(16)
nBST.insert(30)
nBST.insert(60)
nBST.insert(80)
nBST.inorder()
print()
nBST.delete(16)
nBST.inorder()
print()
nBST.delete(25)
nBST.inorder()
print()
nBST.delete(75)
nBST.inorder()
print()
print(nBST.left.data, nBST.right.data, nBST.data)
nBST.delete(50)
nBST.inorder()
print()

                    
















            



                
