import unittest
from BinaryTree import BinaryTree


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


