print('''Day 76: Implementation of Trees as a class with nodes and reference\n''')

class Tree(object):
    def __init__(self, rootobj):
        self.key = rootobj
        self.leftChild = None
        self.rightchild = None
        
    def insertLeft(self, newnode):
        if self.leftChild == None:
            self.leftChild = Tree(newnode)
            
        else:
            t =Tree(newnode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newnode):
        if self.rightchild == None:
            self.rightchild = Tree(newnode)
        else:
            t = Tree(newnode)
            t.rightchild = self.rightchild
            self.rightchild = t

    def getRightChild(self):
        return self.rightchild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = Tree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())