class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def is_head(self, node):
        return True if node is self.head else False

    def find_node(self, value):
        node = self.head
        while node.value is not value:
            node = node.next
            if node is None:
                return None
        return node

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)
        self.len += 1

    def delete(self, value):
        if self.len == 0:
            return None
        node = self.head
        if node.value is value:
            self.head = node.next
            self.len -= 1
        while node.next.value is not value:
            node = node.next
            if node.next is None:
                return None
        node.next = node.next.next
        self.len -= 1

    def display(self, node=None):
        if self.len == 0:
            return None
        if not node:
            node = self.head
        print(node.value, node.next, id(node))
        if node.next:
            self.display(node=node.next)

    def get_reversed(self):
        '''
        Returns object of reversed LinkedList instance.
        '''
        reversed = LinkedList()
        counter = self.len - 1
        while counter > 0:
            node = self.head
            for i in range(counter):
                if node.next is not None:
                    node = node.next
            reversed.append(node.value)
            counter -= 1
        return reversed

    def reverse(self):
        '''
        Reversing LinkedList instance.
        '''
        node = self.head
        while node is not None:
            next = node.next
            if node is self.head:
                node.next = None
            else:
                node.next = prev
                self.head = node
            prev = node
            node = next
