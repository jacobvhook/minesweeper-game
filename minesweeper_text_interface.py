from minesweeper_interface import Interface

class TextInterface(Interface):
    def pick_coordinates(self) -> tuple[int]:
        xguess = int(input("Pick x coordinate (-1 to toggle flagging): "))
        yguess = int(input("Pick y coordinate (-1 to toggle flagging): "))
        
        return (xguess, yguess)
    
    def display_board(self, board: list[list[str]]) -> None:
        if not board:
            return
        
        width = len(board[0])
        print('  ', end='')
        for xval in range(width):
            print(xval, end='')
        print('')
        print('  ', end='')
        for _ in range(width):
            print('_', end='')
        print('')

        yval = 0
        for row in board:
            print(f'{yval}|', end='')
            for entry in row:
                print(entry, end='')
            yval += 1
            print('')
    
    def display_flag_mode(self, flagging: bool) -> None:
        if flagging:
            print('Flagging mode on')
        else:
            print('Flagging mode off')
    
    def display_win(self) -> None:
        print('You won!')
    
    def display_loss(self) -> None:
        print('You lost!')