from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_submission import PlayerSubmission


T = TypeVar("T", bound="PartySubmission")


@_attrs_define
class PartySubmission:
    """
    Attributes:
        players (List['PlayerSubmission']):
        party_name (Union[Unset, str]): Optional name of the party
    """

    players: List["PlayerSubmission"]
    party_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)

        party_name = self.party_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "players": players,
            }
        )
        if party_name is not UNSET:
            field_dict["partyName"] = party_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player_submission import PlayerSubmission

        d = src_dict.copy()
        players = []
        _players = d.pop("players")
        for players_item_data in _players:
            players_item = PlayerSubmission.from_dict(players_item_data)

            players.append(players_item)

        party_name = d.pop("partyName", UNSET)

        party_submission = cls(
            players=players,
            party_name=party_name,
        )

        party_submission.additional_properties = d
        return party_submission

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
