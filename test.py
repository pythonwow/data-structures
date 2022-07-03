import unittest
from LinkedList import LinkedList
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
        list_of_values_same_instance = []
        list_of_values_object_copy = []
        node = linked_list.head
        while node:
            list_of_values_same_instance.append(node.value)
            node = node.next
        node = reversed_object.head
        while node:
            list_of_values_object_copy.append(node.value)
            node = node.next

        self.assertEqual(list_of_values_same_instance, [5, 4, 3, 2], "Error during reversing the LinkedList instance.")
        self.assertEqual(list_of_values_object_copy, [5, 4, 3, 2], "Error during returns of reversed LinkedList copy.")
        self.assertFalse(list_of_values_object_copy is list_of_values_same_instance, "Get reversed does not return new instance.")


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


