# Models a potential spot for a mine
class Mine:
    def __init__(self, ismine, x, y):
        self.ismine=ismine
        self.neighbors = 0
        self.isVisible = False
        self.x = x
        self.y = y
    
    def checkmine(self):
        return self.ismine

    def setneighbors(self, neighbors):
        self.neighbors=neighbors
    
    def checkneighbors(self):
        return self.neighbors
    
    def makeVisible(self):
        self.isVisible = True