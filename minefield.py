from mine import Mine
from random import sample

# Models the field of mines
class MineField:
    def __init__(self,width,height,num_mines):
        self.width=width
        self.height=height
        self.total_size = self.width*self.height
        self.mines = sample(range(self.total_size), num_mines)
        #mines = [4, 10]
        self.minearray = [[Mine(_minefieldmath(x,y,self.width,self.mines),x,y) \
                      for x in range(self.width)] for y in range(self.height)]
        for minelist in self.minearray:
            for mine in minelist:
                mine.setneighbors(self._computeneighbors(mine.x,mine.y))

    # When you guess (x,y) we should make that spot visible and end game if mine
    # Return true if mine, false if not
    def guessspot(self,x,y):
        mine = self.minearray[y][x]
        mine.makeVisible()
        if mine.checkneighbors() == 0:
            self._revealneighbors(mine.x,mine.y)
        return mine.checkmine()

    def displayminefield(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.minearray[y][x].isVisible:
                    if self.minearray[y][x].checkmine(): # Note the y,x ordering. 
                        print('X', end='')
                    else:
                        print(self.minearray[y][x].checkneighbors(),end='')
                else:
                    print('-',end='')
            print('')

    def displaywholeminefield(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.minearray[y][x].checkmine(): # Note the y,x ordering. 
                    print('X', end='')
                else:
                    print(self.minearray[y][x].checkneighbors(),end='')
            print('')

    def _getneighbors(self,x,y):
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

    def _computeneighbors(self, x, y):
        if self.minearray[y][x].checkmine():
            return -1
        
        num_neighbors_are_mines = 0
        neighbors = self._getneighbors(x,y)
        for neighbor in neighbors:
            if neighbor.checkmine():
                num_neighbors_are_mines += 1
        return num_neighbors_are_mines
    
    # If you get a zero then you should reveal neighbors
    def _revealneighbors(self,x,y):
        neighbors = self._getneighbors(x,y)
        for neighbor in neighbors:
            if not neighbor.isVisible:
                neighbor.makeVisible()
                if neighbor.checkneighbors() == 0:
                    self._revealneighbors(neighbor.x,neighbor.y)

    
def _minefieldmath(x, y, width,mines):
    return x + width * y in mines