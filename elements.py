import googlemaps
from datetime import datetime

class node():
    def __init__(self, municipi: str, comarca: str, bloc: int, estanciaMin: int):
        self.municipi = municipi
        self.comarca = comarca
        self.bloc = bloc
        self.estanciaMin = estanciaMin

    def get_mun(self):
        return self.municipi 
    def get_com(self):
        return self.comarca
    def get_bloc(self):
        return self.bloc
    def get_estanciaMin(self):
        return self.estanciaMin

def getDirections(origin: node, destiny: node):
    now = datetime.now()
    gmaps = googlemaps.Client(key='AIzaSyAoFEZk9cyUV2LPi-k89aQp8f8TGdl42n0')
    directions_result = gmaps.directions(origin.get_mun(),destiny.get_mun(),mode="transit",departure_time=now)
    print(directions_result)