from ChannelStorage import ChannelStorage
from Command import SubscribeCommandGenerator, PublishCommandGenerator
from CommandStorage import CommandStorage
from InputParser import InputParserBuilder
from InputStrategy import CommandStorageInputStrategy
from REPLApplication import ReplApplication
from REPLSimulator import REPLSimulator
from Storage import IJsonStorageSystem
from SubscriptionStorage import SubscriptionStorage
from UserStorage import UserStorage

if __name__ == "__main__":
    command_repository = IJsonStorageSystem("./data/commands.json")
    user_storage = UserStorage(IJsonStorageSystem("./data/users.json"))
    channel_storage = ChannelStorage(IJsonStorageSystem("./data/channels.json"))
    subscription_storage = SubscriptionStorage(IJsonStorageSystem("./data/subscriptions.json"))
    application = ReplApplication(user_storage, channel_storage, subscription_storage)

    input_parser = InputParserBuilder() \
        .with_generator("subscribe", SubscribeCommandGenerator(application)) \
        .with_generator("publish", PublishCommandGenerator(application)) \
        .build()

    REPLSimulator(CommandStorageInputStrategy(CommandStorage(command_repository)), input_parser).simulate()
