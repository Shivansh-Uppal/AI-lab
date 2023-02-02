import networkx as nx
import matplotlib.pyplot as plt
tree= {
    '1': ['9','8'],
    '2': ['4','3'],
    '3': ['6','2'],
    '4': ['2'],
    '5': ['8','12'],
    '6': ['25','3','12'],
    '8': ['1','5'],
    '9': ['25','1'],
    '12': ['5','6'],
    '25': ['9','6']
}

stack=[]
visited=[]
print("\ndfs: ")

def visualize():
    G = nx.Graph(tree)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    plt.show()

def dfs(visited,tree,node):
    i=0
    visited.append(node)
    stack.append(node)
    while stack:
        s=stack.pop(i)
        i=i-1
        print(s,end=" ")

        for adjacent in tree[s]:
            if adjacent not in visited:
                visited.append(adjacent)
                stack.append(adjacent)
                i+=1

dfs(visited,tree,'1')
visualize()


