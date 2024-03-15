from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_stats import PlayerStats


T = TypeVar("T", bound="MatchRankingResult")


@_attrs_define
class MatchRankingResult:
    """
    Attributes:
        players (Union[Unset, List['PlayerStats']]):
    """

    players: Union[Unset, List["PlayerStats"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        players: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.players, Unset):
            players = []
            for players_item_data in self.players:
                players_item = players_item_data.to_dict()
                players.append(players_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if players is not UNSET:
            field_dict["players"] = players

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player_stats import PlayerStats

        d = src_dict.copy()
        players = []
        _players = d.pop("players", UNSET)
        for players_item_data in _players or []:
            players_item = PlayerStats.from_dict(players_item_data)

            players.append(players_item)

        match_ranking_result = cls(
            players=players,
        )

        match_ranking_result.additional_properties = d
        return match_ranking_result

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
