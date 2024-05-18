from elements import node, getDirections
from loader import read_tsv
from save_edges import load_edges
def main():
    data = read_tsv("input.tsv")
    dataDict = {j:{i:[] for i in [1,2,3,4]} for j in [2,4,5]}
    visited: set[node]
    edges = load_edges()
    for lot,bloc,comarca,cp,municipi,_,temps in data:
        nodo = node(municipi,cp.zfill(5),comarca,temps)
        nodo.set_connections(edges[int(lot)][int(bloc)])
        dataDict[int(lot)][int(bloc)].append(nodo)
    
    

if __name__ == '__main__': 
    main()