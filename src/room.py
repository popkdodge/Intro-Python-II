# Implement a class to hold room information. This should have name and
# description attributes.
from item import Items

class Room:
    def __init__(self, name, description, item=[]):
        self.name = name 
        self.descripiton = description
        self.n_to = ' '
        self.s_to = ' '
        self.e_to = ' '
        self.w_to = ' '
        self.item = item

    def add_item(self, item_name, item_desc):
        self.item.append(Items(item_name, item_desc))
        return f"{item_name} was was placed on the floor!"
    
    def remove_item(self, item_name):
        self.item = [item for item in self.item if item.name != item_name]
        return f"{item_name} was removed from the ground."


