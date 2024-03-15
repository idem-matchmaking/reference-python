from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerSubmission")


@_attrs_define
class PlayerSubmission:
    """
    Attributes:
        player_id (Union[Unset, str]): ID of the player
        servers (Union[Unset, List[str]]): The servers the player can be matched on
    """

    player_id: Union[Unset, str] = UNSET
    servers: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        player_id = self.player_id

        servers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.servers, Unset):
            servers = self.servers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if player_id is not UNSET:
            field_dict["playerId"] = player_id
        if servers is not UNSET:
            field_dict["servers"] = servers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        player_id = d.pop("playerId", UNSET)

        servers = cast(List[str], d.pop("servers", UNSET))

        player_submission = cls(
            player_id=player_id,
            servers=servers,
        )

        player_submission.additional_properties = d
        return player_submission

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
