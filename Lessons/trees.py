class Node:
    def __init__(self, data, children=None) -> None:
        self.data = data
        self.children = children
    
    def print_tree(self, depth=0):
        mark = "-" if self.children is None else "|"
        print(" " * (depth*2), mark, self.data)

        if self.children is None:
            return

        for child in self.children:
            child.print_tree(depth+1)


def print_tree(node: Node, depth=0):
    print(" " * (depth*2), node.data)

    if node.children is None:
        return

    for child in node.children:
        print_tree(child, depth+1)


tree = Node("root", children=[
    Node("data 1", children=[
        Node("data 1.1"),
        Node("data 1.2", children=[
            Node("data 1.2.1")
        ]),
        Node("data 1.3")
    ]),
    Node("data 2", children=[
        Node("data 2.1", children=[
            Node("data 2.1.1", children=[
                Node("data 2.1.1.1"),
                Node("data 2.1.1.2"),
            ]),
            Node("data 2.1.2", children=[
                Node("data 2.1.2.1"),
            ]),
        ]),
    ]),
    Node("data 3"),
    Node("data 4", children=[])
])
print_tree(tree)