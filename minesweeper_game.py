from minefield import MineField
from minesweeper_settings import MinesweeperSettings
from enum import Enum
from minesweeper_interface import Interface

class GameState(Enum):
    PLAYING = 0
    LOST = 1
    WON = 2

class MinesweeperGame:
    def __init__(self, interface : Interface, settings: MinesweeperSettings):
        self.interface : Interface = interface
        self.settings : MinesweeperSettings = settings

        self.width : int = self.settings.width
        self.height : int = self.settings.height
        self.num_mines : int = self.settings.num_mines
        self.game_state : GameState = GameState.PLAYING

        self.minefield : MineField = MineField(self.width, 
                                               self.height, 
                                               self.num_mines)
        self.flagging : bool = False
        
        self.display_minefield()

        while self.game_state == GameState.PLAYING:
            done_picking : bool = False
            while not done_picking:
                xguess , yguess = self.interface.pick_coordinates()
                if xguess == -1 and yguess == -1:
                    self.flagging = not self.flagging
                    self.display_flagging()
                elif not (xguess < 0 or yguess < 0 or 
                        xguess >= self.width or yguess >= self.height):
                    done_picking = True

            if self.flagging:
                self.minefield.flagspot(xguess, yguess)
            else:
                found_a_mine : bool = self.minefield.guessspot(xguess, yguess)
                if found_a_mine:
                    self.game_state = GameState.LOST
                elif self.minefield.hidden_tiles == self.num_mines:
                    self.game_state = GameState.WON
            
            self.display_minefield()
        
        if self.game_state == GameState.LOST:
            self.interface.display_loss()
        elif self.game_state == GameState.WON:
            self.interface.display_win()
        self.display_minefield(whole = True)
    

    def display_minefield(self, whole : bool = False) -> None:
        if whole:
            self.interface.display_board(self.minefield.getwholeminefield())
        else:
            self.display_flagging()
            self.interface.display_board(self.minefield.getminefield())
    
    def display_flagging(self) -> None:
        self.interface.display_flag_mode(self.flagging)


        



