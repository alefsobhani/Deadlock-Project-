class Graph:
    def __init__(self):
        self.graph = {}

    def addedge(self, fromnode, tonode):
        if fromnode not in self.graph:
            self.graph[fromnode] = []
        self.graph[fromnode].append(tonode)

    def removeedge(self, fromnode, tonode):
        if fromnode in self.graph and tonode in self.graph[fromnode]:
            self.graph[fromnode].remove(tonode)

    def detectcycle(self):
        visited = set()
        recstack = set()

        def cycleutil(v):
            if v not in visited:
                visited.add(v)
                recstack.add(v)
                if v in self.graph:
                    for neighbor in self.graph[v]:
                        if neighbor not in visited and cycleutil(neighbor):
                            return True
                        elif neighbor in recstack:
                            return True
            recstack.remove(v)
            return False

        for node in list(self.graph):
            if cycleutil(node):
                return True
        return False

g = Graph()
g.addedge('P1', 'R1')
g.addedge('R1', 'P2')
g.addedge('P2', 'R2')
g.addedge('R2', 'P1')

if g.detectcycle():
    print("Deadlock detected")
else:
    print("No deadlock")
