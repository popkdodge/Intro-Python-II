# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    """Define Player"""
    def __init__(self, name:str, room='outside'):
        self.name = name
        self.location = room

  