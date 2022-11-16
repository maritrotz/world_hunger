class User:
    """ A user in the world hunger app

    Attributes:
        name(str) : the person's name.
        
    """
    def __init__(self,name):
        self.name = name
        self.orders = 0 
        self.order_total = 0
        self.reward_points = 0
        self.countries = ['Yemen','Indonesia','Sierra Leone','Ecuador','Colombia']
        self.items = {'rice':15,'water':12,'beans':8,'corn':7,'chicken':19,'grain':5,'squash':9}
        
    