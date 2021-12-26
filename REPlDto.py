from dataclasses import dataclass
from typing import List


#####################################
@dataclass
class DatabaseResponseObject:
    id: int
    data: str


@dataclass
class DatabaseInsertObject:
    data: str


#####################################
@dataclass
class AbstractDTO:
    id: int


@dataclass
class UserDTO(AbstractDTO):
    name: str


@dataclass
class ChannelDTO(AbstractDTO):
    channel_name: str


@dataclass
class SubscriptionDTO(AbstractDTO):
    channel_id: int
    user_id: int


@dataclass
class CommandDTO(AbstractDTO):
    command: str


#####################################
@dataclass
class ChannelSubscriptionsDTO(AbstractDTO):
    channel: ChannelDTO
    subscribers: List[UserDTO]


# ეს დიდად არ მჭირდება მარა იყოს, იმის საჩვენებლად რომ რო დაგვჭირდეს
# შეიძლება ესეც და შეილება იმიტომ რომ საბსქრიბშენები ჩენელებზე არაა
# მიბმული, ცალკეა ;)
@dataclass
class UserSubscriptionsDTO(AbstractDTO):
    user: UserDTO
    channels: List[ChannelDTO]
