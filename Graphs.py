class Graphs:
    def __init__(self):
        self.adj_list={}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        
        return False

    def add_edge(self, vertex, edge):
        if edge not in self.adj_list[vertex]:
            self.adj_list[vertex].append(edge)
            return True
        
        return False

    def remove_vertex(self, vertex):
        self.adj_list.pop(vertex)

        for key in self.adj_list.keys():
            if vertex in self.adj_list[key]:
                self.adj_list[key].remove(vertex)

    def remove_edge(self, edge):

        for key in self.adj_list.keys():
            if edge in self.adj_list[key]:
                self.adj_list[key].remove(edge)

    def print_graph(self):
        print("------------------------------------------")
        for vertex in self.adj_list:
            print(vertex, " : ", self.adj_list[vertex])
        print("------------------------------------------")


if __name__ == "__main__":

    my_graph=Graphs()

    my_graph.add_vertex('A')
    my_graph.add_vertex('B')
    my_graph.add_vertex('C')
    my_graph.add_vertex('D')
    my_graph.add_vertex('E')
    my_graph.add_vertex('F')

    my_graph.add_edge('A','B')
    my_graph.add_edge('A','C')
    my_graph.add_edge('C','B')
    my_graph.add_edge('C','D')
    my_graph.add_edge('D','E')
    my_graph.add_edge('D','A')
    my_graph.add_edge('C','F')
    my_graph.add_edge('F','E')
    my_graph.add_edge('E','A')

    my_graph.print_graph()

    my_graph.remove_vertex('A')
    my_graph.remove_edge('A')
    my_graph.print_graph()

