from dataclasses import dataclass
from typing import List, Protocol, Set

from repl_dto import ChannelDTO, UserDTO
from repl_logger import LoggerType, log_repl_message


@dataclass
class PublishNotification:
    channel: ChannelDTO
    users: List[UserDTO]


@dataclass
class SubscribeNotification:
    channel: ChannelDTO
    users: UserDTO


class IPublishObserver(Protocol):
    def on_publish_event(self, notification: PublishNotification) -> None:
        pass


class ISubscribeObserver(Protocol):
    def on_subscribe_event(self, notification: SubscribeNotification) -> None:
        pass


class Observable:
    def __init__(self) -> None:
        self.publish_observers: Set[IPublishObserver] = set()
        self.subscribe_observers: Set[ISubscribeObserver] = set()

    def attach_publish_observer(self, observer: IPublishObserver) -> None:
        self.publish_observers.add(observer)

    def detach_publish_observer(self, observer: IPublishObserver) -> None:
        self.publish_observers.remove(observer)

    def attach_subscribe_observer(self, observer: ISubscribeObserver) -> None:
        self.subscribe_observers.add(observer)

    def detach_subscribe_observer(self, observer: ISubscribeObserver) -> None:
        self.subscribe_observers.remove(observer)

    def notify_video_published(self, notification: PublishNotification) -> None:
        for observer in self.publish_observers:
            observer.on_publish_event(notification)

    def notify_user_subscribed(self, notification: SubscribeNotification) -> None:
        for observer in self.subscribe_observers:
            observer.on_subscribe_event(notification)


class SubscribeNotificationPrinter:
    def __init__(self) -> None:
        pass

    def on_subscribe_event(self, notification: SubscribeNotification) -> None:
        log_repl_message(
            LoggerType.SUBSCRIBE,
            notification.users.name
            + " subscribed to "
            + notification.channel.channel_name,
        )


class PublishNotificationPrinter:
    def __init__(self) -> None:
        pass

    def on_publish_event(self, notification: PublishNotification) -> None:
        msg = "Notifying subscribers of " + notification.channel.channel_name + "\n"
        for i in notification.users:
            msg += "   " + i.name + "\n"

        log_repl_message(LoggerType.PUBLISH, msg)
