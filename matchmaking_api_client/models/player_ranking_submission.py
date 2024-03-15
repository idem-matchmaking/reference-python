from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerRankingSubmission")


@_attrs_define
class PlayerRankingSubmission:
    """
    Attributes:
        player_id (Union[Unset, str]): ID of the player
        score (Union[Unset, float]): Independent of winning, score is a measure of single player performance
    """

    player_id: Union[Unset, str] = UNSET
    score: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        player_id = self.player_id

        score = self.score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if player_id is not UNSET:
            field_dict["playerId"] = player_id
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        player_id = d.pop("playerId", UNSET)

        score = d.pop("score", UNSET)

        player_ranking_submission = cls(
            player_id=player_id,
            score=score,
        )

        player_ranking_submission.additional_properties = d
        return player_ranking_submission

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
