import queue

from python.cracking_the_coding_interview.ch_04_trees_graphs.graph import Graph


def bfs(start, end):
    if start == end:
        return True

    q = queue.Queue()
    start.visited = True
    q.put(start)

    while q.not_empty:
        vertex = q.get()
        if vertex:
            for each in vertex.get_connections():
                if not each.visited:
                    if each == end:
                        return True
                    else:
                        q.put(each)
                    each.visited = True

    return False


def test_graph():
    graph = setup_test_graph()
    start = graph.get_vertex(0)
    end = graph.get_vertex(4)

    assert bfs(start, end) is True


def setup_test_graph():
    graph = Graph()
    for num in range(6):
        graph.add_vertex(num)

    print(graph.get_vertices())

    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 5, 2)
    graph.add_edge(1, 2, 4)
    graph.add_edge(2, 3, 9)
    graph.add_edge(3, 4, 7)
    graph.add_edge(3, 5, 3)
    graph.add_edge(4, 0, 1)
    graph.add_edge(5, 4, 8)
    graph.add_edge(5, 2, 1)

    for vertex in graph:
        for connection in vertex.get_connections():
            print(f"{vertex.get_id()} connected to {connection.get_id()}")

    return graph