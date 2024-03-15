from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_admin_season_reset_json_body_percentages_item import (
        PostAdminSeasonResetJsonBodyPercentagesItem,
    )


T = TypeVar("T", bound="PostAdminSeasonResetJsonBody")


@_attrs_define
class PostAdminSeasonResetJsonBody:
    """
    Attributes:
        season_name (Union[Unset, str]):
        season_start (Union[Unset, str]): datetime for the start of the season in isoformat
        percentages (Union[Unset, List['PostAdminSeasonResetJsonBodyPercentagesItem']]):
    """

    season_name: Union[Unset, str] = UNSET
    season_start: Union[Unset, str] = UNSET
    percentages: Union[
        Unset, List["PostAdminSeasonResetJsonBodyPercentagesItem"]
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        season_name = self.season_name
        season_start = self.season_start
        percentages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.percentages, Unset):
            percentages = []
            for percentages_item_data in self.percentages:
                percentages_item = percentages_item_data.to_dict()

                percentages.append(percentages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if season_name is not UNSET:
            field_dict["seasonName"] = season_name
        if season_start is not UNSET:
            field_dict["seasonStart"] = season_start
        if percentages is not UNSET:
            field_dict["percentages"] = percentages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.post_admin_season_reset_json_body_percentages_item import (
            PostAdminSeasonResetJsonBodyPercentagesItem,
        )

        d = src_dict.copy()
        season_name = d.pop("seasonName", UNSET)

        season_start = d.pop("seasonStart", UNSET)

        percentages = []
        _percentages = d.pop("percentages", UNSET)
        for percentages_item_data in _percentages or []:
            percentages_item = PostAdminSeasonResetJsonBodyPercentagesItem.from_dict(
                percentages_item_data
            )

            percentages.append(percentages_item)

        post_admin_season_reset_json_body = cls(
            season_name=season_name,
            season_start=season_start,
            percentages=percentages,
        )

        post_admin_season_reset_json_body.additional_properties = d
        return post_admin_season_reset_json_body

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
