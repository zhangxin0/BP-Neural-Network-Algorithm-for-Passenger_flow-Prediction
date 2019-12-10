from graphviz import Digraph

dot = Digraph(comment='NN Structure')
dot.node('A', 'X1')
dot.node('B', 'X2')
dot.node('L', 'X3')
dot.node('x4', 'X4')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
dot.render('test-output/NN Structure.gv', view=True)

