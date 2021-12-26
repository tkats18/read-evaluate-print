import re
from abc import abstractmethod
from dataclasses import dataclass
from typing import Protocol

from repl_application import IPublisherApplication, ISubscriberApplication


class Command:
    @abstractmethod
    def execute(self) -> None:
        pass


@dataclass
class PublishCommand(Command):
    application: IPublisherApplication
    channel: str

    def execute(self) -> None:
        self.application.publish(self.channel)


@dataclass
class SubscribeCommand(Command):
    application: ISubscriberApplication
    user: str
    channel: str

    def execute(self) -> None:
        self.application.subscribe(self.user, self.channel)


########################################


class ICommandGenerator(Protocol):
    def generate_command(self, input_command: str) -> Command:
        pass


class PublishCommandGenerator(ICommandGenerator):
    def __init__(self, application: IPublisherApplication):
        self.application = application

    def generate_command(self, input_command: str) -> Command:
        cut = list(filter(None, re.split("<(.*?)>", input_command)))
        return PublishCommand(self.application, cut[1])


class SubscribeCommandGenerator(ICommandGenerator):
    def __init__(self, application: ISubscriberApplication):
        self.application = application

    def generate_command(self, input_command: str) -> Command:
        cut = list(filter(None, re.split("<(.*?)>", input_command)))
        return SubscribeCommand(self.application, cut[0], cut[2])
