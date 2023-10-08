
from typing import Any, Optional, cast

from aiogram.fsm.state import State
from aiogram.fsm.storage.base import BaseStorage, StateType, StorageKey
from deta import Deta


class DetaStateStorage(BaseStorage):
    def __init__(self, deta_project_key: str):
        self.deta_project_key = deta_project_key
        self.deta = Deta(self.deta_project_key)
        self.state_db = self.deta.Base("aiogram_state")
        self.data_db = self.deta.Base("aiogram_data")

    async def set_state(
            self, key: StorageKey, state: StateType = None,
    ) -> None:
        value = cast(str, state.state if isinstance(state, State) else state)
        key = str(key.user_id)
        self.state_db.put(data=value, key=key)

    async def get_state(self, key: StorageKey) -> Optional[str]:
        key = str(key.user_id)
        data = self.state_db.get(key)
        if data is None:
            return None
        value = data["value"]
        return cast(Optional[str], value)

    async def set_data(self, key: StorageKey, data: dict[str, 'Any']) -> None:
        key = str(key.user_id)
        self.data_db.put(data=data, key=key)

    async def get_data(self, key: StorageKey) -> dict[str, 'Any']:
        key = str(key.user_id)
        return self.data_db.get(key) or {}

    async def close(self) -> None:
        pass
