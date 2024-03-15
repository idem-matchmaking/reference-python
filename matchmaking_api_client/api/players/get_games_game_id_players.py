from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.player_state import PlayerState
from ...types import Response


def _get_kwargs(
    game_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/games/{game_id}/players",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["PlayerState"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PlayerState.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["PlayerState"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    game_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[List["PlayerState"]]:
    """Get a list of players

    Args:
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['PlayerState']]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    game_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["PlayerState"]]:
    """Get a list of players

    Args:
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['PlayerState']
    """

    return sync_detailed(
        game_id=game_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    game_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[List["PlayerState"]]:
    """Get a list of players

    Args:
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['PlayerState']]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["PlayerState"]]:
    """Get a list of players

    Args:
        game_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['PlayerState']
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            client=client,
        )
    ).parsed
