from mine import Mine
from random import sample

# Models the field of mines
class MineField:
    def __init__(self, width: int,height: int,num_mines: int):
        self.width : int = width
        self.height : int = height
        self.total_size : int = self.width*self.height
        self.mines : list[int] = sample(range(self.total_size), num_mines)
        self.hidden_tiles : int = self.total_size
        #mines = [4, 10]
        self.minearray : list[list[Mine]] = [[Mine(_minefieldmath(x,y,self.width,self.mines),x,y) \
                      for x in range(self.width)] for y in range(self.height)]
        for minelist in self.minearray:
            for mine in minelist:
                mine.setneighbors(self._computeneighbors(mine.x,mine.y))

    # When you guess (x,y) we should make that spot visible and end game if mine
    # Return true if mine, false if not
    def guessspot(self, x : int, y : int) -> bool:
        mine = self.minearray[y][x]
        mine.makeVisible()
        self.hidden_tiles -= 1
        if mine.checkneighbors() == 0:
            self._revealneighbors(mine.x,mine.y)
        return mine.checkmine()
    
    def flagspot(self, x : int, y : int) -> bool:
        mine = self.minearray[y][x]
        mine.toggle_flag()
        return mine.isFlagged
    
    def getminefield(self) -> list[list[str]]:
        return [[mine.display_partial() for mine in row] for row in self.minearray]
    
    def getwholeminefield(self) -> list[list[str]]:
        return [[mine.display_all() for mine in row] for row in self.minearray]

    def _getneighbors(self, x : int, y : int) -> list[Mine]:
        neighbors=[]
        xvals=[x]
        yvals=[y]
        if x > 0:
            xvals.append(x-1)
        if x < self.width-1:
            xvals.append(x+1)
        if y > 0:
            yvals.append(y-1)
        if y < self.height - 1:
            yvals.append(y+1)
        for x in xvals:
            for y in yvals:
                neighbors.append(self.minearray[y][x])
        return neighbors

    def _computeneighbors(self, x : int, y : int) -> int:
        if self.minearray[y][x].checkmine():
            return -1
        
        num_neighbors_are_mines = 0
        neighbors = self._getneighbors(x,y)
        for neighbor in neighbors:
            if neighbor.checkmine():
                num_neighbors_are_mines += 1
        return num_neighbors_are_mines
    
    # If you get a zero then you should reveal neighbors
    def _revealneighbors(self, x : int, y : int) -> None:
        neighbors = self._getneighbors(x,y)
        for neighbor in neighbors:
            if not neighbor.isVisible:
                neighbor.makeVisible()
                self.hidden_tiles -= 1
                if neighbor.checkneighbors() == 0:
                    self._revealneighbors(neighbor.x,neighbor.y)

    
def _minefieldmath(x : int, y : int, width : int, mines : list[int]) -> bool:
    return x + width * y in mines