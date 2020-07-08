# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    n_to=None
    e_to=None
    s_to=None
    w_to=None
    items=[]
    def __init__(self,name,description):
        self.name=name
        self.description=description
    def __str__(self):
        return (F"{self.name}, {self.description}")