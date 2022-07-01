from DoublyLinkedList import DoublyLinkedList, Node


class SortedDoublyLinkedList(DoublyLinkedList):

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
            self.len += 1
            return
        node = self.head
        while True:
            if value <= node.value:
                self.head = Node(value, next=node)
                node.previous = self.head
                self.len += 1
                return
            elif value > node.value and node.next is None:
                node.next = Node(value, previous=node)
                self.len += 1
                return
            elif value > node.value and value > node.next.value:
                node = node.next
            elif node.value < value <= node.next.value:
                node.next = Node(value, previous=node, next=node.next)
                node.next.next.previous = node.next
                self.len += 1
                return

x = SortedDoublyLinkedList()
x.insert(2)
x.insert(3)
x.insert(5)
x.insert(1)
x.insert(4)
x.display()

