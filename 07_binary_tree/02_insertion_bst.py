class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def insert(root, val):
    if root == None:
        return Node(val)
    if root.data == val:
        return root
    if root.data > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inOrderTraversal(rootNode):
    if rootNode != None:
        inOrderTraversal(rootNode.left)
        print(rootNode.data, end=" ")
        inOrderTraversal(rootNode.right)


def searchelement(root, val):
    if root == None:
        print("Element Not Found")
        return
    if root.data == val:
        print("Element Found")
        return
    if root.data > val:
        searchelement(root.left, val)
        return
    if root.data < val:
        searchelement(root.right, val)



root_node = Node(50)
root_node = insert(root_node, 20)
root_node = insert(root_node, 60)
root_node = insert(root_node, 30)
root_node = insert(root_node, 40)
root_node = insert(root_node, 65)
root_node = insert(root_node, 15)
root_node = insert(root_node, 23)
# insert(root_node, 50)

inOrderTraversal(root_node)
print()
searchelement(root_node, 20)
searchelement(root_node, 100)