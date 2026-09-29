"""Graph algorithms. Graphs are adjacency dicts: {node: [neighbor, ...]} or,
for weighted graphs, {node: [(neighbor, weight), ...]}."""

import heapq
from collections import deque

from dsa.data_structures.union_find import UnionFind


def bfs(graph, start):
    """Return nodes in breadth-first order from start."""
    seen, order, queue = {start}, [], deque([start])
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph.get(node, ()):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return order


def dfs(graph, start):
    """Return nodes in depth-first (preorder) order from start."""
    seen, order, stack = set(), [], [start]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        order.append(node)
        # Reverse so neighbors are visited in listed order.
        for nxt in reversed(graph.get(node, ())):
            if nxt not in seen:
                stack.append(nxt)
    return order


def shortest_path_unweighted(graph, start, goal):
    """Return the shortest path as a list of nodes, or None if unreachable."""
    parent, queue = {start: None}, deque([start])
    while queue:
        node = queue.popleft()
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        for nxt in graph.get(node, ()):
            if nxt not in parent:
                parent[nxt] = node
                queue.append(nxt)
    return None


def dijkstra(graph, source):
    """Shortest distances from source for non-negative weights. O((V+E) log V)."""
    dist = {source: 0}
    heap = [(0, source)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for nxt, w in graph.get(node, ()):
            nd = d + w
            if nd < dist.get(nxt, float("inf")):
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))
    return dist


def topological_sort(graph):
    """Kahn's algorithm. Raises ValueError if the graph has a cycle."""
    indegree = {node: 0 for node in graph}
    for node in graph:
        for nxt in graph[node]:
            indegree[nxt] = indegree.get(nxt, 0) + 1
    queue = deque(n for n, d in indegree.items() if d == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph.get(node, ()):
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    if len(order) != len(indegree):
        raise ValueError("graph contains a cycle")
    return order


def has_cycle_directed(graph):
    """Detect a cycle in a directed graph using three-color DFS."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {}

    def visit(node):
        color[node] = GRAY
        for nxt in graph.get(node, ()):
            state = color.get(nxt, WHITE)
            if state == GRAY or (state == WHITE and visit(nxt)):
                return True
        color[node] = BLACK
        return False

    return any(color.get(n, WHITE) == WHITE and visit(n) for n in graph)


def kruskal_mst(num_nodes, edges):
    """Minimum spanning tree for nodes 0..n-1 and edges (u, v, weight).
    Returns (total_weight, chosen_edges)."""
    uf = UnionFind(num_nodes)
    total, chosen = 0, []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if uf.union(u, v):
            total += w
            chosen.append((u, v, w))
    return total, chosen


def count_islands(grid):
    """Count 4-connected groups of '1' cells in a 2D grid."""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen = set()
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in seen:
                count += 1
                stack = [(r, c)]
                seen.add((r, c))
                while stack:
                    cr, cc = stack.pop()
                    for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in seen:
                            seen.add((nr, nc))
                            stack.append((nr, nc))
    return count
