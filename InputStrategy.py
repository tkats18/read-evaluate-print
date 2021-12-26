from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol

from CommandStorage import CommandStorage


class ICommandInputStrategy(Protocol):
    def get_next_line(self) -> str:
        pass

    def has_next_command(self) -> bool:
        pass


class BaseCommandInputStrategy(ICommandInputStrategy):
    @abstractmethod
    def get_next_line(self) -> str:
        pass

    @abstractmethod
    def has_next_command(self) -> bool:
        pass


# ეს უბრალოდ მაგალითისთვის რატო შეიძლებოდა ეს სტრატეგია საერთოდ
# პროდაქშენში დაჭირვებოდა ვინმეს
@dataclass
class CommandStorageInputStrategy(BaseCommandInputStrategy):
    storage: CommandStorage
    index: int = 0

    def get_next_line(self) -> str:
        if not self.has_next_command():
            raise IndexError()

        res = self.storage.get_command_by_index(self.index).command
        self.index += 1
        return res

    def has_next_command(self) -> bool:
        return self.index < self.storage.get_content_num()


class CommandConsoleInputStrategy(BaseCommandInputStrategy):
    has_next = True

    def get_next_line(self) -> str:
        if not self.has_next_command():
            raise IndexError()

        current_input = input()
        if current_input == "-1":
            self.has_next = False
        return current_input

    def has_next_command(self) -> bool:
        raise self.has_next
