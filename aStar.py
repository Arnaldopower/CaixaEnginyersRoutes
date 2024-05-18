from elements import node, getDirections
from loader import read_tsv

def main():
    read_tsv("input.tsv")
    origin = node("BellPrat", "Anoia", 1, 30)
    destiny = node("El Bruc", "Anoia", 1, 30)
    getDirections(origin, destiny)

if __name__ == '__main__': 
    main()