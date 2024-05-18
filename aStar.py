from elements import node, getDirections
from loader import read_tsv
from cp_conv import nie_to_cp

def main():
    data = read_tsv("input.tsv")
    dataDict = {j:{i:[] for i in [1,2,3,4]} for j in [2,4,5]}
    for lot,bloc,comarca,cp,municipi,_,temps in data:
        dataDict[int(lot)][int(bloc)].append(node(f"{nie_to_cp(cp.zfill(5))}, {municipi}",comarca,temps))
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
                            lol = getDirections(origin, destiny)
                            print(f"(({origin},{destiny}),{lol})")
                            f.write(f"(({origin},{destiny}),{lol})\n")

if __name__ == '__main__': 
    main()