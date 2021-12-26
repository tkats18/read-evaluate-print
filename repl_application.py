from typing import Protocol

from channel_storage import ChannelStorage
from observe import Observable, PublishNotification, SubscribeNotification
from subscription_storage import SubscriptionStorage
from user_storage import UserStorage


class IPublisherApplication(Protocol):
    def publish(self, channel: str) -> None:
        pass


class ISubscriberApplication(Protocol):
    def subscribe(self, user: str, channel: str) -> None:
        pass


class ReplApplication(Observable):

    def __init__(self, users: UserStorage, channels: ChannelStorage, subscriptions: SubscriptionStorage):
        super().__init__()
        self.users = users
        self.channels = channels
        self.subscriptions = subscriptions

    def publish(self, channel: str) -> None:
        if self.channels.get_channel_by_name(channel) is None:
            self.channels.add_channel(channel)

        channel_dto = self.channels.get_channel_by_name(channel)
        if channel_dto is not None:
            full_users = []
            subscriptions = self.subscriptions.get_channel_subscriptions(channel_dto)
            for i in subscriptions:
                user_dto = self.users.get_user_by_id(i.user_id)
                if user_dto is not None:
                    full_users.append(user_dto)
            self.notify_video_published(PublishNotification(self.channels.get_channel_by_name(channel), full_users))

    def subscribe(self, user: str, channel: str) -> None:
        if self.channels.get_channel_by_name(channel) is None:
            self.channels.add_channel(channel)

        if self.users.get_user_by_name(user) is None:
            self.users.add_user(user)

        channel_dto = self.channels.get_channel_by_name(channel)
        user_dto = self.users.get_user_by_name(user)

        if user_dto is not None and channel_dto is not None:
            self.subscriptions.add_subscription(user_dto, channel_dto)
            self.notify_user_subscribed(SubscribeNotification(channel_dto, user_dto))
