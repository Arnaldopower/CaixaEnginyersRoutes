from elements import node, getDirections
from loader import read_tsv

def main():
    data = read_tsv("input.tsv")
    dataDict = {j:{i:[] for i in [1,2,3,4]} for j in [2,4,5]}
    visited: set[node]
    for lot,bloc,comarca,cp,municipi,_,temps in data:
        dataDict[int(lot)][int(bloc)].append(node(municipi,cp.zfill(5),comarca,temps))
    with open("vertexs.txt","a", encoding="utf-8") as f:
        for lot in dataDict.values():
            for bloc in lot.values():
                visited = set()
                for origin in bloc:
                    visited.add(origin)
                    for destiny in bloc:
                        if destiny in visited:
                            continue
                        else:
                            coordsO = origin.get_coords()
                            coordsD = destiny.get_coords()
                            lol = getDirections(f"{coordsO[0]},{coordsO[1]}", f"{coordsD[0]},{coordsD[1]}")
                            print(f"(({origin},{destiny}),{lol})")
                            f.write(f"(({origin},{destiny}),{lol})\n")

if __name__ == '__main__': 
    main()