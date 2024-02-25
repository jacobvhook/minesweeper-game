from minesweeper_game import MinesweeperGame
from minesweeper_text_interface import TextInterface
from minesweeper_settings import MinesweeperSettings

def main() -> None:
    interface : TextInterface = TextInterface()
    settings : MinesweeperSettings = MinesweeperSettings()
    game : MinesweeperGame = MinesweeperGame(interface, settings)

if __name__ == '__main__':
    main()
