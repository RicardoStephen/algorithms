from collections import deque

class GraphDict:

    def __init__(self, graph):
        # TODO check the validity of the graph
        self.graph = graph
        for node in self.graph:
            for child in self.graph[node]:
                if child not in self.graph:
                    raise ValueError(f"{child} is not listed in the mappings.")

    def __len__(self):
        return len(self.graph)

    def __str__(self):
        return str(self.graph)

    def check_bidirectional(self):
        for node in self.graph:
            for child in self.graph[node]:
                if node not in self.graph[child]:
                    return (node, child)
        return None

    ############################################################################
    # Graph traversal
    ############################################################################
    def bfs(self, node, visit):
        frontier = deque([node])
        discovered = {node}
        while frontier:
            node = frontier.popleft()
            visit(node)
            for child in self.graph[node]:
                if child not in discovered:
                    frontier.append(child)
                    discovered.add(child)

    def dfs(self, node, visit):
        discovered = set()
        def dfs(node):
            discovered.add(node)
            for i in self.graph[node]:
                if i not in discovered:
                    dfs(i)
            visit(node)
        dfs(node)


if __name__ == '__main__':
    graph = {'homer': {'marge', 'smithers', 'lenny', 'krusty', 'hibert'},
             'marge': {'homer', 'patty', 'selma'},
             'smithers': {'monty', 'carl', 'homer'},
             'lenny': {'carl', 'homer', 'krusty'},
             'krusty': {'bob', 'lenny', 'homer'},
             'hibert': {'homer'},
             'selma': {'marge', 'patty'},
             'patty': {'selma', 'marge'},
             'monty': {'smithers'},
             'carl': {'smithers', 'lenny'},
             'bob': {'krusty'}}
    graph = GraphDict(graph)
    print(graph.check_bidirectional())
    print(graph)
    print(len(graph))
    print()

    # graph.bfs('homer', print)
    # print()
    # graph.dfs('homer', print)
    # print()

    pasta = {'buy ingredients': {'fry sausage', 'boil pasta', 'grate cheese'},
             'fry sausage': {'make sauce'},
             'boil pasta': {'assemble lasagnia'},
             'grate cheese': {'assemble lasagnia'},
             'make sauce': {'assemble lasagnia'},
             'assemble lasagnia': {'bake'},
             'bake': set()}
    pasta = GraphDict(pasta)
    print(pasta)
    print(len(pasta))
    print()

    pasta.bfs('buy ingredients', print)
