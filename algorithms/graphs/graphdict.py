from collections import deque

from algorithms.baseobject import BaseObject


class GraphDict(BaseObject):

    def __init__(self, graph):
        # Verify connections.
        for neighbors in graph.values():
            for node in neighbors:
                if node not in graph:
                    raise ValueError("Graph has connections to unknown nodes.")
        self.graph = graph
        # Build the transpose graph.
        self.transpose = {}
        for node in self.graph:
            self.transpose[node] = set()
        for node, connections in self.graph.items():
            for connection in connections:
                self.transpose[connection].add(node)

    def __len__(self):
        return len(self.graph)

    def __str__(self):
        return str(self.graph)

    def breadthfirst_traversal(self, source, visit):
        if source not in self.graph:
            raise ValueError("Node not found.")
        discovered = set([source])
        queue = deque([source])
        while queue:
            node = queue.popleft()
            visit(node)
            for neighbor in self.graph[node]:
                if neighbor not in discovered:
                    discovered.add(neighbor)
                    queue.append(neighbor)

    def depthfirst_traversal(self, source, visit):
        if source not in self.graph:
            raise ValueError("Node not found.")
        visited = set()
        def depthfirst_traversal(node):
            visit(node)
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    depthfirst_traversal(neighbor)
        depthfirst_traversal(source)

    def bidirectional_search(self, source, sink):
        if source not in self.graph or sink not in self.graph:
            raise ValueError("Node not found.")
        if source == sink:
            return [source]
        source_provenance = {source: None}
        sink_provenance = {sink: None}
        source_queue = deque([source])
        sink_queue = deque([sink])
        def bfs_one_level(graph, provenance, queue, provenance2):
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in provenance2:
                        return (node, neighbor)
                    if neighbor not in provenance:
                        provenance[neighbor] = node
                        queue.append(neighbor)
            return None
        def expand_bridge(bridge, source_provenance, sink_provenance):
            path = deque(bridge)
            while path[0] != source:
                path.appendleft(source_provenance[path[0]])
            while path[-1] != sink:
                path.append(sink_provenance[path[-1]])
            return list(path)
        while source_queue or sink_queue:
            bridge = bfs_one_level(self.graph, source_provenance, source_queue,
                                   sink_provenance)
            if bridge:
                return expand_bridge(bridge, source_provenance, sink_provenance)
            bridge = bfs_one_level(self.transpose, sink_provenance, sink_queue,
                                   source_provenance)
            if bridge:
                return expand_bridge((bridge[1], bridge[0]), source_provenance,
                                     sink_provenance)
        return []
