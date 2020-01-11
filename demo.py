from graphviz import Digraph

# A simple example of making a small tree
def example_tree():
    u = Digraph('unix', filename='unix.gv',
                node_attr={'color': 'lightblue2', 'style': 'filled'})
    u.attr(size='2,2')
    u.edge('F1','F2',label='P1')
    u.edge('F2','F3',label='P2>100')
    u.edge('F2','F4',label='P2<100')
    u.edge('F1','F5',label='P3')
    u.edge('F1','F6',label='P4')
    u.view()

if __name__=='__main__':
    example_tree()
