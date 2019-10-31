import unittest

from algorithms.graphs import GraphDict


class TestGraphDict(unittest.TestCase):
    """
    Note, these are only smoke tests.
    """

    def setUp(self):
        """
        self.graph:
        
            Homer -> Marge -> Patty
              |        |       |^
              |        |       v|
              |        +----> Selma -> Fat Tony
              |                         ^
              |                         |
              +-> Bart -> Krusty -> Mr. Teeny
        
        self.graph2:
        
            Homer -> Lisa -> Sherry
              |      |^        |
              |      || +------+
              |      v| v
              + ---> Bart <=> Terry
        """
        self.graph_raw = {
            'Homer': {'Marge', 'Bart'},
            'Marge': {'Patty', 'Selma'},
            'Selma': {'Patty', 'Fat Tony'},
            'Patty': {'Selma'},

            'Bart': {'Krusty'},
            'Krusty': {'Mr. Teeny'},
            'Mr. Teeny': {'Fat Tony'},

            'Fat Tony': set()}
        self.graph = GraphDict(self.graph_raw)

        self.graph_raw2 = {
            'Homer': {'Lisa', 'Bart'},
            'Lisa': {'Bart', 'Sherry'},
            'Bart': {'Lisa', 'Terry'},
            'Sherry': {'Bart'},
            'Terry': {'Bart'}}
        self.graph2 = GraphDict(self.graph_raw2)

    def test_init(self):
        pass

    def test_init_empty(self):
        graph_raw = {}
        graph = GraphDict(graph_raw)
        self.assertEqual(len(graph), len(graph_raw))
        self.assertEqual(str(graph), str(graph_raw))

    def test_init_invalid(self):
        graph = {'Homer': {'Marge'}}
        with self.assertRaises(ValueError):
            x = GraphDict(graph)

    def test_len(self):
        self.assertEqual(len(self.graph), len(self.graph_raw))

    def test_str(self):
        self.assertEqual(str(self.graph), str(self.graph_raw))

    def test_breadthfirst_traversal(self):
        valid_breadthfirst_traversals = [
            ['Homer', 'Bart', 'Lisa', 'Terry', 'Sherry'],
            ['Homer', 'Lisa', 'Bart', 'Sherry', 'Terry']]
        visited = []
        def visitor(node):
            visited.append(node)
        # Invalid source.
        with self.assertRaises(ValueError):
            self.graph2.breadthfirst_traversal('Marge', visitor)
        visited.clear()
        # Standard.
        self.graph2.breadthfirst_traversal('Homer', visitor)
        self.assertIn(visited, valid_breadthfirst_traversals)

    def test_depthfirst_traversal(self):
        valid_depthfirst_traversals = [
            ['Homer', 'Lisa', 'Sherry', 'Bart', 'Terry'],
            ['Homer', 'Lisa', 'Bart', 'Terry', 'Sherry'],
            ['Homer', 'Bart', 'Terry', 'Lisa', 'Sherry'],
            ['Homer', 'Bart', 'Lisa', 'Sherry', 'Terry']]
        visited = []
        def visitor(node):
            visited.append(node)
        # Invalid source.
        with self.assertRaises(ValueError):
            self.graph2.depthfirst_traversal('Marge', visitor)
        visited.clear()
        # Standard.
        self.graph2.depthfirst_traversal('Homer', visitor)
        self.assertIn(visited, valid_depthfirst_traversals)

    def test_bidirectional_search(self):
        # Invalid source, invalid sink.
        with self.assertRaises(ValueError):
            self.graph.bidirectional_search('Lisa', 'Marge')
        with self.assertRaises(ValueError):
            self.graph.bidirectional_search('Marge', 'Lisa')
        # ['Homer', 'Marge'], simple.
        self.assertEqual(self.graph.bidirectional_search('Homer', 'Marge'),
                         ['Homer', 'Marge'])
        # ['Selma', 'Patty'], cycle doesn't mess this up.
        self.assertEqual(self.graph.bidirectional_search('Selma', 'Patty'),
                         ['Selma', 'Patty'])
        # ['Homer', 'Marge', 'Selma', 'Fat Tony'], not the longer path
        # ['Homer', 'Bart', 'Krusty', 'Mr. Teeny', 'Fat Tony'].
        self.assertEqual(self.graph.bidirectional_search('Homer', 'Fat Tony'),
                         ['Homer', 'Marge', 'Selma', 'Fat Tony'])
        # [], No paths from 'Fat Tony' to 'Homer'.
        self.assertEqual(self.graph.bidirectional_search('Fat Tony', 'Homer'),
                         [])
