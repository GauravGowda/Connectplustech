class newNode:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def insert(node, key):
    if node == None:
        return newNode(key)

    if key < node.key:
        node.left = insert(node.left, key)

    elif key > node.key:
        node.right = insert(node.right, key)

    return node


def findMaxforN(root, N):
    if root == None:
        return -1
    if root.key == N:
        return N
    elif root.key < N:
        k = findMaxforN(root.right, N)
        if k == -1:
            return root.key
        else:
            return k
    elif root.key > N:
        return findMaxforN(root.left, N)


if __name__ == '__main__':
    N = 4

    # creating following BST
    #
    #			 5
    #		 / \
    #		 2	 12
    #	 / \ / \
    #	 1 3 9 21
    #				 / \
    #			 19 25
    root = None
    root = insert(root, 25)
    insert(root, 2)
    insert(root, 1)
    insert(root, 3)
    insert(root, 12)
    insert(root, 9)
    insert(root, 21)
    insert(root, 19)
    insert(root, 25)
    print(findMaxforN(root, N))

