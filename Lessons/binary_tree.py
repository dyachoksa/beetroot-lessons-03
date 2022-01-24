class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

def print_tree(node: Node, depth=0):
    if node is None: return

    print_tree(node.left, depth+1)  
    print(" " * (depth*2), node.data) 
    print_tree(node.right, depth+1)

tree = Node(10, 
    left=Node(4,
        left=Node(5)
    ), 
    right=Node(9, 
        left=Node(6),
        right=Node(8, right=Node(12)),
    )
)

print_tree(tree)
