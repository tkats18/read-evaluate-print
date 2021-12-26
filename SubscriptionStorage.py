from dataclasses import dataclass
from typing import List

from REPlDto import ChannelDTO, UserDTO, DatabaseResponseObject, \
    SubscriptionDTO, DatabaseInsertObject
from Storage import IRepository


@dataclass
class SubscriptionStorage:
    inner_storage: IRepository

    def get_channel_subscriptions(self, channel: ChannelDTO) -> List[SubscriptionDTO]:
        subscriptions = []
        db_response = self.inner_storage.get_all_content()
        for i in db_response:
            cur_subscription = self._to_representation(i)
            if cur_subscription.channel_id == channel.id:
                subscriptions.append(cur_subscription)
        return subscriptions

    def get_user_subscriptions(self, user: UserDTO) -> List[SubscriptionDTO]:
        subscriptions = []
        db_response = self.inner_storage.get_all_content()
        for i in db_response:
            cur_subscription = self._to_representation(i)
            if cur_subscription.user_id == user.id:
                subscriptions.append(cur_subscription)
        return subscriptions

    def add_subscription(self, user: UserDTO, channel: ChannelDTO) -> None:
        insert_object = DatabaseInsertObject(self._to_db_content(user,channel))
        self.inner_storage.add_item(insert_object)

    def _to_db_content(self, user: UserDTO, channel: ChannelDTO) -> str:
        return "user:" + str(user.id) + "-" + "channel:" + str(channel.id)

    def _to_representation(self, db_object: DatabaseResponseObject) -> SubscriptionDTO:
        user_channel = db_object.data.split("-")
        user = user_channel[0].split(":")
        channel = user_channel[1].split(":")
        return SubscriptionDTO(int(db_object.id), int(user[1]), int(channel[1]))