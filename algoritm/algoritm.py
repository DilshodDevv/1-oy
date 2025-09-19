class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current)
            current = current.next

    def append_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert(self, value, pos):
        new_node = Node(value)
        if pos == 1:
            self.append_first(value)
            return
        current = self.head
        previous = None
        k = 1
        while current and k < pos:
            previous = current
            current = current.next
            k += 1
        if previous:
            previous.next = new_node
            new_node.next = current

    def delete_first(self):
        if self.head:
            self.head = self.head.next

    def delete_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        previous = None
        while current.next:
            previous = current
            current = current.next
        previous.next = None

    def delete(self, pos):
        if pos == 1 and self.head:
            self.head = self.head.next
            return
        current = self.head
        previous = None
        k = 1
        while current and k < pos:
            previous = current
            current = current.next
            k += 1
        if previous and current:
            previous.next = current.next
ll = LinkedList()
ll.add(3)
ll.add(5)
ll.add(7)
ll.add(9)
ll.insert(6, 2)
ll.print_list()
ll.delete(3)
print("After deletion:")
ll.print_list()






