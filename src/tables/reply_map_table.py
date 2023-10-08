from typing import Optional

# noinspection PyProtectedMember
from deta.base import _Base as BaseType
from pydantic import BaseModel, ConfigDict


class ReplyRow(BaseModel):
    model_config = ConfigDict(frozen=True)

    original_chat_id: int
    original_msg_id: int


class ReplyMapTable:
    def __init__(self, base: BaseType):
        self.base = base

    def save(self, original_chat_id, forwarded_msg_id, original_msg_id):
        self.base.put(data={
            'original_chat_id': original_chat_id,
            'original_msg_id': original_msg_id,
        }, key=str(forwarded_msg_id))

    def get(self, key) -> Optional[ReplyRow]:
        data = self.base.get(str(key))
        if data is None:
            return None
        return ReplyRow(**data)
