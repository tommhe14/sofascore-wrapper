from .api import SofascoreAPI
import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path
import json

class AmericanFootball:
    ENUMS_PATH = Path(__file__).parent / "tools" / "enums.json"

    with open(ENUMS_PATH, "r", encoding="utf-8") as file:
        ENUMS = json.load(file)

    def __init__(self, api: SofascoreAPI):
        self.api = api
        self.enums = self.ENUMS

    async def total_matches(self) -> Dict[str, int]:
        """
        Retrieves the total count of today's e-sport matches and how many are currently live.

        Returns:
            Dict[str, int]: A dictionary containing two keys:
                - "live": The number of live e-sport matches.
                - "total": The total number of e-sport matches scheduled for today.

        Example Response:
            .. code-block:: json
            {
                "live": 8,
                "total": 16
            }
        """
        data = await self.api._get("/sport/0/event-count")
        return data.get("american-football", {})
    
    async def matches_by_date(self, sport: str = "american-football", date: str = None) -> Dict[str, Any]:
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
    
    async def categories(self) -> Dict[str, int]:
        """
        Retrieves all the american football categories such as NFL europa and USA.

        Returns:
            Dict[str, int]: A dictionary containing two keys:


        """
        return await self.api._get("/sport/american-football/categories")
    
    async def tournaments(self, category_id: int) -> Dict[str, int]:
        """
        Retrieves all tournaments for a selected esports category i.e NFL PRE SEASON.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/category/{category_id}/unique-tournaments")

    async def best_player_of_playoffs(self, team_id: int, tournament_id: int, season_id: int) -> int:
        """
        Retrieves the best players for the selected team, tournament and season.

        Args:
            tournament_id (int): The ID of the tournament id.

        Returns:
            Dict[str, int]: 

        """
        return await self.api._get(f"/team/{team_id}/unique-tournament/{tournament_id}/season/{season_id}/top-players/playoffs")
    
    
    async def season_games(self, tournament_id: int, season_id: int) -> Dict[str, int]:
        """
        Retrieves all matches for the selected tournament and season.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/unique-tournament/{tournament_id}/season/{season_id}/team-events/total")
    
    async def tournament_info(self, tournament_id: int, season_id: int) -> Dict[str, int]:
        """
        Retrieves the tournament info.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/unique-tournament/{tournament_id}/season/{season_id}/info")
    
    async def round_highlights(self, country_code: str, tournament_id: int, season_id: int, round: int) -> Dict[str, int]:
        """
        Retrieves highlights for the given round.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/sport-video-highlights/country/{country_code}/unique-tournament/{tournament_id}/season/{season_id}/round/{round}")

    async def team_seasons(self, team_id: int) -> Dict[str, int]:
        """
        Retrieves the seasons for a given american football team.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/team/{team_id}/standings/seasons")

    async def standings(self, tournament_id: int, season_id: int) -> Dict[str, int]:
        """
        Retrieves the current standings for the tournament and season.
        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/tournament/{tournament_id}/season/{season_id}/standings/total")

    async def team_near_games(self, team_id: int) -> Dict:
        """
        Retrieves the nearest games for the selected team.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/team/{team_id}/near-events")
    
    async def team_player_stats(self, team_id: int, league_id: int, season_id: int) -> Dict[str, Any]:
        """
        Retrieves a team's best players for a given season.
        Args:
            team_id (int): The ID of the tea,.
            league_id (int): The ID of the league (unique tournament).
            season_id (int): The ID of the season.

        Returns:
            Dict[str, Any]: A dictionary containing the team's best players stats.

        """
        return await self.api._get(f"/team/{team_id}/unique-tournament/{league_id}/season/{season_id}/player-statistics/regularSeason")
    
    async def player_stats(self, player_id: int, league_id: int, season_id: int) -> Dict[str, Any]:
        """
        Retrieves a player's statistics for a specific league and season.

        Args:
            player_id (int): The ID of the player.
            league_id (int): The ID of the league (unique tournament).
            season_id: (int): the ID of the season.

        Returns:
            Dict[str, Any]: A dictionary containing the player's season statistics, including points, rebounds, assists, and more.


        """
        return await self.api._get(f"/player/{player_id}/unique-tournament/{league_id}/season/{season_id}/statistics/regularSeason")
    
    

    
