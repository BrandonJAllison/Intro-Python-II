#Writing a class to hold items
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f'{self.name}'
        