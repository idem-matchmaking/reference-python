""" Contains all the data models used in inputs/outputs """

from .match import Match
from .match_ranking_result import MatchRankingResult
from .match_ranking_submission import MatchRankingSubmission
from .party_submission import PartySubmission
from .player_ranking_submission import PlayerRankingSubmission
from .player_state import PlayerState
from .player_statistics import PlayerStatistics
from .player_statistics_seasons_item import PlayerStatisticsSeasonsItem
from .player_statistics_seasons_item_stats_item import (
    PlayerStatisticsSeasonsItemStatsItem,
)
from .player_stats import PlayerStats
from .player_status_enum import PlayerStatusEnum
from .player_submission import PlayerSubmission
from .post_admin_season_reset_body import PostAdminSeasonResetBody
from .post_admin_season_reset_body_percentages_item import (
    PostAdminSeasonResetBodyPercentagesItem,
)
from .post_games_game_id_matches_match_id_statuses_failed_body import (
    PostGamesGameIdMatchesMatchIdStatusesFailedBody,
)
from .team import Team
from .team_ranking_submission import TeamRankingSubmission

__all__ = (
    "Match",
    "MatchRankingResult",
    "MatchRankingSubmission",
    "PartySubmission",
    "PlayerRankingSubmission",
    "PlayerState",
    "PlayerStatistics",
    "PlayerStatisticsSeasonsItem",
    "PlayerStatisticsSeasonsItemStatsItem",
    "PlayerStats",
    "PlayerStatusEnum",
    "PlayerSubmission",
    "PostAdminSeasonResetBody",
    "PostAdminSeasonResetBodyPercentagesItem",
    "PostGamesGameIdMatchesMatchIdStatusesFailedBody",
    "Team",
    "TeamRankingSubmission",
)
