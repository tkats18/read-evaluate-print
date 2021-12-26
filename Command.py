from abc import abstractmethod


class Command:

    @abstractmethod
    def execute(self):
        pass


class PublishCommand(Command):

    def execute(self):
        pass


class SubscribeCommand(Command):

    def execute(self):
        pass
