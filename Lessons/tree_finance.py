import random

class Node:
    def __init__(self, data=None, title=None, children=None) -> None:
        self.data = data
        self.title = title
        self.children = children

    def calculate_total(self):
        pass

organization = {
    "title": "My organization",
    "offices": [
        {"title": "New York", "offices": [{"title": "Office 1"}, {"title": "Office 2"}]},
        {"title": "London", "offices": [
            {"title": "Office 1"},
            {"title": "Branch 1", "offices": [{"title": "Office 1.1"}, {"title": "Office 1.2"}]},
        ]},
        {"title": "Stockholm", "offices": [{"title": "Office 1"}, {"title": "Office 2"}, {"title": "Office 3"}]},
        {"title": "Kiev", "offices": [{"title": "Office 1"}, {"title": "Office 2"}]},
    ],
}

def build_tree(office):
    if office.get("offices") is None:
        return Node(random.randint(1_000, 1_000_000), title=office["title"])
    
    return Node(data=None, title=office["title"], children=[build_tree(o) for o in office['offices']])


def print_tree(node: Node, depth=0):
    if node.children is None:
        print(" " * (depth*2), "{}: ${}".format(node.title, node.data))
        return
    else:
        print(" " * (depth*2), node.title)

    for child in node.children:
        print_tree(child, depth+1)

def calculate_total(node: Node):
    if node.children is None:
        return node.data

    result = 0
    for child in node.children:
        result += calculate_total(child)
    
    return result

organization_tree = build_tree(organization)
print_tree(organization_tree)
print("Organization total income fo last year: ${}".format(calculate_total(organization_tree)))