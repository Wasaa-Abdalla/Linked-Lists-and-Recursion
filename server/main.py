from linked_list import LinkedList

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_end(30)

    print("Original list:")
    ll.print_list()

    print("Sum of IDs:", ll.recursive_sum())
    print("Search 20:", ll.recursive_search(20))
    print("Search 99:", ll.recursive_search(99))

    ll.recursive_reverse()
    print("Reversed list:")
    ll.print_list()



