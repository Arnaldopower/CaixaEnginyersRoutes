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
    
    


    for i in [2,4,5]:
        for j in [1,2,3,4]:
            open = [] #aqui li fotre l'inicial, a la funció el treiem però no el fiquem a close
            heapq.heapify(open)
            close = []
            graph = dataDict[i][j]
            for z in range(0,5):
                cost = 0
                open = [] #aqui li fotre l'inicial, a la funció el treiem però no el fiquem a close
                heapq.heapify(open)
                StarAlgorithm( ,graph)

def StarAlgorithm(node_inicial: node, graph: List[node]):
    while open:
        inici = heapq.heappop(open)
        for fill in inici.connections:
            



if __name__ == '__main__': 
    main()