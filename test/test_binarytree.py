import unittest

from test import Utils
from algorithms.graphs.binarytree import BinaryTree


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.gen = Utils.intstr_generator()
        
        self.data = {}
        self.data['empty'] = []
        self.data['one'] = [next(self.gen)]
        self.data['two'] = [next(self.gen), None, next(self.gen)]
        self.data['two2'] = [next(self.gen), next(self.gen), None]
        self.data['three'] = [next(self.gen), next(self.gen), next(self.gen)]
        h4_tree = [next(self.gen) for _ in range(15)]
        for i in range(8):
            tree = h4_tree.copy()
            tree[7 + i] = None
            self.data['h4_hole_d3_' + str(i)] = tree
        for i in range(4):
            tree = h4_tree.copy()
            tree[3 + i] = None
            tree[2*(3 + i) + 1] = None
            tree[2*(3 + i) + 2] = None
            self.data['h4_hole_d2_' + str(i)] = tree
        self.trees = {}
        for state, data in self.data.items():
            self.trees[state] = BinaryTree(data)

    def check_traversal(self, traversal_method, data, ordering):
        ordered = list(filter(bool, map(data.__getitem__, ordering)))
        visited = []
        def visit(val):
            visited.append(val)
        traversal_method(visit)
        self.assertEqual(ordered, visited)

    def test_init(self):
        pass

    def test_len(self):
        for data, tree in zip(self.data.values(), self.trees.values()):
            with self.subTest(data = data, tree = tree):
                self.assertEqual(len(tree), len(data) - data.count(None))

    def test_str(self):
        for data, tree in zip(self.data.values(), self.trees.values()):
            with self.subTest(data = data, tree = tree):
                self.assertEqual(str(tree), str(data))

    def test_inorder(self):
        self.check_traversal(self.trees['empty'].inorder, self.data['empty'],
                             [])
        self.check_traversal(self.trees['one'].inorder, self.data['one'], [0])
        h2_inorder = [1, 0, 2]
        self.check_traversal(self.trees['two'].inorder, self.data['two'],
                             h2_inorder)
        self.check_traversal(self.trees['two2'].inorder, self.data['two2'],
                             h2_inorder)
        self.check_traversal(self.trees['three'].inorder, self.data['three'],
                             h2_inorder)

    def test_preorder(self):
        self.check_traversal(self.trees['empty'].preorder, self.data['empty'],
                             [])
        self.check_traversal(self.trees['one'].preorder, self.data['one'], [0])
        h2_preorder = [0, 1, 2]
        self.check_traversal(self.trees['two'].preorder, self.data['two'],
                             h2_preorder)
        self.check_traversal(self.trees['two2'].preorder, self.data['two2'],
                             h2_preorder)
        self.check_traversal(self.trees['three'].preorder, self.data['three'],
                             h2_preorder)

    def test_postorder(self):
        self.check_traversal(self.trees['empty'].postorder, self.data['empty'],
                             [])
        self.check_traversal(self.trees['one'].postorder, self.data['one'], [0])
        h2_postorder = [1, 2, 0]
        self.check_traversal(self.trees['two'].postorder, self.data['two'],
                             h2_postorder)
        self.check_traversal(self.trees['two2'].postorder, self.data['two2'],
                             h2_postorder)
        self.check_traversal(self.trees['three'].postorder, self.data['three'],
                             h2_postorder)
