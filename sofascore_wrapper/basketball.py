from .api import SofascoreAPI
import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path
import json

class Basketball:
    ENUMS_PATH = Path(__file__).parent / "tools" / "enums.json"

    with open(ENUMS_PATH, "r", encoding="utf-8") as file:
        ENUMS = json.load(file)

    def __init__(self, api: SofascoreAPI):
        self.api = api
        self.enums = self.ENUMS

    async def total_games(self) -> Dict[str, int]:
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
        return data.get("basketball", {})


    async def live_games(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Retrieves all currently live basketball games.

        Returns:
            Dict[str, List[Dict[str, Any]]]: A dictionary containing a list of live basketball games under the key "events".
                Each game is represented as a dictionary with details such as tournament, teams, scores, and match status.

        Example Response:
            .. code-block:: json
            {
                "events": [
                    {
                        "tournament": {
                            "name": "U20 CONMEBOL Championship, Group B",
                            "slug": "u20-conmebol-championship-group-b",
                            "category": {
                                "name": "South America",
                                "slug": "south-america",
                                "sport": {
                                    "name": "Football",
                                    "slug": "football",
                                    "id": 1
                                },
                                "id": 1470,
                                "flag": "south-america"
                            },
                            "uniqueTournament": {
                                "name": "U20 CONMEBOL Championship",
                                "slug": "u20-conmebol-championship",
                                "primaryColorHex": "#348925",
                                "secondaryColorHex": "#afc402",
                                "category": {
                                    "name": "South America",
                                    "slug": "south-america",
                                    "sport": {
                                        "name": "Football",
                                        "slug": "football",
                                        "id": 1
                                    },
                                    "id": 1470,
                                    "flag": "south-america"
                                },
                                "userCount": 11952,
                                "id": 632,
                                "hasPerformanceGraphFeature": false,
                                "hasEventPlayerStatistics": true,
                                "displayInverseHomeAwayTeams": false
                            },
                            "priority": 0,
                            "isGroup": true,
                            "groupName": "Group B",
                            "isLive": false,
                            "id": 10066
                        },
                        "season": {
                            "name": "U20 CONMEBOL Ch.ship 2025",
                            "year": "2025",
                            "editor": false,
                            "id": 68914
                        },
                        "roundInfo": {
                            "round": 4
                        },
                        "customId": "xdjsiAn",
                        "status": {
                            "code": 6,
                            "description": "1st half",
                            "type": "inprogress"
                        },
                        "homeTeam": {
                            "name": "Ecuador U20",
                            "slug": "ecuador-u20",
                            "shortName": "Ecuador U20",
                            "gender": "M",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 4401,
                            "nameCode": "ECU",
                            "disabled": false,
                            "national": true,
                            "type": 0,
                            "id": 33758,
                            "country": {
                                "alpha2": "EC",
                                "alpha3": "ECU",
                                "name": "Ecuador",
                                "slug": "ecuador"
                            },
                            "entityType": "team",
                            "teamColors": {
                                "primary": "#ffff00",
                                "secondary": "#000063",
                                "text": "#000063"
                            },
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "الإكوادور تحت 20",
                                    "ru": "Эквадор U20"
                                }
                            }
                        },
                        "awayTeam": {
                            "name": "Brazil U20",
                            "slug": "brazil-u20",
                            "shortName": "Brazil U20",
                            "gender": "M",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 39092,
                            "nameCode": "BRA",
                            "disabled": false,
                            "national": true,
                            "type": 0,
                            "id": 22672,
                            "country": {
                                "alpha2": "BR",
                                "alpha3": "BRA",
                                "name": "Brazil",
                                "slug": "brazil"
                            },
                            "entityType": "team",
                            "teamColors": {
                                "primary": "#ffff00",
                                "secondary": "#009933",
                                "text": "#009933"
                            },
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "البرازيل تحت 20",
                                    "ru": "Бразилия U20"
                                }
                            }
                        },
                        "homeScore": {
                            "current": 0,
                            "display": 0,
                            "period1": 0,
                            "normaltime": 0
                        },
                        "awayScore": {
                            "current": 0,
                            "display": 0,
                            "period1": 0,
                            "normaltime": 0
                        },
                        "time": {
                            "initial": 0,
                            "max": 2700,
                            "extra": 540,
                            "currentPeriodStartTimestamp": 1738279810
                        },
                        "changes": {
                            "changes": [
                                "homeScore.period1",
                                "homeScore.normaltime",
                                "awayScore.period1",
                                "awayScore.normaltime"
                            ],
                            "changeTimestamp": 1738279909
                        },
                        "hasGlobalHighlights": false,
                        "hasEventPlayerStatistics": true,
                        "hasEventPlayerHeatMap": true,
                        "detailId": 1,
                        "crowdsourcingDataDisplayEnabled": false,
                        "id": 13123315,
                        "statusTime": {
                            "prefix": "",
                            "initial": 0,
                            "max": 2700,
                            "timestamp": 1738279810,
                            "extra": 540
                        },
                        "startTimestamp": 1738279800,
                        "slug": "ecuador-u20-brazil-u20",
                        "lastPeriod": "period1",
                        "finalResultOnly": false,
                        "feedLocked": true,
                        "isEditor": false
                    }
                ]
            }
        """
        return await self.api._get("/sport/basketball/events/live")

    async def games_by_date(self, sport: str = "basketball", date: str = None) -> Dict[str, Any]:
        """
        Retrieves the fixtures for today or a specific date.

        Args:
            sport (str): The sport of which you wish to gain fixtures for. Check below for appropriate sport names.
            date (str, optional): The date in the format "YYYY-MM-DD". If not provided, today's date is used.

        Arg sport (str, Any):
            [
                "football", "rugby", "cricket", "tennis", "mma", "motorsport", "darts", "snooker",
                "cycling", "basketball", "table-tennis", "ice-hockey", "e-sports", "handball",
                "volleyball", "baseball", "american-football", "futsal", "minifootball", "badminton",
                "aussie-rules", "beach-volley", "waterpolo", "floorball", "bandy"
            ]

        }

        Returns:
            Dict[str, Any]: A dictionary containing the fixtures for the specified date, including match details, teams, and timings.

        Example Response:
            .. code-block:: json
            {
                "events": [
                    {
                        "tournament": {
                            "name": "Premier League",
                            "slug": "premier-league",
                            "category": {
                                "name": "England",
                                "slug": "england",
                                "sport": {
                                    "name": "Football",
                                    "slug": "football",
                                    "id": 1
                                },
                                "id": 1,
                                "flag": "england",
                                "alpha2": "EN"
                            },
                            "uniqueTournament": {
                                "name": "Premier League",
                                "slug": "premier-league",
                                "primaryColorHex": "#3c1c5a",
                                "secondaryColorHex": "#f80158",
                                "category": {
                                    "name": "England",
                                    "slug": "england",
                                    "sport": {
                                        "name": "Football",
                                        "slug": "football",
                                        "id": 1
                                    },
                                    "id": 1,
                                    "flag": "england",
                                    "alpha2": "EN"
                                },
                                "userCount": 1361165,
                                "hasPerformanceGraphFeature": true,
                                "id": 17,
                                "displayInverseHomeAwayTeams": false,
                                "fieldTranslations": {
                                    "nameTranslation": {
                                        "ar": "الدوري الإنجليزي الممتاز",
                                        "hi": "प्रिमियर लीग",
                                        "bn": "প্রিমিয়ার লীগ"
                                    },
                                    "shortNameTranslation": {}
                                }
                            },
                            "priority": 617,
                            "isLive": false,
                            "id": 1,
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "الدوري الإنجليزي الممتاز",
                                    "hi": "प्रिमियर लीग",
                                    "bn": "প্রিমিয়ার লীগ"
                                },
                                "shortNameTranslation": {}
                            }
                        },
                        "customId": "HsR",
                        "status": {
                            "code": 0,
                            "description": "Not started",
                            "type": "notstarted"
                        },
                        "winnerCode": 0,
                        "homeTeam": {
                            "name": "Arsenal",
                            "slug": "arsenal",
                            "shortName": "Arsenal",
                            "gender": "M",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 2341486,
                            "nameCode": "ARS",
                            "disabled": false,
                            "national": false,
                            "type": 0,
                            "id": 42,
                            "entityType": "team",
                            "teamColors": {
                                "primary": "#cc0000",
                                "secondary": "#ffffff",
                                "text": "#ffffff"
                            },
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "ارسنال",
                                    "ru": "Арсенал",
                                    "hi": "आर्सेनल",
                                    "bn": "আর্সেনাল"
                                },
                                "shortNameTranslation": {
                                    "ar": "ارسنال",
                                    "hi": "आर्सेनल",
                                    "bn": "আর্সেনাল"
                                }
                            }
                        },
                        "awayTeam": {
                            "name": "Liverpool",
                            "slug": "liverpool",
                            "shortName": "Liverpool",
                            "gender": "M",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 2572976,
                            "nameCode": "LIV",
                            "disabled": false,
                            "national": false,
                            "type": 0,
                            "id": 44,
                            "entityType": "team",
                            "teamColors": {
                                "primary": "#cc0000",
                                "secondary": "#ffffff",
                                "text": "#ffffff"
                            },
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "ليفربول",
                                    "ru": "Ливерпуль",
                                    "hi": "लिवरपूल",
                                    "bn": "লিভারপুল"
                                },
                                "shortNameTranslation": {
                                    "ar": "ليفربول",
                                    "hi": "लिवरपूल",
                                    "bn": "লিভারপুল"
                                }
                            }
                        },
                        "homeScore": {
                            "current": 0,
                            "display": 0,
                            "period1": 0,
                            "period2": 0,
                            "normaltime": 0
                        },
                        "awayScore": {
                            "current": 0,
                            "display": 0,
                            "period1": 0,
                            "period2": 0,
                            "normaltime": 0
                        },
                        "time": {
                            "injuryTime1": 0,
                            "injuryTime2": 0,
                            "currentPeriodStartTimestamp": 0
                        },
                        "changes": {
                            "changes": [],
                            "changeTimestamp": 0
                        },
                        "hasGlobalHighlights": false,
                        "hasXg": false,
                        "hasEventPlayerStatistics": false,
                        "hasEventPlayerHeatMap": false,
                        "detailId": 1,
                        "crowdsourcingDataDisplayEnabled": false,
                        "id": 12436472,
                        "startTimestamp": 1735330500,
                        "slug": "arsenal-liverpool",
                        "finalResultOnly": false,
                        "feedLocked": false,
                        "isEditor": false
                    }
                ]
            }
        """
        if date is None:
            date = datetime.datetime.now().strftime("%Y-%m-%d")

        if sport.lower().replace(' ', '-') not in self.enums["sports"]:
            raise ValueError(f"Invalid sport: {sport.lower().replace(' ', '-')}. Must be one of {list(self.enums['sports'].keys())}")

        endpoint = f"/sport/{sport.lower().replace(' ', '-')}/scheduled-events/{date}"
        return await self.api._get(endpoint)
    
    async def player_ratings(self, player_id: int, league_id: int, season_id: int) -> Dict[str, int]:
        """
        Retrieves a player's ratings for a specific league and season.

        Args:
            player_id (int): The ID of the player.
            league_id (int): The ID of the league (unique tournament).
            season_id (int): The ID of the season.

        Returns:
            Dict[str, int]: A dictionary containing the player's ratings.

        Example Response:
            .. code-block:: json

                {
                    "seasonRatings": [
                        {
                            "eventId": 12696938,
                            "event": {
                                "homeTeam": {
                                    "name": "Milwaukee Bucks",
                                    "id": 3410
                                },
                                "awayTeam": {
                                    "name": "Memphis Grizzlies",
                                    "id": 3415
                                },
                                "homeScore": {
                                    "current": 119
                                },
                                "awayScore": {
                                    "current": 132
                                },
                                "status": {
                                    "description": "Ended"
                                }
                            },
                            "rating": 7.9,
                            "opponent": {
                                "name": "Memphis Grizzlies",
                                "id": 3415
                            },
                            "isHome": true
                        }
                    ]
                }

        Example Usage:
            .. code-block:: python

                ratings = await api.player_ratings(player_id=123, league_id=132, season_id=2024)
                print(ratings["seasonRatings"][0]["rating"])  # Output: 7.9

        """
        return await self.api._get(f"/player/{player_id}/unique-tournament/{league_id}/season/{season_id}/ratings")
    
    async def player_seasons(self, player_id: int) -> Dict[str, Any]:
        """
        Retrieves a player's seasons and the leagues they participated in.

        Args:
            player_id (int): The ID of the player.

        Returns:
            Dict[str, Any]: A dictionary containing the player's seasons and league details.

        Example Response:
            .. code-block:: json

                {
                    "uniqueTournamentSeasons": [
                        {
                            "uniqueTournament": {
                                "name": "NBA",
                                "slug": "nba",
                                "primaryColorHex": "#045daf",
                                "secondaryColorHex": "#cc2b31",
                                "category": {
                                    "name": "USA",
                                    "slug": "usa",
                                    "sport": {
                                        "name": "Basketball",
                                        "slug": "basketball",
                                        "id": 2
                                    },
                                    "id": 15,
                                    "flag": "usa",
                                    "alpha2": "US"
                                },
                                "userCount": 241408,
                                "id": 132,
                                "displayInverseHomeAwayTeams": true
                            },
                            "seasons": [
                                {
                                    "name": "NBA 24/25",
                                    "year": "24/25",
                                    "editor": false,
                                    "id": 65360
                                }
                            ]
                        }
                    ]
                }

        Example Usage:
            .. code-block:: python

                seasons = await api.player_seasons(player_id=123)
                print(seasons["uniqueTournamentSeasons"][0]["uniqueTournament"]["name"])  # Output: "NBA"

        """
        return await self.api._get(f"/player/{player_id}/statistics/seasons")
    
    async def player_stats(self, player_id: int, league_id: int) -> Dict[str, Any]:
        """
        Retrieves a player's statistics for a specific league and season.

        Args:
            player_id (int): The ID of the player.
            league_id (int): The ID of the league (unique tournament).

        Returns:
            Dict[str, Any]: A dictionary containing the player's season statistics, including points, rebounds, assists, and more.

        Example Response:
            .. code-block:: json

                {
                    "seasons": [
                        {
                            "statistics": {
                                "points": 1302,
                                "rebounds": 499,
                                "assists": 241,
                                "blocks": 54,
                                "steals": 31,
                                "rating": 8.3,
                                "appearances": 41
                            },
                            "team": {
                                "name": "Milwaukee Bucks",
                                "slug": "milwaukee-bucks",
                                "shortName": "Bucks",
                                "id": 3410
                            },
                            "season": {
                                "name": "NBA 24/25",
                                "year": "24/25",
                                "id": 65360
                            }
                        }
                    ]
                }

        Example Usage:
            .. code-block:: python

                stats = await api.player_stats(player_id=123, league_id=132)
                print(stats["seasons"][0]["statistics"]["points"])  # Output: 1302

        """
        return await self.api._get(f"/player/{player_id}/unique-tournament/{league_id}/statistics/regularSeason")
    
    async def top_players_per_game(self, league_id: int, season_id: int) -> Dict[str, Any]:
        """
        Retrieves the top players' statistics per game for a specific league and season.

        Args:
            league_id (int): The ID of the league (unique tournament).
            season_id (int): The ID of the season.

        Returns:
            Dict[str, Any]: A dictionary containing top players' statistics per game, 
            including points, rebounds, assists, and more.

        Example Response:
            .. code-block:: json

                {
                    "topPlayers": {
                        "points": [
                            {
                                "statistic": 60,
                                "player": {
                                    "name": "De'Aaron Fox",
                                    "shortName": "D. Fox",
                                    "position": "G",
                                    "id": 885244
                                },
                                "event": {
                                    "tournament": {
                                        "name": "NBA",
                                        "id": 177
                                    },
                                    "homeTeam": {
                                        "name": "Sacramento Kings",
                                        "id": 3413
                                    },
                                    "awayTeam": {
                                        "name": "Minnesota Timberwolves",
                                        "id": 3426
                                    },
                                    "homeScore": {
                                        "current": 126
                                    },
                                    "awayScore": {
                                        "current": 130
                                    },
                                    "id": 12687000
                                }
                            }
                        ]
                    }
                }

        Example Usage:
            .. code-block:: python

                stats = await api.top_players_per_game(league_id=132, season_id=65360)
                print(stats["topPlayers"]["points"][0]["player"]["name"])  # Output: De'Aaron Fox

        """
        return await self.api._get(f"/unique-tournament/{league_id}/season/{season_id}/top-players-per-game/all/regularSeason")

    async def top_players_per_season(self, league_id: int, season_id: int) -> Dict[str, Any]:
        """
        Retrieves the top players' statistics per game for a specific league and season.

        Args:
            league_id (int): The ID of the league (unique tournament).
            season_id (int): The ID of the season.

        Returns:
            Dict[str, Any]: A dictionary containing top players' statistics per game, 
            including points, rebounds, assists, and more.

        Example Response:
            .. code-block:: json

                {
                    "topPlayers": {
                        "points": [
                            {
                                "statistic": 60,
                                "player": {
                                    "name": "De'Aaron Fox",
                                    "shortName": "D. Fox",
                                    "position": "G",
                                    "id": 885244
                                },
                                "event": {
                                    "tournament": {
                                        "name": "NBA",
                                        "id": 177
                                    },
                                    "homeTeam": {
                                        "name": "Sacramento Kings",
                                        "id": 3413
                                    },
                                    "awayTeam": {
                                        "name": "Minnesota Timberwolves",
                                        "id": 3426
                                    },
                                    "homeScore": {
                                        "current": 126
                                    },
                                    "awayScore": {
                                        "current": 130
                                    },
                                    "id": 12687000
                                }
                            }
                        ]
                    }
                }

        Example Usage:
            .. code-block:: python

                stats = await api.top_players_per_game(league_id=132, season_id=65360)
                print(stats["topPlayers"]["points"][0]["player"]["name"])  # Output: De'Aaron Fox

        """
        return await self.api._get(f"/unique-tournament/{league_id}/season/{season_id}/top-players/regularSeason")

    async def top_teams_per_season(self, league_id: int, season_id: int) -> Dict[str, Any]:
        """
        Retrieves the top teams' statistics per game for a specific league and season.

        Args:
            league_id (int): The ID of the league (unique tournament).
            season_id (int): The ID of the season.

        Returns:
            Dict[str, Any]: A dictionary containing top teams' statistics per game,
            including points, rebounds, assists, and more.

        Example Response:
            .. code-block:: json

                {
                    "topTeams": {
                        "points": [
                            {
                                "team": {
                                    "name": "Memphis Grizzlies",
                                    "slug": "memphis-grizzlies",
                                    "shortName": "Memphis Grizzlies",
                                    "gender": "M",
                                    "userCount": 51009,
                                    "national": false,
                                    "type": 0,
                                    "id": 3415,
                                    "entityType": "team",
                                    "teamColors": {
                                        "primary": "#374df5",
                                        "secondary": "#374df5",
                                        "text": "#ffffff"
                                    },
                                    "fieldTranslations": {
                                        "nameTranslation": {
                                            "ar": "ممفيس جريزليز",
                                            "ru": "Мемфис Гриззлис",
                                            "hi": "मेम्फिस ग्रिजलीज़",
                                            "bn": "মেমফিস গ্রিজলিস"
                                        },
                                        "shortNameTranslation": {
                                            "ar": "جريزليس",
                                            "hi": "ग्रिज़लीज़",
                                            "bn": "গ্রিজলিস"
                                        }
                                    }
                                },
                                "statistics": {
                                    "points": 6046,
                                    "id": 3834,
                                    "matches": 49,
                                    "awardedMatches": 0
                                }
                            }
                        ]
                    }
                }

        Example Usage:
            .. code-block:: python

                stats = await api.top_teams_per_season(league_id=132, season_id=65360)
                print(stats["topTeams"]["points"][0]["team"]["name"])  # Output: Memphis Grizzlies

        """
        return await self.api._get(f"/unique-tournament/{league_id}/season/{season_id}/top-teams/regularSeason")

    


    

