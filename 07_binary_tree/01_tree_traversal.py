class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None



# root -> left -> right
def preOrderTraversal(rootNode):
    if rootNode != None :
        print(rootNode.data, end=" ")
        preOrderTraversal(rootNode.left)
        preOrderTraversal(rootNode.right)


# left -> right -> root
def postOrderTraversal(rootNode):
    if rootNode != None:
        postOrderTraversal(rootNode.left)
        postOrderTraversal(rootNode.right)
        print(rootNode.data, end=" ")


# left -> root -> right
def inOrderTraversal(rootNode):
    if rootNode != None:
        inOrderTraversal(rootNode.left)
        print(rootNode.data, end=" ")
        inOrderTraversal(rootNode.right)
        
       




root_node = Node(1)

root_node.left = Node(3)
root_node.right = Node(5)

root_node.left.left = Node(2)
root_node.left.right = Node(4)

root_node.right.right = Node(8)

print("Pre Order Tree Data")
preOrderTraversal(root_node)

print("\n\nPost Order Tree Data")
postOrderTraversal(root_node)

print("\n\nInorder Tree Data")
inOrderTraversal(root_node)