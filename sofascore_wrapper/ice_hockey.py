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
        Retrieves the total count of today's ice hockey matches and how many are currently live.

        Returns:
            Dict[str, int]: A dictionary containing two keys:
                - "live": The number of live ice hockey matches.
                - "total": The total number of ice hockey matches scheduled for today.

        Example Response:
            .. code-block:: json
            {
                "live": 8,
                "total": 16
            }
        """
        data = await self.api._get("/sport/0/event-count")
        return data.get("ice-hockey", {})
    
    async def all_tournaments(self, country_code: str = "GB") -> Dict[str, int]:
        """
        Retrieves all the ice hockey tournaments

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/config/default-unique-tournaments/{country_code.upper()}/ice-hockey")
    
    async def categories(self) -> Dict[str, int]:
        """
        Retrieves all the tennis categories such as the countries.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get("/sport/ice-hockey/categories")
    
    async def matches_by_date(self, sport: str = "ice-hockey", date: str = None) -> Dict[str, Any]:
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

    async def team_top_players(self, team_id: int, tournament_id: int, season_id: int) -> Dict[str, int]:
        """
        Retrieves the top players for the given team.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/team/{team_id}/unique-tournament/{tournament_id}/season/{season_id}/top-players/regularSeason")

    async def player_last_year_summary(self, player_id: int) -> Dict[str, int]:
        """
        Retrieves the players last year summary

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/player/{player_id}/last-year-summary")
    
    async def player_stats(self, player_id: int, league_id: int, season_id: int) -> Dict[str, Any]:
        """
        Retrieves a player's statistics for a specific league and season.

        Args:
            player_id (int): The ID of the player.
            league_id (int): The ID of the league (unique tournament).
            season_id (int): The ID of the season.

        Returns:
            Dict[str, Any]: A dictionary containing the player's season statistics, including points, rebounds, assists, and more.

        """
        return await self.api._get(f"/player/{player_id}/unique-tournament/{league_id}/season/{season_id}/statistics/regularSeason")

    async def player_shot_actions(self, player_id: int, league_id: int, season_id: int) -> Dict[str, Any]:
        """
        Retrieves a player's shot actions for a specific league and season.

        Args:
            player_id (int): The ID of the player.
            league_id (int): The ID of the league (unique tournament).
            season_id (int): The ID of the season.

        Returns:
            Dict[str, Any]: A dictionary containing the player's season statistics, including points, rebounds, assists, and more.


        """
        return await self.api._get(f"/player/{player_id}/unique-tournament/{league_id}/season/{season_id}/shot-actions/regularSeason")
    
    


    


    





    
    
