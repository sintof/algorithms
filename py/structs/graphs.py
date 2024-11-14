from utils.speed import timeit

@timeit
def dfs(node, graph, visited={}):
    visited = {node}
    print(node)

    for i in graph[node]:
        if i not in visited:
            visited.add(i)
            dfs(i, graph, visited)


@timeit
def dfs_iterative(node, graph):
    visited = {node}
    stack = [node]

    while stack:
        node = stack.pop()
        print(node)

        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                stack.append(i)


@timeit
def bfs(node, graph):
    visited = {node}
    queue = [node]

    while queue:
        node = queue.pop(0)
        print(node)

        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                queue.append(i)


def start():
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["f"],
        "e": [],
        "f": [],
    }

    dfs("a", graph)
    dfs_iterative("a", graph)
    bfs("a", graph)
