from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerSubmission")


@_attrs_define
class PlayerSubmission:
    """
    Attributes:
        player_id (str): ID of the player
        servers (List[str]): The servers the player can be matched on
        reference (Union[Unset, str]): optional end-to-end reference set when adding the party
    """

    player_id: str
    servers: List[str]
    reference: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        player_id = self.player_id

        servers = self.servers

        reference = self.reference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "playerId": player_id,
                "servers": servers,
            }
        )
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        player_id = d.pop("playerId")

        servers = cast(List[str], d.pop("servers"))

        reference = d.pop("reference", UNSET)

        player_submission = cls(
            player_id=player_id,
            servers=servers,
            reference=reference,
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
