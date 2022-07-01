from LinkedList import LinkedList


class Node:

    def __init__(self, value, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next


class DoublyLinkedList(LinkedList):

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            self.len += 1
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(value, previous=node)
            self.len += 1

    def delete(self, value):
        if self.len == 0:
            return None
        node = self.head
        if node.value is value:
            self.head = node.next
            self.head.previous = None
            self.len -= 1
        while node.next.value is not value:
            node = node.next
            if node.next is None:
                return None
        node.next = node.next.next
        node.next.previous = node
        self.len -= 1



