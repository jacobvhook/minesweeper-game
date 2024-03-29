# Models a potential spot for a mine
class Mine:
    def __init__(self, ismine : bool, x : int, y : int):
        self.ismine : bool =ismine
        self.neighbors : int = 0
        self.isVisible : bool = False
        self.isFlagged : bool = False
        self.x : int = x
        self.y : int = y
    
    def checkmine(self) -> bool:
        return self.ismine

    def setneighbors(self, neighbors : int) -> None:
        self.neighbors = neighbors
    
    def checkneighbors(self) -> int:
        return self.neighbors
    
    def makeVisible(self) -> None:
        self.isVisible = True
    
    def toggle_flag(self) -> bool:
        self.isFlagged = not self.isFlagged
        return self.isFlagged

    def display_partial(self) -> str:
        if self.isFlagged and not self.isVisible:
            return 'F'
        elif not self.isVisible:
            return '-'
        elif self.ismine:
            return 'X'
        else:
            return str(self.neighbors)
    
    def display_all(self) -> str:
        if self.ismine:
            return 'X'
        else:
            return str(self.neighbors)