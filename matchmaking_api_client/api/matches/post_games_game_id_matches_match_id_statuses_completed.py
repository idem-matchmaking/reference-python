from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.match_ranking_result import MatchRankingResult
from ...models.match_ranking_submission import MatchRankingSubmission
from ...types import Response


def _get_kwargs(
    game_id: str,
    match_id: str,
    *,
    body: MatchRankingSubmission,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/games/{game_id}/matches/{match_id}/statuses/completed",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MatchRankingResult]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MatchRankingResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MatchRankingResult]:
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
    body: MatchRankingSubmission,
) -> Response[MatchRankingResult]:
    """Report completed match

    Args:
        game_id (str):
        match_id (str):
        body (MatchRankingSubmission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MatchRankingResult]
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


def sync(
    game_id: str,
    match_id: str,
    *,
    client: AuthenticatedClient,
    body: MatchRankingSubmission,
) -> Optional[MatchRankingResult]:
    """Report completed match

    Args:
        game_id (str):
        match_id (str):
        body (MatchRankingSubmission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MatchRankingResult
    """

    return sync_detailed(
        game_id=game_id,
        match_id=match_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    game_id: str,
    match_id: str,
    *,
    client: AuthenticatedClient,
    body: MatchRankingSubmission,
) -> Response[MatchRankingResult]:
    """Report completed match

    Args:
        game_id (str):
        match_id (str):
        body (MatchRankingSubmission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MatchRankingResult]
    """

    kwargs = _get_kwargs(
        game_id=game_id,
        match_id=match_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    game_id: str,
    match_id: str,
    *,
    client: AuthenticatedClient,
    body: MatchRankingSubmission,
) -> Optional[MatchRankingResult]:
    """Report completed match

    Args:
        game_id (str):
        match_id (str):
        body (MatchRankingSubmission):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MatchRankingResult
    """

    return (
        await asyncio_detailed(
            game_id=game_id,
            match_id=match_id,
            client=client,
            body=body,
        )
    ).parsed
