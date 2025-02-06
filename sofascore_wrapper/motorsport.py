from .api import SofascoreAPI
import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path
import json

class Motorsport:
    ENUMS_PATH = Path(__file__).parent / "tools" / "enums.json"

    with open(ENUMS_PATH, "r", encoding="utf-8") as file:
        ENUMS = json.load(file)

    def __init__(self, api: SofascoreAPI):
        self.api = api
        self.enums = self.ENUMS

    async def total_races(self) -> Dict[str, int]:
        """
        Retrieves the total count of today's motorsport races and how many are currently live.

        Returns:
            Dict[str, int]: A dictionary containing two keys:
                - "live": The number of live motorsport races.
                - "total": The total number of motorsport races scheduled for today.

        Example Response:
            .. code-block:: json
            {
                "live": 8,
                "total": 16
            }
        """
        data = await self.api._get("/sport/0/event-count")
        return data.get("motorsport", {})
    
    async def categories(self) -> Dict[str, int]:
        """
        Retrieves all the motorsport categories such as Rally, F1.

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
        return await self.api._get("/sport/motorsport/categories")
    
    async def live_races(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Retrieve all currently live motorsport events.

        Returns:
            Dict[str, List[Dict[str, Any]]]: A dictionary containing a list of live motorsport events under the key "events".
            Each event is represented as a dictionary with details such as stage, teams, results, and race status.

        """
        return await self.api._get("/sport/motorsport/events/live")
    
    async def featured_races(self) -> Dict[str, int]:
        """
        Retrieves the featured motorsport races.

        Returns:
            Dict[str, int]: A dictionary containing details about upcoming motorsport races.

        Example Response:
            .. code-block:: json

                {
                "stages": [
                    {
                    "uniqueStage": {
                        "category": {
                        "name": "Formula E",
                        "slug": "formula-e",
                        "sport": {
                            "name": "Motorsport",
                            "slug": "motorsport",
                            "id": 11
                        },
                        "id": 1321,
                        "flag": "formula-e"
                        },
                        "name": "Formula E",
                        "slug": "formula-e",
                        "id": 68
                    },
                    "description": "GP Diriyah 1",
                    "slug": "gp-diriyah-1",
                    "type": {
                        "id": 2,
                        "name": "Event"
                    },
                    "status": {
                        "description": "Not started",
                        "type": "notstarted"
                    },
                    "year": "2025",
                    "id": 210100,
                    "country": {
                        "alpha2": "SA",
                        "name": "Saudi Arabia"
                    },
                    "name": "GP Diriyah 1",
                    "info": {
                        "circuit": "Jeddah Corniche Circuit",
                        "circuitCity": "Jeddah",
                        "circuitCountry": "Saudi Arabia",
                        "circuitLength": 6174,
                        "laps": 50,
                        "raceDistance": 308700
                    },
                    "startDateTimestamp": 1739460600,
                    "endDateTimestamp": 1739556000,
                    "seasonStageName": "Formula E 2025",
                    "flag": "saudi-arabia",
                    "stageParent": {
                        "description": "Formula E 2025",
                        "id": 210097,
                        "startDateTimestamp": 1733513400
                    }
                    }
                ]
                }

        Example Usage:
            .. code-block:: python

                featured_races = await api.motorsport_featured_races()
                print(featured_races["stages"][0]["name"])  # Output: "GP Diriyah 1"

        """
        return await self.api._get("/stage/sport/motorsport/featured")
    
    async def seasons(self, motorsport_id: int) -> Dict[str, int]:
        """
        Retrieves season details for a specific motorsport category (e.g., Formula 1, Rally).

        Args:
            motorsport_id (int): The ID of the motorsport category.

        Returns:
            Dict[str, int]: A dictionary containing season details for the specified motorsport.

        Example Response:
            .. code-block:: json

                {
                "seasons": [
                    {
                    "uniqueStage": {
                        "category": {
                        "name": "Formula 1",
                        "slug": "formula-1",
                        "sport": {
                            "name": "Motorsport",
                            "slug": "motorsport",
                            "id": 11
                        },
                        "id": 36,
                        "flag": "formula-1"
                        },
                        "name": "Formula 1",
                        "slug": "formula-1",
                        "id": 40
                    },
                    "description": "Formula 1 2025",
                    "slug": "formula-1-2025",
                    "year": "2025",
                    "id": 209766,
                    "name": "Formula 1 2025",
                    "startDateTimestamp": 1741916100,
                    "endDateTimestamp": 1765119600
                    }
                ]
                }

        Example Usage:
            .. code-block:: python

                seasons_data = await api.seasons(motorsport_id=40)
                print(seasons_data["seasons"][0]["name"])  # Output: "Formula 1 2025"

        """
        return await self.api._get(f"/unique-stage/{motorsport_id}/seasons")
    
    async def current_season(self, motorsport_id: int) -> int:
        """
        Retrieves the current season for the selected motorsport (e.g., Formula 1, Rally).

        Args:
            motorsport_id (int): The ID of the motorsport category.

        Returns:
            Dict[str, int]: A dictionary containing season details for the specified motorsport.

        Example Response:
            .. code-block:: json

                209766

        Example Usage:
            .. code-block:: python

                current_season = await api.current_season(motorsport_id=40)
                print(current_season)  # Output: "209766"

        """
        data = await self.api._get(f"/unique-stage/{motorsport_id}/seasons")

        season_obj = [
            season for season in data["seasons"]
            if season["startDateTimestamp"] <= datetime.datetime.now().timestamp() <= season["endDateTimestamp"]
        ]
        return season_obj[0].get("uniqueStage", {}).get("id", {}) if season_obj else None
    
    async def races(self, season_id: int) -> Dict[str, int]:
        """
        Retrieves all the races for the selected season.

        Returns:
            Dict[str, int]: A dictionary containing two keys:

        Example Response:
            .. code-block:: json
            {
        "stages": [
            {
            "uniqueStage": {
                "category": {
                "name": "Formula 1",
                "slug": "formula-1",
                "sport": {
                    "name": "Motorsport",
                    "slug": "motorsport",
                    "id": 11
                },
                "id": 36,
                "country": {

                },
                "flag": "formula-1"
                },
                "name": "Formula 1",
                "slug": "formula-1",
                "id": 40
            },
            "description": "Australia GP",
            "slug": "formula-1-gp",
            "type": {
                "id": 2,
                "name": "Event"
            },
            "status": {
                "description": "Not started",
                "type": "notstarted"
            },
            "year": "2025",
            "id": 209767,
            "country": {
                "alpha2": "AU",
                "name": "Australia"
            },
            "name": "Australia GP",
            "info": {
                "circuit": "Melbourne Grand Prix Circuit",
                "circuitCity": "Melbourne",
                "circuitCountry": "Australia",
                "circuitLength": 5278,
                "laps": 58,
                "raceDistance": 306124
            },
            "startDateTimestamp": 1741916100,
            "endDateTimestamp": 1742104800,
            "seasonStageName": "Formula 1 2025",
            "flag": "australia",
            "stageParent": {
                "description": "Formula 1 2025",
                "id": 209766,
                "startDateTimestamp": 1741916100
            }
            },
        """
        return await self.api._get(f"/stage/{season_id}/substages")
    
    async def race_info(self, stage_id: int) -> Dict[str, int]:
        """
        Retrieves detailed information about a specific race stage for a selected motorsport event 
        (e.g., Formula 1, Rally) based on the provided stage ID.

        Args:
            stage_id (int): The ID of the specific race stage (e.g., Formula 1 Grand Prix event).

        Returns:
            Dict[str, int]: A dictionary containing details about the selected race stage, 
            including the name, description, country, circuit info, start and end times, and more.

        Example Response:
            .. code-block:: json

                {
                    "stage": {
                        "uniqueStage": {
                            "category": {
                                "name": "Formula 1",
                                "slug": "formula-1",
                                "sport": {
                                    "name": "Motorsport",
                                    "slug": "motorsport",
                                    "id": 11
                                },
                                "id": 36,
                                "country": {},
                                "flag": "formula-1"
                            },
                            "name": "Formula 1",
                            "slug": "formula-1",
                            "id": 40
                        },
                        "description": "Australia GP",
                        "slug": "formula-1-gp",
                        "type": {
                            "id": 2,
                            "name": "Event"
                        },
                        "status": {
                            "description": "Not started",
                            "type": "notstarted"
                        },
                        "year": "2025",
                        "id": 209767,
                        "country": {
                            "alpha2": "AU",
                            "name": "Australia"
                        },
                        "name": "Australia GP",
                        "info": {
                            "circuit": "Melbourne Grand Prix Circuit",
                            "circuitCity": "Melbourne",
                            "circuitCountry": "Australia",
                            "circuitLength": 5278,
                            "laps": 58,
                            "raceDistance": 306124
                        },
                        "startDateTimestamp": 1741916100,
                        "endDateTimestamp": 1742104800,
                        "seasonStageName": "Formula 1 2025",
                        "flag": "australia",
                        "stageParent": {
                            "description": "Formula 1 2025",
                            "id": 209766,
                            "startDateTimestamp": 1741916100
                        }
                    }
                }

        Example Usage:
            .. code-block:: python

                # Example usage of the race_info method
                race_details = await api.race_info(stage_id=40)
                print(race_details)  # Output: Details about the Australia GP stage

        """
        return await self.api._get(f"/stage/{stage_id}")
    
    async def driver_rankings(self, season_id: int) -> Dict[str, int]:
        """
        Retrieves the current standings of drivers for a given motorsport season.

        Args:
            season_id (int): The ID of the season for which to retrieve driver rankings.

        Returns:
            int: The driver rankings for the given season, including details such as 
            position, points, victories, and other stats.

        Example Response:
            .. code-block:: json

                {
                    "standings": [
                        {
                            "team": {
                                "name": "Verstappen M.",
                                "slug": "verstappen-max",
                                "shortName": "Verstappen M.",
                                "gender": "M",
                                "sport": {
                                    "name": "Motorsport",
                                    "slug": "motorsport",
                                    "id": 11
                                },
                                "category": {
                                    "name": "Formula 1",
                                    "slug": "formula-1",
                                    "sport": {
                                        "name": "Motorsport",
                                        "slug": "motorsport",
                                        "id": 11
                                    },
                                    "id": 36,
                                    "country": {},
                                    "flag": "formula-1"
                                },
                                "userCount": 31878,
                                "nameCode": "VER",
                                "disabled": false,
                                "national": false,
                                "parentTeam": {
                                    "name": "Red Bull Racing",
                                    "slug": "red-bull-racing",
                                    "shortName": "Red Bull Racing",
                                    "gender": "M",
                                    "sport": {
                                        "name": "Motorsport",
                                        "slug": "motorsport",
                                        "id": 11
                                    },
                                    "category": {
                                        "name": "Formula 1",
                                        "slug": "formula-1",
                                        "sport": {
                                            "name": "Motorsport",
                                            "slug": "motorsport",
                                            "id": 11
                                        },
                                        "id": 36,
                                        "country": {},
                                        "flag": "formula-1"
                                    },
                                    "userCount": 0,
                                    "nameCode": "RBR",
                                    "disabled": false,
                                    "national": false,
                                    "type": 0,
                                    "id": 214902,
                                    "country": {
                                        "alpha2": "GB",
                                        "alpha3": "GBR",
                                        "name": "United Kingdom",
                                        "slug": "united-kingdom"
                                    },
                                    "entityType": "team",
                                    "flag": "great-britain",
                                    "teamColors": {
                                        "primary": "#1e40ff",
                                        "secondary": "#222226",
                                        "text": "#222226"
                                    }
                                },
                                "type": 1,
                                "id": 191417,
                                "country": {
                                    "alpha2": "NL",
                                    "alpha3": "NLD",
                                    "name": "Netherlands",
                                    "slug": "netherlands"
                                },
                                "entityType": "team",
                                "flag": "netherlands",
                                "teamColors": {
                                    "primary": "#374df5",
                                    "secondary": "#374df5",
                                    "text": "#ffffff"
                                }
                            },
                            "points": 437,
                            "position": 1,
                            "victories": 9,
                            "racesStarted": 24,
                            "racesWithPoints": 23,
                            "polePositions": 8,
                            "podiums": 14,
                            "fastestLaps": 3,
                            "updatedAtTimestamp": 1733672824
                        }
                    ]
                }

        Example Usage:
            .. code-block:: python

                # Example usage of the driver_rankings method
                standings = await api.driver_rankings(season_id=206455)
                print(standings)  # Output: Driver rankings for the given season

        """
        return await self.api._get(f"/stage/{season_id}/standings/competitor")
    
    async def team_rankings(self, season_id: int) -> Dict[str, int]:
        """
        Retrieves the current standings of teams for a given motorsport season.

        Args:
            season_id (int): The ID of the season for which to retrieve team rankings.

        Returns:
            int: The driver rankings for the given season, including details such as 
            position, points, victories, and other stats.

        Example Response:
            .. code-block:: json

                {
                    "standings": [
                        {
                            "team": {
                                "name": "Verstappen M.",
                                "slug": "verstappen-max",
                                "shortName": "Verstappen M.",
                                "gender": "M",
                                "sport": {
                                    "name": "Motorsport",
                                    "slug": "motorsport",
                                    "id": 11
                                },
                                "category": {
                                    "name": "Formula 1",
                                    "slug": "formula-1",
                                    "sport": {
                                        "name": "Motorsport",
                                        "slug": "motorsport",
                                        "id": 11
                                    },
                                    "id": 36,
                                    "country": {},
                                    "flag": "formula-1"
                                },
                                "userCount": 31878,
                                "nameCode": "VER",
                                "disabled": false,
                                "national": false,
                                "parentTeam": {
                                    "name": "Red Bull Racing",
                                    "slug": "red-bull-racing",
                                    "shortName": "Red Bull Racing",
                                    "gender": "M",
                                    "sport": {
                                        "name": "Motorsport",
                                        "slug": "motorsport",
                                        "id": 11
                                    },
                                    "category": {
                                        "name": "Formula 1",
                                        "slug": "formula-1",
                                        "sport": {
                                            "name": "Motorsport",
                                            "slug": "motorsport",
                                            "id": 11
                                        },
                                        "id": 36,
                                        "country": {},
                                        "flag": "formula-1"
                                    },
                                    "userCount": 0,
                                    "nameCode": "RBR",
                                    "disabled": false,
                                    "national": false,
                                    "type": 0,
                                    "id": 214902,
                                    "country": {
                                        "alpha2": "GB",
                                        "alpha3": "GBR",
                                        "name": "United Kingdom",
                                        "slug": "united-kingdom"
                                    },
                                    "entityType": "team",
                                    "flag": "great-britain",
                                    "teamColors": {
                                        "primary": "#1e40ff",
                                        "secondary": "#222226",
                                        "text": "#222226"
                                    }
                                },
                                "type": 1,
                                "id": 191417,
                                "country": {
                                    "alpha2": "NL",
                                    "alpha3": "NLD",
                                    "name": "Netherlands",
                                    "slug": "netherlands"
                                },
                                "entityType": "team",
                                "flag": "netherlands",
                                "teamColors": {
                                    "primary": "#374df5",
                                    "secondary": "#374df5",
                                    "text": "#ffffff"
                                }
                            },
                            "points": 437,
                            "position": 1,
                            "victories": 9,
                            "racesStarted": 24,
                            "racesWithPoints": 23,
                            "polePositions": 8,
                            "podiums": 14,
                            "fastestLaps": 3,
                            "updatedAtTimestamp": 1733672824
                        }
                    ]
                }

        Example Usage:
            .. code-block:: python

                # Example usage of the team_rankings method
                standings = await api.team_rankings(season_id=206455)
                print(standings)  # Output: Driver rankings for the given season

        """
        return await self.api._get(f"/stage/{season_id}/standings/team")
    
    async def race_results(self, stage_id: int) -> Dict[str, int]:
        """
        Retrieves the driver rankings for a specific race

        Args:
            stage_id (int): The ID of the race (stage)

        Returns:
            int: The driver rankings for the given season, including details such as 
            position, points, victories, and other stats.

        Example Response:
            .. code-block:: json

                {
                    "standings": [
                        {
                            "team": {
                                "name": "Verstappen M.",
                                "slug": "verstappen-max",
                                "shortName": "Verstappen M.",
                                "gender": "M",
                                "sport": {
                                    "name": "Motorsport",
                                    "slug": "motorsport",
                                    "id": 11
                                },
                                "category": {
                                    "name": "Formula 1",
                                    "slug": "formula-1",
                                    "sport": {
                                        "name": "Motorsport",
                                        "slug": "motorsport",
                                        "id": 11
                                    },
                                    "id": 36,
                                    "country": {},
                                    "flag": "formula-1"
                                },
                                "userCount": 31878,
                                "nameCode": "VER",
                                "disabled": false,
                                "national": false,
                                "parentTeam": {
                                    "name": "Red Bull Racing",
                                    "slug": "red-bull-racing",
                                    "shortName": "Red Bull Racing",
                                    "gender": "M",
                                    "sport": {
                                        "name": "Motorsport",
                                        "slug": "motorsport",
                                        "id": 11
                                    },
                                    "category": {
                                        "name": "Formula 1",
                                        "slug": "formula-1",
                                        "sport": {
                                            "name": "Motorsport",
                                            "slug": "motorsport",
                                            "id": 11
                                        },
                                        "id": 36,
                                        "country": {},
                                        "flag": "formula-1"
                                    },
                                    "userCount": 0,
                                    "nameCode": "RBR",
                                    "disabled": false,
                                    "national": false,
                                    "type": 0,
                                    "id": 214902,
                                    "country": {
                                        "alpha2": "GB",
                                        "alpha3": "GBR",
                                        "name": "United Kingdom",
                                        "slug": "united-kingdom"
                                    },
                                    "entityType": "team",
                                    "flag": "great-britain",
                                    "teamColors": {
                                        "primary": "#1e40ff",
                                        "secondary": "#222226",
                                        "text": "#222226"
                                    }
                                },
                                "type": 1,
                                "id": 191417,
                                "country": {
                                    "alpha2": "NL",
                                    "alpha3": "NLD",
                                    "name": "Netherlands",
                                    "slug": "netherlands"
                                },
                                "entityType": "team",
                                "flag": "netherlands",
                                "teamColors": {
                                    "primary": "#374df5",
                                    "secondary": "#374df5",
                                    "text": "#ffffff"
                                }
                            },
                            "points": 437,
                            "position": 1,
                            "victories": 9,
                            "racesStarted": 24,
                            "racesWithPoints": 23,
                            "polePositions": 8,
                            "podiums": 14,
                            "fastestLaps": 3,
                            "updatedAtTimestamp": 1733672824
                        }
                    ]
                }

        Example Usage:
            .. code-block:: python

                # Example usage of the team_rankings method
                standings = await api.team_rankings(season_id=206455)
                print(standings)  # Output: Driver rankings for the given season

        """
        return await self.api._get(f"/stage/{stage_id}/standings/competitor")
    
    async def race_image(self, stage_id: int) -> str:
        """
        Returns the race track image
        """  
        return f"https://img.sofascore.com/api/v1/stage/{stage_id}/image"
    
    async def team_image(self, team_id: int) -> str:
        """
        Returns the team image
        """  
        return f"https://img.sofascore.com/api/v1/team/{team_id}/image"
    
    async def driver_image(self, driver_id: int) -> str:
        """
        Returns the driver image
        """  
        return f"https://img.sofascore.com/api/v1/team/{driver_id}/image"

    async def driver_info(self, driver_id: int) -> dict:
        """
        Retrieves detailed information about a driver.

        Args:
            driver_id (int): The ID of the driver.

        Returns:
            dict: A dictionary containing driver details.

        Example Response:
            .. code-block:: json

                {
                "team": {
                    "name": "Verstappen M.",
                    "shortName": "Verstappen M.",
                    "country": {
                    "name": "Netherlands",
                    "alpha2": "NL",
                    "alpha3": "NLD"
                    },
                    "playerTeamInfo": {
                    "residence": "Monte Carlo, Monaco",
                    "birthplace": "Hasselt, Belgium",
                    "height": 1.8,
                    "weight": 67,
                    "number": 1,
                    "birthDateTimestamp": 875577600
                    },
                    "parentTeam": {
                    "name": "Red Bull Racing",
                    "country": {
                        "name": "United Kingdom",
                        "alpha2": "GB",
                        "alpha3": "GBR"
                    }
                    },
                    "teamColors": {
                    "primary": "#374df5",
                    "secondary": "#374df5",
                    "text": "#ffffff"
                    }
                }
                }

        Example Usage:
            .. code-block:: python

                driver_details = await api.driver_info(driver_id=191417)
                print(driver_details)

        """
        return await self.api._get(f"/team/{driver_id}")
    
    async def team_info(self, team_id: int) -> dict:
        """
        Retrieves detailed information about a team.

        Args:
            team_id (int): The ID of the team.

        Returns:
            dict: A dictionary containing team details.

        Example Response:
            .. code-block:: json

                {
                "team": {
                    "name": "Red Bull Racing",
                    "slug": "red-bull-racing",
                    "shortName": "Red Bull Racing",
                    "gender": "M",
                    "sport": {
                    "name": "Motorsport",
                    "slug": "motorsport",
                    "id": 11
                    },
                    "category": {
                    "name": "Formula 1",
                    "slug": "formula-1",
                    "sport": {
                        "name": "Motorsport",
                        "slug": "motorsport",
                        "id": 11
                    },
                    "id": 36,
                    "country": {

                    },
                    "flag": "formula-1"
                    },
                    "userCount": 0,
                    "nameCode": "RBR",
                    "disabled": false,
                    "national": false,
                    "type": 0,
                    "id": 214902,
                    "country": {
                    "alpha2": "GB",
                    "alpha3": "GBR",
                    "name": "United Kingdom",
                    "slug": "united-kingdom"
                    },
                    "entityType": "team",
                    "fullName": "Red Bull Racing",
                    "teamColors": {
                    "primary": "#1e40ff",
                    "secondary": "#222226",
                    "text": "#222226"
                    }
                },
                "pregameForm": null
                }

        Example Usage:
            .. code-block:: python

                team_details = await api.team_info(team_id=191417)
                print(team_details)

        """
        return await self.api._get(f"/team/{team_id}")
    
    async def driver_seasons(self, driver_id: int) -> Dict[str, int]:
        """
        Retrieves a list of seasons in which a driver has participated.

        Args:
            driver_id (int): The ID of the driver.

        Returns:
            dict: A dictionary containing season details for the given driver.

        Example Usage:
            .. code-block:: python

                driver_seasons = await api.driver_seasons(driver_id=191417)
                print(driver_seasons)

        """
        return await self.api._get(f"/team/{driver_id}/stage-seasons")
    
    async def team_seasons(self, team_id: int) -> Dict[str, int]:
        """
        Retrieves a list of seasons in which a team has participated.

        Args:
            team_id (int): The ID of the team.

        Returns:
            dict: A dictionary containing season details for the given team.

        Example Usage:
            .. code-block:: python

                team_seasons = await api.team_seasons(team_id=191417)
                print(team_seasons)

        """
        return await self.api._get(f"/team/{team_id}/stage-seasons")
    
    async def driver_races(self, driver_id: int, season_id: int) -> Dict[str, int]:
        """
        Retrieves a list of races in which the driver participated for the given season

        Args:
            driver_id (int): The ID of the driver.

        Returns:
            dict: A dictionary containing season details for the given driver.

        Example Usage:
            .. code-block:: python

                driver_races = await api.driver_races(driver_id=191417, season_id=206455)
                print(driver_races)

        """
        return await self.api._get(f"/team/{driver_id}/stage-season/{season_id}/races")
    
    async def team_races(self, team_id: int, season_id: int) -> Dict[str, int]:
        """
        Retrieves a list of races in which the team participated for the given season

        Args:
            team_id (int): The ID of the team.

        Returns:
            dict: A dictionary containing season details for the given team.

        Example Usage:
            .. code-block:: python

                team_races = await api.team_races(team_id=214902, season_id=206455)
                print(team_races)

        """
        return await self.api._get(f"/team/{team_id}/stage-season/{season_id}/races")
    



    

