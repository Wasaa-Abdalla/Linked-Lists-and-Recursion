# linked_list.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at front (O(1))
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Optional: Insert at end (O(n))
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Recursive sum
    def recursive_sum(self):
        return self._recursive_sum(self.head)

    def _recursive_sum(self, node):
        if node is None:
            return 0
        return node.data + self._recursive_sum(node.next)

    # Recursive search
    def recursive_search(self, target):
        return self._recursive_search(self.head, target)

    def _recursive_search(self, node, target):
        if node is None:
            return False
        if node.data == target:
            return True
        return self._recursive_search(node.next, target)

    # Recursive reverse (in-place)
    def recursive_reverse(self):
        self.head = self._recursive_reverse(self.head, None)

    def _recursive_reverse(self, current, prev):
        if current is None:
            return prev
        next_node = current.next
        current.next = prev
        return self._recursive_reverse(next_node, current)

    # Utility: Print list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
