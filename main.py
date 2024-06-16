import logging
import random

from matchmaking_api_client.api.matches import post_games_game_id_matches as get_matches
from matchmaking_api_client.api.matches import (
    post_games_game_id_matches_match_id_statuses_completed as complete_match_api,
)
from matchmaking_api_client.api.matches import (
    post_games_game_id_matches_match_id_statuses_confirmed as confirm_match_api,
)
from matchmaking_api_client.api.players import (
    delete_games_game_id_players_player_id as remove_player_api,
)
from matchmaking_api_client.api.players import (
    get_games_game_id_players as get_players_api,
)
from matchmaking_api_client.api.players import post_games_game_id_players
from matchmaking_api_client.api.stats import (
    get_players_player_id as get_player_stats_api,
)
from matchmaking_api_client.models import (
    Match,
    MatchRankingSubmission,
    PartySubmission,
    PlayerRankingSubmission,
    PlayerState,
    PlayerSubmission,
    TeamRankingSubmission,
)

from config import GAME_ID, get_client

logger = logging.getLogger(__name__)


def add_player(player_id: str):
    """Enqueue a player with the given player_id"""
    # A party submission enables enqueuing multiple players that form a single party
    submission = PartySubmission(
        players=[
            # Player submission contains the player id and potentially additional compatibility info
            # such as acceptable game servers, as well player choices that influence rating.
            PlayerSubmission(
                player_id=player_id,
                reference=f"{player_id}_internal_id_{random.randint(100, 999)}",
                servers=[
                    "example-gameserver-1"
                ],  # Here, we only provide a single game server
            )
        ],
        party_name=player_id,  # Optionally, parties can have a name
    )
    submission.players[0].additional_properties["partitionHash"] = "example_partition_hash"
    response = post_games_game_id_players.sync_detailed(
        GAME_ID,
        client=get_client(),
        body=submission,
    )
    # The response for adding a player returns no payload
    if response.status_code == 204:
        print(f"Added player {player_id} to the matchmaking queue.")
    else:
        logger.warning(
            f"Adding player {player_id} failed with status code {response.status_code}."
        )


def remove_player(player_id: str):
    response = remove_player_api.sync_detailed(
        GAME_ID, player_id=player_id, client=get_client()
    )
    if response.status_code == 204:
        print(f"Removed player {player_id} from the matchmaking queue.")
    else:
        logger.warning(
            f"Removing player {player_id} failed with status code {response.status_code}."
        )


def get_players() -> list[PlayerState]:
    """Retrieve a list of players in the matchmaking process"""
    player_list: list[PlayerState] = get_players_api.sync(GAME_ID, client=get_client())
    player_info = (
        "\n  ".join(
            [f"Player: {item.player_id} in status {item.state}" for item in player_list]
        )
        or "No players in matchmaking"
    )
    print(f"Players in matchmaking:\n  {player_info}")
    return player_list


def get_suggested_matches() -> list[Match]:
    """Retrieve match suggestions from the matchmaking API"""
    matches_response = get_matches.sync_detailed(GAME_ID, client=get_client())
    suggested_matches: list[Match] = matches_response.parsed

    # print some info about suggested matches
    match_infos = []
    for match in suggested_matches:
        player_info = ", ".join(
            [player.player_id for team in match.teams for player in team.players]
        )
        match_infos.append(f"Match: {match.uuid} with players {player_info}")
    match_summary = "\n  ".join(match_infos) if match_infos else "No suggested matches"
    print(f"Suggested matches:\n  {match_summary}")

    return suggested_matches


def update_match_confirmed(match_id: str):
    """Once a match is created, confirm the process to remove containing players from the queue"""
    response = confirm_match_api.sync_detailed(GAME_ID, match_id, client=get_client())
    # The response for confirming a match returns no payload
    if response.status_code == 204:
        print(f"Confirmed match {match_id}.")
    else:
        logger.warning(f"Failed confirming match {match_id}.")


def update_match_completed(match_id: str, winning_player: str, losing_player: str):
    """
    Once a match has ended, report the game result information
    to update player stats, including rating and ranking
    """
    # A match ranking submission contains all match-related info relevant for the player stats
    game_result = MatchRankingSubmission(
        server="example-gameserver-1",  # the game server the match was played on
        game_length=302,  # game duration in seconds
        teams=[
            # each team in the game shares a team ranking submission with a shared rank
            TeamRankingSubmission(
                rank=0,  # Rank begins with 0 for the winning team
                # Each player has their own player ranking submission which contains a score
                # as well as potentially additional information that is relevant for the player stats.
                players=[
                    PlayerRankingSubmission(
                        player_id=winning_player,
                        score=3219,
                    )
                ],
            ),
            TeamRankingSubmission(
                rank=1,  # the rank increases per team until it reaches its maximum for the worst team
                players=[
                    PlayerRankingSubmission(
                        player_id=losing_player,
                        score=2817,
                    )
                ],
            ),
        ],
    )
    ranking_result = complete_match_api.sync(
        GAME_ID, match_id, client=get_client(), body=game_result
    )
    # Print a small selection of player stats
    # For a full list of player stats, look at matchmaking_api_client/models/player_stats.py
    print("Player stat updates:")
    for player in ranking_result.players:
        print(
            f"""Player {player.player_id}:
        # of games played: {player.total_matches_played}, # won: {player.wins}
        new rating: {player.rating}, rating change: {player.rating_delta_last_game},
        new ranking: {player.ranking_points}
        """
        )


def get_player_stats(player_id: str):
    """Retrieve player statistics"""
    response = get_player_stats_api.sync_detailed(player_id, client=get_client())
    if response.status_code == 200:
        player_stats = response.parsed
        print(
            f"""Player {player_id} stats:
        # of games played: {player_stats.total_matches_played}, # won: {player_stats.total_wins}
        """
        )
    else:
        print(
            f"Failed to retrieve player stats for {player_id}. Status code {response.status_code}."
        )


def wait_for_user():
    input("Press Enter to continue")


def main():
    # Run a sample process

    print("At the beginning, the player queue is empty")
    online_players = get_players()
    if online_players:
        print("Well, let's remove all players and try again.")
        for player in online_players:
            remove_player(player.player_id)
        get_players()
    wait_for_user()
    print("We now add a player")
    add_player("player_1")
    print("Now, a single player is in the queue")
    get_players()
    wait_for_user()
    print("We add another player")
    add_player("player_2")
    print("Now, two players are in the queue")
    get_players()
    wait_for_user()
    print("We retrieve match suggestions")
    suggested_matches = get_suggested_matches()

    for suggested_match in suggested_matches:
        wait_for_user()
        print("After having successfully created the match, we confirm the match")
        update_match_confirmed(suggested_match.uuid)
        print("We wait for the match to complete")
        wait_for_user()
        print(
            "After the match has completed, we send game reports and receive updated player stats"
        )
        # randomize the winner
        players = [
            suggested_match.teams[0].players[0],
            suggested_match.teams[1].players[0],
        ]
        players = random.sample(players, k=2)
        winning_player = players.pop()
        losing_player = players.pop()
        update_match_completed(
            suggested_match.uuid, winning_player.player_id, losing_player.player_id
        )

        print("Now, let's retrieve the updated player stats")
        wait_for_user()
        for player in [winning_player, losing_player]:
            get_player_stats(player.player_id)

    print("This concludes our short tour. Thank you for your time.")


if __name__ == "__main__":
    main()
