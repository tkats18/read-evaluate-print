from dataclasses import dataclass

from input_parser import InputParser
from input_strategy import ICommandInputStrategy


@dataclass
class REPLSimulator:
    inputter: ICommandInputStrategy
    parser: InputParser

    def simulate(self):
        while self.inputter.has_next_command():
            current_input = self.inputter.get_next_line()
            command = self.parser.parse(current_input)
            command.execute()
