class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.visited = False

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def get_connections(self):
        return self.connected_to.keys()

    def __str__(self):
        connected_vertices = [connection.id for connection in self.connected_to]
        return f'{self.id} connected to {connected_vertices}'