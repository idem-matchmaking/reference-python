from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_ranking_submission import TeamRankingSubmission


T = TypeVar("T", bound="MatchRankingSubmission")


@_attrs_define
class MatchRankingSubmission:
    """
    Attributes:
        teams (List['TeamRankingSubmission']):
        server (Union[Unset, str]):
        game_length (Union[Unset, float]):
    """

    teams: List["TeamRankingSubmission"]
    server: Union[Unset, str] = UNSET
    game_length: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)

        server = self.server

        game_length = self.game_length

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "teams": teams,
            }
        )
        if server is not UNSET:
            field_dict["server"] = server
        if game_length is not UNSET:
            field_dict["gameLength"] = game_length

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_ranking_submission import TeamRankingSubmission

        d = src_dict.copy()
        teams = []
        _teams = d.pop("teams")
        for teams_item_data in _teams:
            teams_item = TeamRankingSubmission.from_dict(teams_item_data)

            teams.append(teams_item)

        server = d.pop("server", UNSET)

        game_length = d.pop("gameLength", UNSET)

        match_ranking_submission = cls(
            teams=teams,
            server=server,
            game_length=game_length,
        )

        match_ranking_submission.additional_properties = d
        return match_ranking_submission

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
