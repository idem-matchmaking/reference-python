from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_statistics_seasons_item import PlayerStatisticsSeasonsItem


T = TypeVar("T", bound="PlayerStatistics")


@_attrs_define
class PlayerStatistics:
    """
    Attributes:
        player_id (Union[Unset, str]): ID of the player
        total_wins (Union[Unset, int]):
        total_losses (Union[Unset, int]):
        total_matches_played (Union[Unset, int]):
        seasons (Union[Unset, List['PlayerStatisticsSeasonsItem']]):
    """

    player_id: Union[Unset, str] = UNSET
    total_wins: Union[Unset, int] = UNSET
    total_losses: Union[Unset, int] = UNSET
    total_matches_played: Union[Unset, int] = UNSET
    seasons: Union[Unset, List["PlayerStatisticsSeasonsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        player_id = self.player_id

        total_wins = self.total_wins

        total_losses = self.total_losses

        total_matches_played = self.total_matches_played

        seasons: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.seasons, Unset):
            seasons = []
            for seasons_item_data in self.seasons:
                seasons_item = seasons_item_data.to_dict()
                seasons.append(seasons_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if player_id is not UNSET:
            field_dict["playerId"] = player_id
        if total_wins is not UNSET:
            field_dict["totalWins"] = total_wins
        if total_losses is not UNSET:
            field_dict["totalLosses"] = total_losses
        if total_matches_played is not UNSET:
            field_dict["totalMatchesPlayed"] = total_matches_played
        if seasons is not UNSET:
            field_dict["seasons"] = seasons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player_statistics_seasons_item import PlayerStatisticsSeasonsItem

        d = src_dict.copy()
        player_id = d.pop("playerId", UNSET)

        total_wins = d.pop("totalWins", UNSET)

        total_losses = d.pop("totalLosses", UNSET)

        total_matches_played = d.pop("totalMatchesPlayed", UNSET)

        seasons = []
        _seasons = d.pop("seasons", UNSET)
        for seasons_item_data in _seasons or []:
            seasons_item = PlayerStatisticsSeasonsItem.from_dict(seasons_item_data)

            seasons.append(seasons_item)

        player_statistics = cls(
            player_id=player_id,
            total_wins=total_wins,
            total_losses=total_losses,
            total_matches_played=total_matches_played,
            seasons=seasons,
        )

        player_statistics.additional_properties = d
        return player_statistics

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
