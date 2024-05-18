from elements import node, getDirections

def main():
    origin = node("BellPrat", "Anoia", 1, 30)
    destiny = node("El Bruc", "Anoia", 1, 30)
    getDirections(origin, destiny)

if __name__ == '__main__': 
    main()