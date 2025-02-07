from .api import SofascoreAPI
import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path
import json

class MMA:
    ENUMS_PATH = Path(__file__).parent / "tools" / "enums.json"

    with open(ENUMS_PATH, "r", encoding="utf-8") as file:
        ENUMS = json.load(file)

    def __init__(self, api: SofascoreAPI):
        self.api = api
        self.enums = self.ENUMS

    async def total_fights(self) -> Dict[str, int]:
        """
        Retrieves the total count of today's basketball games and how many are currently live.

        Returns:
            Dict[str, int]: A dictionary containing two keys:
                - "live": The number of live basketball games.
                - "total": The total number of basketball games scheduled for today.

        Example Response:
            .. code-block:: json
            {
                "live": 21,
                "total": 270
            }
        """
        data = await self.api._get("/sport/0/event-count")
        return data.get("mma", {})


    async def live_fights(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Retrieve all currently live MMA events.

        Returns:
            Dict[str, List[Dict[str, Any]]]: A dictionary containing a list of live MMA events under the key "events".
            Each event is represented as a dictionary with details such as tournament, teams, scores, and match status.

        Example:
            The response follows this structure:

            .. code-block:: json

                {
                    "events": [
                        {
                            "fightType": "maincard",
                            "tournament": {
                                "name": "FS - MAT B - World OG Qualif.",
                                "slug": "fs-mat-b-world-og-qualif",
                                "category": {
                                    "name": "World",
                                    "slug": "world",
                                    "sport": {
                                        "name": "Mixed Martial Arts",
                                        "slug": "mma",
                                        "id": 76
                                    },
                                    "id": 1708,
                                    "flag": "international"
                                },
                                "id": 134691,
                                "startTimestamp": 1715414400,
                                "location": "Istanbul"
                            },
                            "season": {
                                "name": "FS - MAT B - World OG Qualif.",
                                "year": "2024",
                                "id": 63132
                            },
                            "status": {
                                "code": 58,
                                "description": "Awaiting announcement",
                                "type": "inprogress"
                            },
                            "homeTeam": {
                                "name": "Thomas John Mcglinchey BARNS",
                                "shortName": "T. J. M. BARNS",
                                "id": 528778,
                                "teamColors": {
                                    "primary": "#374df5",
                                    "secondary": "#374df5",
                                    "text": "#ffffff"
                                }
                            },
                            "awayTeam": {
                                "name": "Maxwell Lemar LACEY GARITA",
                                "shortName": "M. L. L. GARITA",
                                "id": 528779,
                                "teamColors": {
                                    "primary": "#374df5",
                                    "secondary": "#374df5",
                                    "text": "#ffffff"
                                }
                            },
                            "homeScore": {},
                            "awayScore": {},
                            "time": {
                                "current": 7,
                                "period1": 7,
                                "totalPeriodCount": 3
                            },
                            "id": 12490984,
                            "startTimestamp": 1715415495,
                            "slug": "maxwell-lemar-lacey-garita-thomas-john-mcglinchey-barns"
                        }
                    ]
                }
        """
        return await self.api._get("/sport/mma/events/live")

    async def fights_by_date(self, sport: str = "mma", date: str = None) -> Dict[str, Any]:
        """
        Retrieves scheduled fixtures for a given sport on a specific date.

        Args:
            sport (str): The sport for which to retrieve fixtures. Available options include:
                - "football", "rugby", "cricket", "tennis", "mma", "motorsport", "darts", "snooker"
                - "cycling", "basketball", "table-tennis", "ice-hockey", "e-sports", "handball"
                - "volleyball", "baseball", "american-football", "futsal", "minifootball", "badminton"
                - "aussie-rules", "beach-volley", "waterpolo", "floorball", "bandy"
            
            date (str, optional): The date in "YYYY-MM-DD" format. If not provided, the current date is used.

        Returns:
            Dict[str, Any]: A dictionary containing fixture details for the specified sport and date, 
            including match details, teams, venue, and start time.

        Raises:
            ValueError: If the provided sport is not in the list of supported sports.

        Example Response:
            .. code-block:: json

                {
                    "events": [
                        {
                            "venue": {
                                "city": {"name": "Sydney"},
                                "name": "Qudos Bank Arena",
                                "country": {"alpha2": "AU", "name": "Australia"}
                            },
                            "tournament": {
                                "name": "UFC 312: Du Plessis vs. Strickland 2",
                                "category": {"name": "World", "sport": {"name": "Mixed Martial Arts"}}
                            },
                            "homeTeam": {"name": "Aleksandre Topuria", "shortName": "A. Topuria"},
                            "awayTeam": {"name": "Colby Thicknesse", "shortName": "C. Thicknesse"},
                            "status": {"description": "Not started"},
                            "startTimestamp": 1739055600
                        }
                    ]
                }
        """
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        sport_key = sport.lower().replace(' ', '-')
        
        if sport_key not in self.enums["sports"]:
            raise ValueError(f"Invalid sport: {sport_key}. Must be one of {list(self.enums['sports'].keys())}")
        
        endpoint = f"/sport/{sport_key}/scheduled-events/{date}"
        
        return await self.api._get(endpoint)
    
    async def fighter_career_stats(self, fighter_id: int) -> Dict[str, int]:
        """
        Retrieves career statistics for a given fighter.

        Args:
            fighter_id (int): The ID of the fighter.

        Returns:
            Dict[str, int]: A dictionary containing the fighter's career statistics.

        Example Response:
            .. code-block:: json

                {
                    "issued": {
                        "strikes": {
                            "total": {
                                "landed": {
                                    "roundAvg": 46.64
                                }
                            },
                            "distance": {
                                "landed": {
                                    "roundAvg": 38.45,
                                    "roundPct": 82.5
                                }
                            },
                            "ground": {
                                "landed": {
                                    "roundAvg": 8.18,
                                    "roundPct": 17.5
                                }
                            }
                        },
                        "significantStrikes": {
                            "total": {
                                "landed": {
                                    "roundAvg": 20.27,
                                    "roundPct": 43.5
                                }
                            }
                        }
                    }
                }

        Example Usage:
            .. code-block:: python

                stats = await mma.fighter_career_stats(fighter_id=12345)
                print(stats["issued"]["strikes"]["total"]["landed"]["roundAvg"])  # Output: 46.64

        """
        return await self.api._get(f"/team/{fighter_id}/career-statistics")

    async def fighter_next_fights(self, fighter_id: int) -> List[Dict[str, Any]]:
        """
        Retrieves upcoming fights for a given fighter.

        Args:
            fighter_id (int): The ID of the fighter.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing details about upcoming fights, 
            including tournament, season, venue, teams, scores, and more.

        Example Response:
            .. code-block:: json

                {
                    "events": [
                        {
                            "venue": {
                                "city": { "name": "Sydney" },
                                "name": "Qudos Bank Arena",
                                "country": { "alpha2": "AU", "name": "Australia" }
                            },
                            "fightType": "maincard",
                            "weightClass": "middle",
                            "tournament": {
                                "name": "UFC 312: Du Plessis vs. Strickland 2",
                                "id": 144072,
                                "startTimestamp": 1739055600
                            },
                            "season": { "name": "UFC 312", "year": "2025" },
                            "status": { "description": "Not started", "type": "notstarted" },
                            "homeTeam": { "name": "Dricus Du Plessis", "id": 461874 },
                            "awayTeam": { "name": "Sean Strickland", "id": 461861 }
                        }
                    ],
                    "hasNextPage": false
                }

        Example Usage:
            .. code-block:: python

                upcoming_fights = await mma.fighter_next_fights(fighter_id=12345)
                print(upcoming_fights[0]["tournament"]["name"])  # Output: UFC 312: Du Plessis vs. Strickland 2

        """
        data = await self.api._get(f"/team/{fighter_id}/events/next/0")
        data["events"].reverse()
        return data["events"]


    async def fighter_last_fights(self, fighter_id: int) -> List[Dict[str, Any]]:
        """
        Retrieves previous fights for a given fighter.

        Args:
            fighter_id (int): The ID of the fighter.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing details about previous fights, 
            including tournament, season, venue, teams, scores, and more.

        Example Response:
            .. code-block:: json

                {
                    "events": [
                        {
                            "venue": {
                                "city": { "name": "Sydney" },
                                "name": "Qudos Bank Arena",
                                "country": { "alpha2": "AU", "name": "Australia" }
                            },
                            "fightType": "maincard",
                            "weightClass": "middle",
                            "tournament": {
                                "name": "UFC 312: Du Plessis vs. Strickland 2",
                                "id": 144072,
                                "startTimestamp": 1739055600
                            },
                            "season": { "name": "UFC 312", "year": "2025" },
                            "status": { "description": "Not started", "type": "notstarted" },
                            "homeTeam": { "name": "Dricus Du Plessis", "id": 461874 },
                            "awayTeam": { "name": "Sean Strickland", "id": 461861 }
                        }
                    ],
                    "hasNextPage": false
                }

        Example Usage:
            .. code-block:: python

                upcoming_fights = await mma.fighter_last_fights(fighter_id=12345)
                print(upcoming_fights[0]["tournament"]["name"])  # Output: UFC 312: Du Plessis vs. Strickland 2

        """
        data = await self.api._get(f"/team/{fighter_id}/events/last/0")
        data["events"].reverse()
        return data["events"]
    
    from typing import Any, Dict, List, Optional

    async def fighter_rankings(self, fighter_id: int) -> Optional[List[Dict[str, Any]]]:
        """
        Retrieves rankings and previous fights for a given fighter.

        Args:
            fighter_id (int): The ID of the fighter.

        Returns:
            Optional[List[Dict[str, Any]]]: A list of dictionaries containing details about previous fights, 
            including tournament, season, venue, teams, scores, and more. Returns `None` if no data is found.

        Example Usage:
            .. code-block:: python

                fighter_data = await mma.fighter_rankings(fighter_id=12345)
                if fighter_data:
                    print(fighter_data[0]["tournament"]["name"])  # Example Output: UFC 312: Du Plessis vs. Strickland 2
        """  
        return await self.api._get(f"/rankings/team/{fighter_id}")
    
    async def fighter_info(self, fighter_id: int) -> Optional[List[Dict[str, Any]]]:
        """
        Pulls info about the fighter

        Args:
            fighter_id (int): The ID of the fighter.

        Returns:
            Optional[List[Dict[str, Any]]]: A list of dictionaries containing details about previous fights, 
            including tournament, season, venue, teams, scores, and more. Returns `None` if no data is found.

        Example Usage:
            .. code-block:: python

                fighter_data = await mma.fighter_info(fighter_id=12345)
                if fighter_data:
                    print(fighter_data["team"]["name"])  # Example Output: Dricus Du Plessis
        """  
        return await self.api._get(f"/team/{fighter_id}")
    
    async def main_events_date(self, date: str = None) -> Optional[List[Dict[str, Any]]]:
        """
        Pulls MMA main events for the provided date, or today.

        Args:
            date (Optional) str: YYYY-MM-DD provided date.

        Returns:
            Optional[List[Dict[str, Any]]]: A list of dictionaries containing details about previous fights, 
            including tournament, season, venue, teams, scores, and more. Returns `None` if no data is found.

        Example Usage:
            .. code-block:: python

                fighter_data = await mma.main_events_date(date="2025-02-06")
        """  
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m-%d")

        return await self.api._get(f"/sport/mma/main-events/{date}/extended")

    async def main_events_month(self, organisation_id: int, date: str = None) -> Optional[List[Dict[str, Any]]]:
        """
        Pulls MMA main events for the provided month, or the current month.

        Args:
            date (Optional) str: YYYY-MM provided date.

        Returns:
            Optional[List[Dict[str, Any]]]: A list of dictionaries containing details about previous fights, 
            including tournament, season, venue, teams, scores, and more. Returns `None` if no data is found.

        Example Usage:
            .. code-block:: python

                fighter_data = await mma.main_events_month(date="2025-02")
        """  
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m")

        return await self.api._get(f"/unique-tournament/{organisation_id}/scheduled-mma-main-events/{date}")

    async def mma_tournaments(self) -> Optional[List[Dict[str, Any]]]:
        """
        Pulls active MMA tournaments such as UFC and BELLATOR.

        Returns:
            Optional[List[Dict[str, Any]]]: A list of dictionaries, 
            including tournament info

        Example Usage:
            .. code-block:: python

                fighter_data = await mma.mma_tournaments()
        """  
        return await self.api._get(f"/category/1708/unique-tournaments")

    async def mma_tournaments_months(self, tournament_id: int) -> Dict[str, Any]:
        """
        Pulls which months has fights for the provided tournament

        Returns:
            Optional[List[Dict[str, Any]]]: A list of dictionaries, 
            including tournament info

        Example Response:
            .. code-block:: python

                {
                    "monthsWithEvents": [
                        {
                            "month": 9,
                            "year": 2024
                        },
                ...

        Example Usage:
            .. code-block:: python

                fighter_data = await mma.mma_tournaments_months(19906)
        """  
        return await self.api._get(f"/calendar/unique-tournament/{tournament_id}/0/months-with-events")
    
    async def tournament_info(self, tournament_id: int) -> Dict:
        """
        Pulls info about the provided tournament

        Returns:
            Optional[List[Dict[str, Any]]]: A list of dictionaries, 
            including tournament info

        Example Usage:
            .. code-block:: python

                fighter_data = await mma.tournament_info(19906)
        """  
        return await self.api._get(f"/unique-tournament/{tournament_id}")

    async def fighter_image(self, fighter_id: int) -> Dict:
        """
        Returns the fighter image
        """  
        return f"https://img.sofascore.com/api/v1/team/{fighter_id}/image"

    async def tournament_image(self, tournament_id: int) -> Dict:
        """
        Returns the tournament image
        """  
        return f"https://img.sofascore.com/api/v1/unique-tournament/{tournament_id}/image/dark"
    
    async def ranking_summary(self, tournament_id: int) -> Dict:
        """
        Pulls the ranking summary for the chosen tournament

        Returns:
            Optional[List[Dict[str, Any]]]: A list of dictionaries, 
            including tournament info

        Example Usage:
            .. code-block:: python

                fighter_data = await mma.ranking_summary(19906)
        """  
        return await self.api._get(f"/unique-tournament/{tournament_id}/summary")
    
    async def rankings(self, ranking_id: int) -> Dict:
        """
        Pulls the full ranking data from the ranking provided by ranking_summary()

        Returns:
            Optional[List[Dict[str, Any]]]: A list of dictionaries, 
            including tournament info

        Example Usage:
            .. code-block:: python

                fighter_data = await mma.ranking_summary(19906)
        """  
        return await self.api._get(f"/rankings/{ranking_id}")
    




    
    
    
   
    


    

