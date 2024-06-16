from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.match_player import MatchPlayer


T = TypeVar("T", bound="Team")


@_attrs_define
class Team:
    """
    Attributes:
        players (List['MatchPlayer']):
    """

    players: List["MatchPlayer"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "players": players,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.match_player import MatchPlayer

        d = src_dict.copy()
        players = []
        _players = d.pop("players")
        for players_item_data in _players:
            players_item = MatchPlayer.from_dict(players_item_data)

            players.append(players_item)

        team = cls(
            players=players,
        )

        team.additional_properties = d
        return team

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
