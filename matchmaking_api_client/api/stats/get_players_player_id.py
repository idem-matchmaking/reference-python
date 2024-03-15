from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.player_statistics import PlayerStatistics
from ...types import Response


def _get_kwargs(
    player_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/players/{player_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PlayerStatistics]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PlayerStatistics.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PlayerStatistics]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    player_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[PlayerStatistics]:
    """Retrieve player statistics

    Args:
        player_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlayerStatistics]
    """

    kwargs = _get_kwargs(
        player_id=player_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    player_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[PlayerStatistics]:
    """Retrieve player statistics

    Args:
        player_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlayerStatistics
    """

    return sync_detailed(
        player_id=player_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    player_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[PlayerStatistics]:
    """Retrieve player statistics

    Args:
        player_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PlayerStatistics]
    """

    kwargs = _get_kwargs(
        player_id=player_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    player_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[PlayerStatistics]:
    """Retrieve player statistics

    Args:
        player_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PlayerStatistics
    """

    return (
        await asyncio_detailed(
            player_id=player_id,
            client=client,
        )
    ).parsed
