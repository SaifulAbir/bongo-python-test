class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


def lca(node1, node2):
    """
    Time complexity is O(n)
    Space complexity is O(n)
    """

    # Valid nodes check
    if node1 is None or node2 is None:
        return None

    # same node check
    if node1 == node2:
        print(node1.value)
        return

    ancestors1 = []

    # Adding node1 and all ancestors of node1 in list ancestors1
    while node1 is not None:
        ancestors1.append(node1)
        node1 = node1.parent

    # Checking if node2 or any of it's ancestors lie in the same list
    while node2 is not None:
        if node2 in ancestors1:
            print(node2.value)
            return
        node2 = node2.parent
    return None  # reaches here only if node1 and node2 are in different trees


if __name__ == '__main__':
    node1 = Node(1, None)
    node2 = Node(2, node1)
    node3 = Node(3, node1)
    node4 = Node(4, node2)
    node5 = Node(5, node2)
    node6 = Node(6, node3)
    node7 = Node(7, node3)
    node8 = Node(8, node4)
    node9 = Node(9, node4)

    lca(node6, node7)
    lca(node3, node7)
