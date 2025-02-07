from .api import SofascoreAPI
import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path
import json

class Esports:
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
        return data.get("esports", {})
    
    async def all_tournaments(self) -> Dict[str, int]:
        """
        Retrieves all the e-sport tournaments

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        Example Response:
            .. code-block:: json
            {
                "categories": [
                    {
                        "name": "DTM",
                        "slug": "dtm",
                        "sport": {
                            "name": "Motorsport",
                            "slug": "motorsport",
                            "id": 11
                        },
                    "priority": 1,
                    "uniqueStages": [
                        {
                            "name": "DTM",
                            "slug": "dtm",
                            "id": 10,
                            "primaryColorHex": "#0d2750",
                            "secondaryColorHex": "#99cfff"
                        }
                    ],
                        "id": 198,
                        "flag": "dtm"
                    },
        """
        return await self.api._get("/config/default-unique-tournaments/GB/esports")
    
    async def categories(self) -> Dict[str, int]:
        """
        Retrieves all the esports categories such as LoL, Counter-Strike.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        Example Response:
            .. code-block:: json
            {
                "categories": [
                    {
                        "name": "Counter Strike",
                        "slug": "csgo",
                        "sport": {
                            "name": "E-sports",
                            "slug": "esports",
                            "id": 72
                        },
                    "priority": 0,
                        "id": 1572,
                        "flag": "counter-strike"
                    },
        """
        return await self.api._get("/sport/esports/categories")
    
    async def matches_by_date(self, sport: str = "esports", date: str = None) -> Dict[str, Any]:
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
    
    async def tournaments(self, category_id: int) -> Dict[str, int]:
        """
        Retrieves all tournaments for a selected esports category i.e counter strike.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/category/{category_id}/unique-tournaments")
    
    async def tournament_seasons(self, tournament_id: int) -> Dict[str, int]:
        """
        Retrieves the tournament seasons.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/unique-tournament/{tournament_id}/seasons")
    
    async def tournament_info(self, tournament_id: int, season_id: int) -> Dict[str, int]:
        """
        Retrieves the tournament info.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/unique-tournaments/{tournament_id}/season/{season_id}/info")
    
    async def get_tournament(self, tournament_id: int) -> Dict[str, int]:
        """
        Retrieves the tournament.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/unique-tournaments/{tournament_id}")

    async def tournament_media(self, tournament_id: int) -> Dict[str, int]:
        """
        Retrieves the tournament media such as highlights and streams.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/unique-tournaments/{tournament_id}/media")

    async def featured_matches(self, tournament_id: int) -> Dict[str, int]:
        """
        Retrieves the tournament current featured matches.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/unique-tournaments/{tournament_id}/featured-events")

    async def tournament_cuptree(self, tournament_id: int, season_id: int) -> Dict[str, int]:
        """
        Retrieves the tournament current cup tree for the selected season.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/unique-tournaments/{tournament_id}/season/{season_id}/cuptrees")

    async def next_tournament_matches(self, tournament_id: int, season_id: int) -> Dict[str, int]:
        """
        Retrieves the next matches for the selected tournament and season.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/unique-tournaments/{tournament_id}/season/{season_id}/events/next/0")
    
    async def last_tournament_matches(self, tournament_id: int, season_id: int) -> Dict[str, int]:
        """
        Retrieves the last matches for the selected tournament and season.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/unique-tournaments/{tournament_id}/season/{season_id}/events/last/0")
    
    async def tournament_matches(self, tournament_id: int, season_id: int) -> Dict[str, int]:
        """
        Retrieves all matches for the selected tournament and season.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/unique-tournaments/{tournament_id}/season/{season_id}/events")

    async def get_match(self, match_id) -> Dict[str, int]:
        """
        Retrieves match info.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/event/{match_id}/esports-games")

    async def match_rounds(self, match_id) -> Dict[str, int]:
        """
        Retrieves further match info which cannot be pulled from match.get_match()

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/esports-game/{match_id}/rounds")
    
    async def lineups(self, match_id) -> Dict[str, int]:
        """
        Retrieves match lineups

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/esports-game/{match_id}/lineups")

    async def team_streaks(self, match_id) -> Dict[str, int]:
        """
        Retrieves team streaks for the selected match.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/esports-game/{match_id}/team-streaks")

    async def highlights(self, match_id) -> Dict[str, int]:
        """
        Retrieves the match highlights.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        """
        return await self.api._get(f"/esports-game/{match_id}/highlights")
    

    
    

    


    



