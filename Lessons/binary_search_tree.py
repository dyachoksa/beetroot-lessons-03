class Node:
    def __init__(self, key=None, data=None, left=None, right=None) -> None:
        self.key = key
        self.left = left
        self.right = right
        self.data = data

    def __repr__(self) -> str:
        return "<Node key={} data={}>".format(self.key, self.data)

    def insert(self, key, data=None):
        if self.key is None:
            self.key = key
            self.data = data
            return

        if key < self.key:
            if self.left:
                self.left.insert(key, data)
                return
            
            self.left = Node(key, data=data)
            return
        
        if self.right:
            self.right.insert(key, data=data)
            return
        
        self.right = Node(key, data=data)
    
    def get_min(self):
        current = self

        while current.left is not None:
            current = current.left
        
        return current.key
    
    def get_max(self):
        current = self

        while current.right is not None:
            current = current.right

        return current.key

    def search(self, key):
        if self.key == key:
            return self
        
        if key < self.key:
            if self.left is None:
                return None
            
            return self.left.search(key)
        
        if self.right is None:
            return None
        
        return self.right.search(key)


def print_tree(node: Node, depth=0):
    if node is None: return

    print_tree(node.left, depth+1)  
    print(" " * (depth*2), node.key) 
    print_tree(node.right, depth+1)


def main():
    numbers = [12, 10, 15, 17, 8, 2, 13, 9]

    search_tree = Node(11)
    for num in numbers:
        search_tree.insert(num)

    print_tree(search_tree)

    print("Min:", search_tree.get_min())
    print("Max:", search_tree.get_max())

    print("Search for 15:", search_tree.search(15))
    print("Search for 7:", search_tree.search(7))

    # A list (Python-dictionaty) of contacts
    contacts = {
        "id-01": {"id": "id-01", "name": "Anna", "email": "anna@example.com"},
        "id-02": {"id": "id-02", "name": "Ben", "email": "Ben@example.com"},
        "id-03": {"id": "id-03", "name": "John", "email": "john@example.com"},
        "id-04": {"id": "id-04", "name": "Alex", "email": "alex@example.com"},
        "id-05": {"id": "id-05", "name": "Jane", "email": "jane@example.com"},
    }

    search_tree = Node()
    for id_ in contacts.keys():
        search_tree.insert(contacts[id_]["name"], data=id_)

    print_tree(search_tree)

    result = search_tree.search("Alex")
    print("Search for Alex:", result)
    if result is not None:
        print(contacts[result.data])


if __name__ == "__main__":
    main()
