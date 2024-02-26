from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def pick_coordinates(self) -> tuple[int]:
        pass

    @abstractmethod
    def display_board(self, board : list[list[str]]) -> None:
        pass

    @abstractmethod
    def display_flag_mode(self, flagging: bool) -> None:
        pass

    @abstractmethod
    def display_win(self) -> None:
        pass

    @abstractmethod
    def display_loss(self) -> None:
        pass