from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerStatisticsSeasonsItemStatsItem")


@_attrs_define
class PlayerStatisticsSeasonsItemStatsItem:
    """
    Attributes:
        rating (Union[Unset, float]):
        rating_uncertainty (Union[Unset, float]):
        ranking_points (Union[Unset, float]):
        wins (Union[Unset, int]):
        losses (Union[Unset, int]):
        matches_played (Union[Unset, int]):
        win_ratio (Union[Unset, float]):
        mode (Union[Unset, str]):
    """

    rating: Union[Unset, float] = UNSET
    rating_uncertainty: Union[Unset, float] = UNSET
    ranking_points: Union[Unset, float] = UNSET
    wins: Union[Unset, int] = UNSET
    losses: Union[Unset, int] = UNSET
    matches_played: Union[Unset, int] = UNSET
    win_ratio: Union[Unset, float] = UNSET
    mode: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rating = self.rating

        rating_uncertainty = self.rating_uncertainty

        ranking_points = self.ranking_points

        wins = self.wins

        losses = self.losses

        matches_played = self.matches_played

        win_ratio = self.win_ratio

        mode = self.mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_uncertainty is not UNSET:
            field_dict["ratingUncertainty"] = rating_uncertainty
        if ranking_points is not UNSET:
            field_dict["rankingPoints"] = ranking_points
        if wins is not UNSET:
            field_dict["wins"] = wins
        if losses is not UNSET:
            field_dict["losses"] = losses
        if matches_played is not UNSET:
            field_dict["matchesPlayed"] = matches_played
        if win_ratio is not UNSET:
            field_dict["winRatio"] = win_ratio
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rating = d.pop("rating", UNSET)

        rating_uncertainty = d.pop("ratingUncertainty", UNSET)

        ranking_points = d.pop("rankingPoints", UNSET)

        wins = d.pop("wins", UNSET)

        losses = d.pop("losses", UNSET)

        matches_played = d.pop("matchesPlayed", UNSET)

        win_ratio = d.pop("winRatio", UNSET)

        mode = d.pop("mode", UNSET)

        player_statistics_seasons_item_stats_item = cls(
            rating=rating,
            rating_uncertainty=rating_uncertainty,
            ranking_points=ranking_points,
            wins=wins,
            losses=losses,
            matches_played=matches_played,
            win_ratio=win_ratio,
            mode=mode,
        )

        player_statistics_seasons_item_stats_item.additional_properties = d
        return player_statistics_seasons_item_stats_item

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
