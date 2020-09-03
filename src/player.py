# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Items
class Player:
    """Define Player"""
    def __init__(self, name:str, room='outside'):
        self.name = name
        self.location = room
        self.inventory = []

    def add_item_to_inventory(self, item_name, item_description):
        self.inventory.append(Items(item_name, item_description))
    
