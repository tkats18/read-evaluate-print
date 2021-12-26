from dataclasses import dataclass
from typing import Any, Dict, Optional

from command import Command, ICommandGenerator


class IInputParser:
    def parse(self, input_str: str) -> Command:
        pass


class IInputParserBuilder:
    def with_generator(
        self, prefix: str, generator: ICommandGenerator
    ) -> "IInputParserBuilder":
        pass

    def build(self) -> IInputParser:
        pass


##########################################


@dataclass
class InputParser:
    command_mapping: Dict[str, ICommandGenerator]

    def parse(self, input_str: str) -> Command:
        input_parts = input_str.split(" ")
        index = input_str.index(input_parts[1])
        return self.command_mapping[input_parts[1]].generate_command(
            input_str[index + len(input_parts[1]) + 1 :]
        )


class InputParserBuilder:
    def __init__(self, kwargs: Optional[Dict[str, Any]] = None):
        self.kwargs = kwargs or {}

    def with_generator(
        self, prefix: str, generator: ICommandGenerator
    ) -> "InputParserBuilder":
        self.kwargs.setdefault("generators", {})
        self.kwargs["generators"][prefix] = generator
        return self

    def build(self) -> InputParser:
        return InputParser(self.kwargs["generators"])
