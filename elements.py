import googlemaps
from datetime import datetime

class node():
    def __init__(self, municipiCP: str, comarca: str, estanciaMin: int):
        self.municipiCP = municipiCP
        self.comarca = comarca
        self.estanciaMin = estanciaMin

    def get_munCP(self):
        return self.municipiCP
    def get_com(self):
        return self.comarca
    def get_bloc(self):
        return self.bloc
    def get_estanciaMin(self):
        return self.estanciaMin
    def __str__(self):
        return self.municipiCP

def getDirections(origin: node, destiny: node) -> tuple[int, int]:
    now = datetime.now()
    gmaps = googlemaps.Client(key='AIzaSyAoFEZk9cyUV2LPi-k89aQp8f8TGdl42n0')
    directions_result = gmaps.directions(origin.get_munCP(),destiny.get_munCP(),mode="driving",departure_time=now)
    return (directions_result[0]["legs"][0]["duration_in_traffic"]["value"], directions_result[0]["legs"][0]["distance"]["value"]) #value -> seconds / distance -> meters

