from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.player_statistics_seasons_item_stats_item import (
        PlayerStatisticsSeasonsItemStatsItem,
    )


T = TypeVar("T", bound="PlayerStatisticsSeasonsItem")


@_attrs_define
class PlayerStatisticsSeasonsItem:
    """
    Attributes:
        season (Union[Unset, str]):
        season_wins (Union[Unset, int]):
        season_losses (Union[Unset, int]):
        season_matches_played (Union[Unset, int]):
        stats (Union[Unset, List['PlayerStatisticsSeasonsItemStatsItem']]):
    """

    season: Union[Unset, str] = UNSET
    season_wins: Union[Unset, int] = UNSET
    season_losses: Union[Unset, int] = UNSET
    season_matches_played: Union[Unset, int] = UNSET
    stats: Union[Unset, List["PlayerStatisticsSeasonsItemStatsItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        season = self.season

        season_wins = self.season_wins

        season_losses = self.season_losses

        season_matches_played = self.season_matches_played

        stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if season is not UNSET:
            field_dict["season"] = season
        if season_wins is not UNSET:
            field_dict["seasonWins"] = season_wins
        if season_losses is not UNSET:
            field_dict["seasonLosses"] = season_losses
        if season_matches_played is not UNSET:
            field_dict["seasonMatchesPlayed"] = season_matches_played
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.player_statistics_seasons_item_stats_item import (
            PlayerStatisticsSeasonsItemStatsItem,
        )

        d = src_dict.copy()
        season = d.pop("season", UNSET)

        season_wins = d.pop("seasonWins", UNSET)

        season_losses = d.pop("seasonLosses", UNSET)

        season_matches_played = d.pop("seasonMatchesPlayed", UNSET)

        stats = []
        _stats = d.pop("stats", UNSET)
        for stats_item_data in _stats or []:
            stats_item = PlayerStatisticsSeasonsItemStatsItem.from_dict(stats_item_data)

            stats.append(stats_item)

        player_statistics_seasons_item = cls(
            season=season,
            season_wins=season_wins,
            season_losses=season_losses,
            season_matches_played=season_matches_played,
            stats=stats,
        )

        player_statistics_seasons_item.additional_properties = d
        return player_statistics_seasons_item

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
