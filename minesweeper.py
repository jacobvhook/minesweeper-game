from minefield import MineField
from enum import Enum

class GameState(Enum):
    PLAYING = 0
    LOST = 1
    WON = 2

def main():
    width : int = 10
    height : int = 10
    num_mines : int = 5

    game_state : GameState = GameState.PLAYING

    minefield = MineField(width, height, num_mines)
    minefield.displayminefield()

    while game_state == GameState.PLAYING:
        xguess = int(input("Pick x coordinate "))
        yguess = int(input("Pick y coordinate "))

        found_a_mine = minefield.guessspot(xguess,yguess)
        if found_a_mine:
            game_state = GameState.LOST
        elif minefield.hidden_tiles == num_mines:
            game_state = GameState.WON

        minefield.displayminefield()
    if game_state == GameState.LOST:
        print('Sorry you lost!')
    elif game_state == GameState.WON:
        print('You Won!')
    minefield.displaywholeminefield()

if __name__ == '__main__':
    main()