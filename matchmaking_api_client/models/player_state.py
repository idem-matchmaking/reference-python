from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.player_status_enum import PlayerStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerState")


@_attrs_define
class PlayerState:
    """
    Attributes:
        player_id (Union[Unset, str]): ID of the player
        state (Union[Unset, PlayerStatusEnum]):
    """

    player_id: Union[Unset, str] = UNSET
    state: Union[Unset, PlayerStatusEnum] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        player_id = self.player_id

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if player_id is not UNSET:
            field_dict["playerId"] = player_id
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        player_id = d.pop("playerId", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, PlayerStatusEnum]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PlayerStatusEnum(_state)

        player_state = cls(
            player_id=player_id,
            state=state,
        )

        player_state.additional_properties = d
        return player_state

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
