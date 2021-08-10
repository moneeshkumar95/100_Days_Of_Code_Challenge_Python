print('Day 75: Simple Implementation of Trees\n')

def tree(r):
    return [r, [],[]]

def insertLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1,[newBranch, t, []])

    else:
        root.insert(1,[newBranch, [], []])

    return root

def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])

    else:
        root.insert(1, [newBranch, [], []])

    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newValue):
    root[0] = newValue

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = tree(3)

print(insertLeft(r,5))

print(insertRight(r,8))

l = getRightChild(r)
print(l)

setRootVal(l,9)
print(l)

print(r)