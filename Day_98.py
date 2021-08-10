print('Day 98\n')

class newNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.visited = False


count = [0]

def NthInorder(node, n):
    if (node == None):
        return

    if (count[0] <= n):

        NthInorder(node.left, n)
        count[0] += 1

        if (count[0] == n):
            return f'{n}th node of inorder traversal is {node.data}'

        NthInorder(node.right, n)


root = newNode(10)
root.left = newNode(20)
root.right = newNode(30)
root.left.left = newNode(40)
root.left.right = newNode(50)

n = int(input('Enter the n value: '))

print(f'\nOutput: {NthInorder(root, n)}')
