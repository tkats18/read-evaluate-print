from dataclasses import dataclass


class CommandInputter:
    def get_line(self, index: int) -> str:
        pass

    def get_line_num(self) -> int:
        pass

    # ეს ეხლა რეალურად არ მჭირდება, მაგრამ კონსოლის ინფუთისთვის ამას
    # გამოვიყენებდი (ამის საჩვენებლად დავწერე).
    def get_next_line(self) -> str:
        pass


class CommandStorageInputter:
    # TODO
    # storage: Storage
    def get_line(self, index: int) -> str:
        return ""

    def get_line_num(self) -> int:
        pass


# ეს უბრალოდ მაგალითისთვის რატო შეიძლებოდა ეს სტრატეგია საერთოდ
# პროდაქშენში დაჭირვებოდა ვინმეს
class CommandConsoleInputter:

    def get_next_line(self) -> str:
        pass


# ----------------------------------------------------------


class CommandInputStrategy:
    # storage, stringparser
    # inputer, stringParser
    commandInputter: CommandInputter

    def has_next_raw_command(self) -> bool:
        pass

    def get_next_raw_command(self) -> str:
        pass


@dataclass
class StorageInputStrategy(CommandInputStrategy):
    commandInputter: CommandInputter
    index: int = 0

    def has_next_raw_command(self) -> bool:
        return self.index < self.commandInputter.get_line_num()

    def get_next_raw_command(self) -> str:

        if not self.has_next_raw_command():
            raise IndexError()

        res = self.commandInputter.get_line(self.index)
        self.index += 1
        return res
