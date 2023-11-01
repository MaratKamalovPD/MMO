import networkx as nx
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')



feature_1 = ['104', '106', 'сортир', '101']
feature_2 = ['коридор 1', 'коридор 1', 'коридор 1', 'коридор 1']
score =     ['3', '4', '2', '5' ]
weight =     [3, 4, 2, 5]

df = pd.DataFrame({'f1': feature_1, 'f2': feature_2, 'score': score, 'weight': weight})

print(df)

G = nx.from_pandas_edgelist(df=df, source='f1', target='f2', edge_attr=['score','weight'])

#path = nx.shortest_path(G, '1', '10', weight='weight')
#print("shortest parth = " + str(path))
#length = nx.shortest_path_length(G, '1', '10', weight='weight')
#print("lenth of the shortest parth = " + str(length))

pos={
    "104":(50.1, 109.5),
    "106":(60.4,110.4),
    "коридор 1":(59.1,96.6),
    "сортир":(68.8,101.7),
    "101":(51.2,84.3),
}
datafile = 'FirstFloorPlan.png'
img = plt.imread(datafile)

plt.imshow(img, zorder=0, extent=[0.0, 327.0, 0.0, 135.0]) # (0, 0) - левый нижний угол, (327, 135) - правый верхний
nx.draw(G, pos, with_labels=True)
labels = {e: G.edges[e]['score'] for e in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()




