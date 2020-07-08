# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    current_room=None
    inventory=[]
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return (F"Player's Name:{self.name}, Items:{self.inventory}")