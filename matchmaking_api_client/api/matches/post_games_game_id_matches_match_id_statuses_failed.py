from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_games_game_id_matches_match_id_statuses_failed_body import (
    PostGamesGameIdMatchesMatchIdStatusesFailedBody,
)
from ...types import Response


def _get_kwargs(
    game_id: str,
    match_id: str,
    *,
    body: PostGamesGameIdMatchesMatchIdStatusesFailedBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/games/{game_id}/matches/{match_id}/statuses/failed",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: str,
    match_id: str,
    *,
    client: AuthenticatedClient,
    body: PostGamesGameIdMatchesMatchIdStatusesFailedBody,
) -> Response[Any]:
    """Report failed match creation

    Args:
        game_id (str):
        match_id (str):
        body (PostGamesGameIdMatchesMatchIdStatusesFailedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        match_id=match_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    game_id: str,
    match_id: str,
    *,
    client: AuthenticatedClient,
    body: PostGamesGameIdMatchesMatchIdStatusesFailedBody,
) -> Response[Any]:
    """Report failed match creation

    Args:
        game_id (str):
        match_id (str):
        body (PostGamesGameIdMatchesMatchIdStatusesFailedBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        match_id=match_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
