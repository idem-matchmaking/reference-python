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
        server (Union[Unset, str]):
        game_length (Union[Unset, float]):
        teams (Union[Unset, List['TeamRankingSubmission']]):
    """

    server: Union[Unset, str] = UNSET
    game_length: Union[Unset, float] = UNSET
    teams: Union[Unset, List["TeamRankingSubmission"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server = self.server

        game_length = self.game_length

        teams: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.teams, Unset):
            teams = []
            for teams_item_data in self.teams:
                teams_item = teams_item_data.to_dict()
                teams.append(teams_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server is not UNSET:
            field_dict["server"] = server
        if game_length is not UNSET:
            field_dict["gameLength"] = game_length
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.team_ranking_submission import TeamRankingSubmission

        d = src_dict.copy()
        server = d.pop("server", UNSET)

        game_length = d.pop("gameLength", UNSET)

        teams = []
        _teams = d.pop("teams", UNSET)
        for teams_item_data in _teams or []:
            teams_item = TeamRankingSubmission.from_dict(teams_item_data)

            teams.append(teams_item)

        match_ranking_submission = cls(
            server=server,
            game_length=game_length,
            teams=teams,
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
