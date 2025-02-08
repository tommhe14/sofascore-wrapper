from .api import SofascoreAPI
import datetime
from typing import Optional, Dict, Any
from pathlib import Path
import json

class Transfers:
    ENUMS_PATH = Path(__file__).parent / "tools" / "enums.json"

    with open(ENUMS_PATH, "r", encoding="utf-8") as file:
        ENUMS = json.load(file)

    def __init__(self, api: SofascoreAPI):
        self.api = api
        self.enums = self.ENUMS

    async def get_transfer_feed(
            self,
            page: int = 1,
            sort_by: str = "transferdate", 
            min_age: int = 15,
            max_age: int = 50,
            nationality: Optional[str] = None,
            unique_tournament_id: Optional[int] = None,
            position: Optional[str] = None,
            followers_count: Optional[int] = None,
        ):
            """
            Fetches the transfer feed from Sofascore API with optional filters.

            Args:
                page (int): Page number for pagination (default=1).
                sort_by (str): Sorting method ("followers", "transferfee", "transferdate").
                min_age (int): Minimum player age (default=15, max=50).
                max_age (int): Maximum player age (default=50, min=15).
                nationality (Optional[str]): Filter by nationality code (e.g., 'DZA' for Algeria).
                unique_tournament_id (Optional[int]): Filter by league/tournament ID.
                position (Optional[str]): Filter by player position ('FW', 'MF', 'DF', 'GK').
                followers_count (Optional[int]): Minimum followers count (max=1000).

            Returns:
                Dict: The API response containing transfer feed data.
            """
            sort_mapping = {
                "followers": "-userCount",
                "transferfee": "-transferFee",
                "transferdate": "-transferDate"
            }
            sort_by = sort_mapping.get(sort_by.lower())
            if not sort_by:
                raise ValueError(f"Invalid sort_by value: Must be one of {list(sort_mapping.keys())}")

            min_age = max(15, min(50, min_age))
            max_age = max(15, min(50, max_age))

            if followers_count is not None:
                followers_count = min(1000, max(0, followers_count))

            valid_positions = {"FW", "MF", "DF", "GK"}
            if position:
                position = position.upper()
                if position not in valid_positions:
                    raise ValueError(f"Invalid position: {position}. Must be one of {valid_positions}")

            query_params = [f"page={page}", f"sort={sort_by}", f"minAge={min_age}", f"maxAge={max_age}"]

            if nationality:
                query_params.append(f"nationality={nationality.upper()}")
            if unique_tournament_id:
                query_params.append(f"uniqueTournamentId={unique_tournament_id}")
            if position:
                query_params.append(f"position={position}")
            if followers_count:
                query_params.append(f"followersCount={followers_count}")

            request_url = f"/transfer?{'&'.join(query_params)}"

            return await self.api._get(request_url) 