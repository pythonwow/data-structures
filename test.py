import unittest
from LinkedList import LinkedList
from SortedLinkedList import SortedLinkedList
from DoublyLinkedList import DoublyLinkedList
from SortedDoublyLinkedList import SortedDoublyLinkedList
from BinaryTree import BinaryTree


class TestLinkedList(unittest.TestCase):

    linked_list = LinkedList()
    values = [1, 2, 3, 4, 5]
    for val in values:
        linked_list.append(val)

    def test_1_append(self, linked_list=linked_list):
        mssg = "Error during LinkedList append method."
        # checking if nodes are at their right places
        self.assertEqual(linked_list.head.value, 1, mssg)
        self.assertEqual(linked_list.head.next.next.value, 3, mssg)

    def test_2_len(self, linked_list=linked_list):
        mssg = "Returns wrong linked list length."
        # checking if attribute len keeps updated
        linked_list.append(6)
        self.assertEqual(linked_list.len, 6, mssg)
        linked_list.delete(6)
        self.assertEqual(linked_list.len, 5, mssg)

    def test_3_delete(self, linked_list=linked_list):
        # checking if delete does it s job
        linked_list.delete(1)
        self.assertEqual(linked_list.head.value, 2, "Error during delete function handling.")

    def test_4_reverse(self, linked_list=linked_list):
        # checking if reverse and get_reversed actually do their work
        reversed_object = linked_list.get_reversed()
        linked_list.reverse()
        list_of_values_same_instance = linked_list.get_values_list()
        list_of_values_object_copy = reversed_object.get_values_list()

        self.assertEqual(list_of_values_same_instance, [5, 4, 3, 2], "Error during reversing the LinkedList instance.")
        self.assertEqual(list_of_values_object_copy, [5, 4, 3, 2], "Error during returns of reversed LinkedList copy.")
        self.assertFalse(list_of_values_object_copy is list_of_values_same_instance, "Return same instance.")

class TestSortedLinkedList(unittest.TestCase):
    def test_1_sorting(self):
        sorted_ll = SortedLinkedList()
        values = [3, 5, 1, 2, 4]
        for val in values:
            sorted_ll.insert(val)
        self.assertEqual(sorted_ll.get_values_list(), [1, 2, 3, 4, 5], "Wrong sorted values.")


class TestDoublyLinkedList(unittest.TestCase):
    def test_1_append(self):
        values = [1, 2, 3, 4, 5]
        doubly_ll = DoublyLinkedList()
        for val in values:
            doubly_ll.append(val)
        self.assertEqual(doubly_ll.head.next.previous, doubly_ll.head, "Wrong previous connection.")
        doubly_ll.delete(2)
        self.assertEqual(doubly_ll.head.next.previous, doubly_ll.head, "Wrong previous connection.")
        self.assertEqual(doubly_ll.head.next.value, 3, "Wrong next connection after delete.")


class TestSortedDoublyLinkedList(unittest.TestCase):
    def test_1_insert(self):
        sd_ll = SortedDoublyLinkedList()
        values = [3, 2, 5, 4, 1]
        for val in values:
            sd_ll.insert(val)
        self.assertEqual(sd_ll.head.next.previous, sd_ll.head, "Wrong previous connection.")
        sd_ll.delete(2)
        self.assertEqual(sd_ll.head.next.value, 3, "Error during delete handling.")
        self.assertEqual(sd_ll.head.next.previous.value, 1, "Error during delete handling.")

class TestBinaryTree(unittest.TestCase):

    tree = BinaryTree()
    values = [5, 3, 6, 2, 4, 6, 10, 11, 10, 0, 1]
    for value in values:
        tree.insert(value)

    def test_1_insert(self, tree=tree):
        mssg = "Incorrect node insertion to the BinaryTree."
        # checking if nodes were put in the right places
        self.assertEqual(tree.root.left.right.value, 4, mssg)
        self.assertEqual(tree.root.right.left.value, 6, mssg)
        self.assertEqual(tree.root.left.left.left.right.value, 1, mssg)

    def test_2_delete(self, tree=tree):
        mssg = "Error during delete func handling."
        # delete root
        tree.delete(5)
        self.assertEqual(tree.root.value, 6, mssg)
        self.assertIsNone(tree.root.right.left, mssg)
        # delete node with 2 children
        tree.delete(3)
        self.assertEqual(tree.root.left.value, 4, mssg)
        self.assertEqual(tree.root.left.left.value, 2, mssg)
        self.assertFalse(tree.root.left.has_right(), mssg)
        # delete node with no child
        tree.delete(11)
        self.assertIsNone(tree.root.right.right.right, mssg)
        self.assertEqual(tree.root.right.right.value, 10, mssg)
        # delete node which does not exist
        self.assertIsNone(tree.delete(99), mssg)
