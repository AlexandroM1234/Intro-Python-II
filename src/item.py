class Item:
    def __init__(self,name,description):
        self.name=name
        self.description=description
    def __str__(self):
        return(F"Item:{self.name}, Description:{self.description}")
    def on_drop(self):
        return (F"You have dropped {self.name}")
    def on_take(self):
        return (F"You have taken {self.name}")