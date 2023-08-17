## Delete a node and all its children from a non-binary tree given only a reference to the node to be deleted.
## The node to be deleted is not the root node.
## The node only has a reference to its parent node.

class Node:
    def __init__(self, parent_node=None, children=None, value=None):
        self.parent_node = parent_node
        self.children = children
        self.value = value

    def add_child(self, child_node):
        self.children.append(child_node)

    def delete_node(self):
        self.parent_node.children.remove(self)
        self.parent_node = None
        self.children = None


def populate_tree(node_list):
    tree = {}
    root = Node(value=-1)

    tree[-1] = {-1: root}

    for index, parent_node_height in enumerate(node_list):
        node = Node(value=index)

        if not tree.get(parent_node_height):
            tree[parent_node_height] = {}

        if parent_node_height == 0:
            parent_node = root
        else:
            parent_node = tree[parent_node_height - 1][list(tree[parent_node_height - 1].keys())[-1]]

        if parent_node:
            if parent_node.children is None:
                parent_node.children = []

            parent_node.children.append(node)
            node.parent_node = parent_node

        tree[parent_node_height][index] = node

    return root


def print_tree(root, height=0):
    root_string = "root\n|\nv"
    print(height * '--->' + f'{root.parent_node.value if root.parent_node else root_string}')
    if root.children:
        for child in root.children:
            print_tree(child, height=height+1)


if __name__ == "__main__":
    node_list = [0, 1, 1, 2, 2, 3, 3, 3, 4, 4, 0, 0]
    root = populate_tree(node_list)
    print_tree(root)