import googlemaps
from datetime import datetime
from classe import CordinateGetter

class node():
    def __init__(self, municipi:str, CP: str, comarca: str, estanciaMin: int):
        self.municipi = municipi 
        self.CP = CP
        self.comarca = comarca
        self.estanciaMin = estanciaMin
        self.connections = {}

    def get_mun(self):
        return self.municipi
    def get_com(self):
        return self.comarca
    def get_bloc(self):
        return self.bloc
    def get_estanciaMin(self):
        return self.estanciaMin
    def get_coords(self):
        return CordinateGetter.get_coordinates(self.CP)
    def set_connections(self, connections):
        for s,t in connections:
            if self.municipi in s:
                self.connections[next(l for l in s if l != self.municipi)] = t
        self.connections = dict(sorted(self.connections.items(), key=lambda item: item[1][0]))
    def __str__(self):
        return self.municipi

def getDirections(origin: node, destiny: node) -> tuple[int, int]:
    now = datetime.now()
    gmaps = googlemaps.Client(key='AIzaSyDrS4cmFMnWHhamFFudv6VlBJWcmjLvGCk')
    directions_result = gmaps.directions(origin,destiny,mode="driving",departure_time=now)
    return (directions_result[0]["legs"][0]["duration_in_traffic"]["value"], directions_result[0]["legs"][0]["distance"]["value"]) #value -> seconds / distance -> meters

