from dataclasses import dataclass
from typing import Protocol

from ChannelStorage import ChannelStorage
from SubscriptionStorage import SubscriptionStorage
from UserStorage import UserStorage


class IPublisherApplication(Protocol):
    def publish(self, channel: str):
        pass


class ISubscriberApplication(Protocol):
    def subscribe(self, user: str, channel: str):
        pass


@dataclass
class ReplApplication(IPublisherApplication, ISubscriberApplication):
    def __init__(self, users: UserStorage, channels: ChannelStorage, subscriptions: SubscriptionStorage):
        self.users = users
        self.channels = channels
        self.subscriptions = subscriptions

    def publish(self, channel: str):
        pass

    def subscribe(self, user: str, channel: str):
        pass
