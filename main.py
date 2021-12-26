from channel_storage import ChannelStorage
from command import SubscribeCommandGenerator, PublishCommandGenerator
from command_storage import CommandStorage
from input_parser import InputParserBuilder
from input_strategy import CommandStorageInputStrategy
from observe import PublishNotificationPrinter, SubscribeNotificationPrinter
from repl_application import ReplApplication
from repl_simulator import REPLSimulator
from storage import IJsonStorageSystem
from subscription_storage import SubscriptionStorage
from user_storage import UserStorage

if __name__ == "__main__":

    command_repository = IJsonStorageSystem("./data/commands.json", False)
    user_storage = UserStorage(IJsonStorageSystem("./data/users.json", True))
    channel_storage = ChannelStorage(IJsonStorageSystem("./data/channels.json", True))
    subscription_storage = SubscriptionStorage(IJsonStorageSystem("./data/subscriptions.json", True))

    application = ReplApplication(user_storage, channel_storage, subscription_storage)
    application.attach_publish_observer(PublishNotificationPrinter())
    application.attach_subscribe_observer(SubscribeNotificationPrinter())

    # ახალი ქომანდის დამატება რო გვინდოდეს ერთი ხაზი ქვემოთ ერთი ხაზი ზემოთ, მერე იმპლემენტაციები და ვსო

    input_parser = InputParserBuilder() \
        .with_generator("subscribe", SubscribeCommandGenerator(application)) \
        .with_generator("publish", PublishCommandGenerator(application)) \
        .build()

    REPLSimulator(CommandStorageInputStrategy(CommandStorage(command_repository)), input_parser).simulate()
