from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerStats")


@_attrs_define
class PlayerStats:
    """
    Attributes:
        player_id (Union[Unset, str]): ID of the player
        rating (Union[Unset, float]):
        rating_uncertainty (Union[Unset, float]):
        ranking_points (Union[Unset, float]):
        rating_delta_last_game (Union[Unset, float]):
        ranking_delta_last_game (Union[Unset, float]):
        wins (Union[Unset, int]):
        losses (Union[Unset, int]):
        matches_played (Union[Unset, int]):
        win_ratio (Union[Unset, float]):
        season_wins (Union[Unset, int]):
        season_losses (Union[Unset, int]):
        season_matches_played (Union[Unset, int]):
        total_wins (Union[Unset, int]):
        total_losses (Union[Unset, int]):
        total_matches_played (Union[Unset, int]):
        season (Union[Unset, str]):
    """

    player_id: Union[Unset, str] = UNSET
    rating: Union[Unset, float] = UNSET
    rating_uncertainty: Union[Unset, float] = UNSET
    ranking_points: Union[Unset, float] = UNSET
    rating_delta_last_game: Union[Unset, float] = UNSET
    ranking_delta_last_game: Union[Unset, float] = UNSET
    wins: Union[Unset, int] = UNSET
    losses: Union[Unset, int] = UNSET
    matches_played: Union[Unset, int] = UNSET
    win_ratio: Union[Unset, float] = UNSET
    season_wins: Union[Unset, int] = UNSET
    season_losses: Union[Unset, int] = UNSET
    season_matches_played: Union[Unset, int] = UNSET
    total_wins: Union[Unset, int] = UNSET
    total_losses: Union[Unset, int] = UNSET
    total_matches_played: Union[Unset, int] = UNSET
    season: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        player_id = self.player_id

        rating = self.rating

        rating_uncertainty = self.rating_uncertainty

        ranking_points = self.ranking_points

        rating_delta_last_game = self.rating_delta_last_game

        ranking_delta_last_game = self.ranking_delta_last_game

        wins = self.wins

        losses = self.losses

        matches_played = self.matches_played

        win_ratio = self.win_ratio

        season_wins = self.season_wins

        season_losses = self.season_losses

        season_matches_played = self.season_matches_played

        total_wins = self.total_wins

        total_losses = self.total_losses

        total_matches_played = self.total_matches_played

        season = self.season

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if player_id is not UNSET:
            field_dict["playerId"] = player_id
        if rating is not UNSET:
            field_dict["rating"] = rating
        if rating_uncertainty is not UNSET:
            field_dict["ratingUncertainty"] = rating_uncertainty
        if ranking_points is not UNSET:
            field_dict["rankingPoints"] = ranking_points
        if rating_delta_last_game is not UNSET:
            field_dict["ratingDeltaLastGame"] = rating_delta_last_game
        if ranking_delta_last_game is not UNSET:
            field_dict["rankingDeltaLastGame"] = ranking_delta_last_game
        if wins is not UNSET:
            field_dict["wins"] = wins
        if losses is not UNSET:
            field_dict["losses"] = losses
        if matches_played is not UNSET:
            field_dict["matchesPlayed"] = matches_played
        if win_ratio is not UNSET:
            field_dict["winRatio"] = win_ratio
        if season_wins is not UNSET:
            field_dict["seasonWins"] = season_wins
        if season_losses is not UNSET:
            field_dict["seasonLosses"] = season_losses
        if season_matches_played is not UNSET:
            field_dict["seasonMatchesPlayed"] = season_matches_played
        if total_wins is not UNSET:
            field_dict["totalWins"] = total_wins
        if total_losses is not UNSET:
            field_dict["totalLosses"] = total_losses
        if total_matches_played is not UNSET:
            field_dict["totalMatchesPlayed"] = total_matches_played
        if season is not UNSET:
            field_dict["season"] = season

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        player_id = d.pop("playerId", UNSET)

        rating = d.pop("rating", UNSET)

        rating_uncertainty = d.pop("ratingUncertainty", UNSET)

        ranking_points = d.pop("rankingPoints", UNSET)

        rating_delta_last_game = d.pop("ratingDeltaLastGame", UNSET)

        ranking_delta_last_game = d.pop("rankingDeltaLastGame", UNSET)

        wins = d.pop("wins", UNSET)

        losses = d.pop("losses", UNSET)

        matches_played = d.pop("matchesPlayed", UNSET)

        win_ratio = d.pop("winRatio", UNSET)

        season_wins = d.pop("seasonWins", UNSET)

        season_losses = d.pop("seasonLosses", UNSET)

        season_matches_played = d.pop("seasonMatchesPlayed", UNSET)

        total_wins = d.pop("totalWins", UNSET)

        total_losses = d.pop("totalLosses", UNSET)

        total_matches_played = d.pop("totalMatchesPlayed", UNSET)

        season = d.pop("season", UNSET)

        player_stats = cls(
            player_id=player_id,
            rating=rating,
            rating_uncertainty=rating_uncertainty,
            ranking_points=ranking_points,
            rating_delta_last_game=rating_delta_last_game,
            ranking_delta_last_game=ranking_delta_last_game,
            wins=wins,
            losses=losses,
            matches_played=matches_played,
            win_ratio=win_ratio,
            season_wins=season_wins,
            season_losses=season_losses,
            season_matches_played=season_matches_played,
            total_wins=total_wins,
            total_losses=total_losses,
            total_matches_played=total_matches_played,
            season=season,
        )

        player_stats.additional_properties = d
        return player_stats

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
