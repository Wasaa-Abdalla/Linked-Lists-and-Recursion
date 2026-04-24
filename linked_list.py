class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert new node at the front
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert new node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Public method for recursive sum
    def recursive_sum(self):
        return self._recursive_sum(self.head)

    def _recursive_sum(self, node):
        if node is None:
            return 0
        return node.data + self._recursive_sum(node.next)

    # Public method for recursive search
    def recursive_search(self, target):
        return self._recursive_search(target, self.head)

    def _recursive_search(self, target, node):
        if node is None:
            return False
        if node.data == target:
            return True
        return self._recursive_search(target, node.next)

    # Public method for recursive reverse
    def recursive_reverse(self):
        self.head = self._recursive_reverse(self.head, None)

    def _recursive_reverse(self, node, prev):
        if node is None:
            return prev
        next_node = node.next
        node.next = prev
        return self._recursive_reverse(next_node, node)
