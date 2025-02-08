from .api import SofascoreAPI
import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path
import json

class Tennis:
    ENUMS_PATH = Path(__file__).parent / "tools" / "enums.json"

    with open(ENUMS_PATH, "r", encoding="utf-8") as file:
        ENUMS = json.load(file)

    def __init__(self, api: SofascoreAPI):
        self.api = api
        self.enums = self.ENUMS

    async def total_matches(self) -> Dict[str, int]:
        """
        Retrieves the total count of today's tennis matches and how many are currently live.

        Returns:
            Dict[str, int]: A dictionary containing two keys:
                - "live": The number of live tennis matches.
                - "total": The total number of tennis matches scheduled for today.

        Example Response:
            .. code-block:: json
            {
                "live": 8,
                "total": 16
            }
        """
        data = await self.api._get("/sport/0/event-count")
        return data.get("tennis", {})
    
    async def all_tournaments(self, country_code: str) -> Dict[str, int]:
        """
        Retrieves all the tennis tournaments

        Returns:
            Dict[str, int]: A dictionary containing two keys:


        """
        return await self.api._get(f"/config/default-unique-tournaments/{country_code.upper()}/tennis")
    
    async def categories(self) -> Dict[str, int]:
        """
        Retrieves all the tennis categories such as the countries.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get("/sport/tennis/categories")
    
    async def matches_by_date(self, sport: str = "cricket", date: str = None) -> Dict[str, Any]:
        """
        Retrieves scheduled fixtures for a given sport on a specific date.

        Args:
            sport (str): The sport for which to retrieve fixtures. Available options include:
                - "football", "rugby", "cricket", "tennis", "mma", "motorsport", "darts", "snooker"
                - "cycling", "basketball", "table-tennis", "ice-hockey", "esports", "handball"
                - "volleyball", "baseball", "american-football", "futsal", "minifootball", "badminton"
                - "aussie-rules", "beach-volley", "waterpolo", "floorball", "bandy"
            
            date (str, optional): The date in "YYYY-MM-DD" format. If not provided, the current date is used.

        Returns:
            Dict[str, Any]: A dictionary containing fixture details for the specified sport and date, 
            including match details, teams, venue, and start time.

        Raises:
            ValueError: If the provided sport is not in the list of supported sports.

        """
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        sport_key = sport.lower().replace(' ', '-')
        
        if sport_key not in self.enums["sports"]:
            raise ValueError(f"Invalid sport: {sport_key}. Must be one of {list(self.enums['sports'].keys())}")
        
        endpoint = f"/sport/{sport_key}/scheduled-events/{date}"
        
        return await self.api._get(endpoint)
    
    async def season_games(self, tournament_id: int, season_id: int) -> Dict[str, int]:
        """
        Retrieves all matches for the selected tournament and season.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/unique-tournament/{tournament_id}/season/{season_id}/team-events/total")

    async def power_per_leg(self, match_id: int) -> Dict[str, int]:
        """
        Retrieves the power score per game(round) for the given match.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/event/{match_id}/tennis-power")

    async def point_by_point(self, match_id: int) -> Dict[str, int]:
        """
        Retrieves the point by point data for the given match.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/event/{match_id}/point-by-point")

    async def player_tournaments(self, player_id: int) -> Dict[str, int]:
        """
        Retrieves the point by point data for the given match.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/team/{player_id}/recent-unique-tournaments")

    async def player_performance(self, player_id: int) -> Dict[str, int]:
        """
        Retrieves the player performance.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/team/{player_id}/performance")

    async def player_next_matches(self, player_id: int) -> Dict[str, int]:
        """
        Retrieves the player's next matches.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/team/{player_id}/events/next/0")
    
    async def player_last_matches(self, player_id: int) -> Dict[str, int]:
        """
        Retrieves the player's last matches.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/team/{player_id}/events/last/0")
    
    async def player_image(self, player_id: int) -> Dict[str, int]:
        """
        Retrieves the player's image.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return f"https://img.sofascore.com/api/v1/team/{player_id}/image"
    






    
    
