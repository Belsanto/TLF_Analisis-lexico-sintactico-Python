# Definir la clase y las funciones para construir y visualizar el árbol de derivación.
import pydot

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __str__(self):
        return self.name

def build_tree(t):
    if isinstance(t, tuple):
        node = TreeNode(t[0])
        for child in t[1:]:
            node.add_child(build_tree(child))
        return node
    else:
        return TreeNode(str(t))

def draw_tree(node, graph=None, parent=None):
    if graph is None:
        graph = pydot.Dot(graph_type='digraph')

    current = pydot.Node(str(id(node)), label=node.name)
    graph.add_node(current)

    if parent:
        graph.add_edge(pydot.Edge(parent, current))

    for child in node.children:
        draw_tree(child, graph, current)

    return graph
