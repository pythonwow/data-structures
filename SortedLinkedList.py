from LinkedList import LinkedList, Node


class SortedLinkedList(LinkedList):

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
            self.len += 1
            return
        node = self.head
        while True:
            if value <= node.value:
                self.head = Node(value, node)
                self.len += 1
                return
            elif value > node.value and node.next is None:
                node.next = Node(value)
                self.len += 1
                return
            elif value > node.value and value > node.next.value:
                node = node.next
            elif node.value < value <= node.next.value:
                node.next = Node(value, node.next)
                self.len += 1
                return
