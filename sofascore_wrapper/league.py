from .api import SofascoreAPI
from typing import List, Dict, Any, Literal

BASE_URL = "https://www.sofascore.com/api/v1"

class League:
    def __init__(self, api: SofascoreAPI, league_id: int):
        """
        Initialize the League class with the API and league ID.

        Args:
            api (SofascoreAPI): An instance of the SofascoreAPI class.
            league_id (int): The unique ID of the league.
        """
        self.api = api
        self.league_id = league_id

    async def get_league(self) -> dict:
        """
        Fetch general information about the league.

        Returns:
            dict: A dictionary containing league details.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "id": 17,
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
                "displayInverseHomeAwayTeams": false
            }
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}")

    async def get_seasons(self) -> List[Dict[str, Any]]:
        """
        Fetch all available seasons for the league.

        Returns:
            List[Dict[str, Any]]: A list of season objects.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            [
                {
                    "name": "Premier League 24/25",
                    "year": "24/25",
                    "editor": false,
                    "id": 61627
                },
                ...
            ]
        """
        data = await self.api._get(f"/unique-tournament/{self.league_id}/seasons")
        return data.get("seasons", [])
    
    async def current_season(self) -> Dict:
        """
        Returns the current season for the selected league.

        Returns:
            List[Dict[str, Any]]: A list of season objects.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "name": "Premier League 24/25",
                "year": "24/25",
                "editor": false,
                "id": 61627
            }
        """
        data = await self.api._get(f"/unique-tournament/{self.league_id}/seasons")
        season_obj = data.get("seasons", [])
        return season_obj[0] if season_obj else None

    async def get_info(self, season: int) -> dict:
        """
        Fetch statistical information about the league for a specific season.

        Args:
            season (int): The season ID to fetch information for.

        Returns:
            dict: A dictionary containing league statistics for the season.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "info": {
                    "goals": 691,
                    "homeTeamWins": 89,
                    "awayTeamWins": 79,
                    "draws": 61,
                    "yellowCards": 1041,
                    "redCards": 31,
                    "newcomersUpperDivision": [],
                    "newcomersLowerDivision": [
                        {
                            "name": "Leicester City",
                            "slug": "leicester-city",
                            "shortName": "Leicester",
                            "gender": "M",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 536747,
                            "nameCode": "LEI",
                            "disabled": false,
                            "national": false,
                            "type": 0,
                            "id": 31,
                            "country": {
                                "alpha2": "EN",
                                "alpha3": "ENG",
                                "name": "England",
                                "slug": "england"
                            },
                            "entityType": "team",
                            "teamColors": {
                                "primary": "#003090",
                                "secondary": "#ffffff",
                                "text": "#ffffff"
                            },
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "ليستر سيتي",
                                    "ru": "Лестер Сити",
                                    "hi": "लीसेस्टर सिटी",
                                    "bn": "লেস্টার সিটি"
                                },
                                "shortNameTranslation": {
                                    "ar": "ليستر",
                                    "hi": "लीसेस्टर",
                                    "bn": "লেস্টার"
                                }
                            }
                        }
                    ]
                }
            }
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/info")

    async def top_players_per_game(self, season: int) -> List[Dict[str, Any]]:
        """
        Fetch the top players per game for a specific season.

        Args:
            season (int): The season ID to fetch top players for.

        Returns:
            List[Dict[str, Any]]: A list of top players with their statistics.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            [
                {
                    "statistic": 10,
                    "player": {
                        "name": "Phil Foden",
                        "slug": "phil-foden",
                        "shortName": "P. Foden",
                        "position": "M",
                        "jerseyNumber": "47",
                        "userCount": 212999,
                        "id": 859765,
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "فيل فودين",
                                "hi": "फिल फोडेन",
                                "bn": "ফিল ফোডেন"
                            },
                            "shortNameTranslation": {
                                "ar": "ف. فودين",
                                "hi": "पी. फोडेन",
                                "bn": "পি. ফোডেন"
                            }
                        }
                    },
                    "event": {
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
                                "id": 17,
                                "displayInverseHomeAwayTeams": false
                            },
                            "priority": 617,
                            "isLive": false,
                            "id": 1
                        },
                        "customId": "rP",
                        "status": {
                            "code": 100,
                            "description": "Ended",
                            "type": "finished"
                        },
                        "winnerCode": 1,
                        "homeTeam": {
                            "name": "Manchester City",
                            "slug": "manchester-city",
                            "shortName": "Man City",
                            "gender": "M",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 2901739,
                            "nameCode": "MCI",
                            "disabled": false,
                            "national": false,
                            "type": 0,
                            "id": 17,
                            "entityType": "team",
                            "teamColors": {
                                "primary": "#66ccff",
                                "secondary": "#ffffff",
                                "text": "#ffffff"
                            }
                        },
                        "awayTeam": {
                            "name": "Aston Villa",
                            "slug": "aston-villa",
                            "shortName": "Aston Villa",
                            "gender": "M",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 878821,
                            "nameCode": "AVL",
                            "disabled": false,
                            "national": false,
                            "type": 0,
                            "id": 40,
                            "entityType": "team",
                            "teamColors": {
                                "primary": "#670e36",
                                "secondary": "#94bee5",
                                "text": "#94bee5"
                            }
                        },
                        "homeScore": {
                            "current": 4,
                            "display": 4,
                            "period1": 2,
                            "period2": 2,
                            "normaltime": 4
                        },
                        "awayScore": {
                            "current": 1,
                            "display": 1,
                            "period1": 1,
                            "period2": 0,
                            "normaltime": 1
                        },
                        "hasXg": true,
                        "id": 11352352,
                        "startTimestamp": 1712171700,
                        "slug": "aston-villa-manchester-city",
                        "finalResultOnly": false
                    }
                },
                ...
            ]
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/top-players-per-game/all/overall")

    async def get_image(self, image_type: Literal["dark", "light"] = "dark") -> str:
        """
        Get the league image URL.

        Args:
            image_type (str, optional): The type of image ("dark" or "light"). Defaults to "dark".

        Returns:
            str: The URL for the requested league image.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            "https://img.sofascore.com/api/v1/unique-tournament/17/image/dark"
        """
        return f"{BASE_URL}/unique-tournament/{self.league_id}/image/{image_type}"

    async def top_players(self, season: int) -> Dict[str, Any]:
        """
        Get top players for a specific season.

        Args:
            season (int): The season ID to fetch top players for.

        Returns:
            Dict[str, Any]: A dictionary containing top players' statistics.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "topPlayers": {
                    "rating": [
                        {
                            "statistics": {
                                "rating": 8.0090909090909,
                                "id": 1508984,
                                "type": "overall",
                                "appearances": 22
                            },
                            "playedEnough": true,
                            "player": {
                                "name": "Mohamed Salah",
                                "slug": "mohamed-salah",
                                "shortName": "M. Salah",
                                "position": "F",
                                "userCount": 345702,
                                "id": 159665,
                                "fieldTranslations": {
                                    "nameTranslation": {
                                        "ar": "محمد صلاح",
                                        "hi": "मोहम्मद सलाह",
                                        "bn": "মোহাম্মদ সালাহ"
                                    },
                                    "shortNameTranslation": {
                                        "ar": "م. صلاح",
                                        "hi": "एम. सलाह",
                                        "bn": "এম. সালাহ"
                                    }
                                }
                            },
                            "team": {
                                "name": "Liverpool",
                                "slug": "liverpool",
                                "shortName": "Liverpool",
                                "userCount": 2600079,
                                "national": false,
                                "id": 44,
                                "entityType": "team",
                                "teamColors": {
                                    "primary": "#374df5",
                                    "secondary": "#374df5",
                                    "text": "#ffffff"
                                }
                            }
                        }
                    ]
                }
            }
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/top-players/overall")

    async def top_teams(self, season: int) -> Dict[str, Any]:
        """
        Get top teams for a specific season.

        Args:
            season (int): The season ID to fetch top teams for.

        Returns:
            Dict[str, Any]: A dictionary containing top teams' statistics.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "topTeams": {
                    "avgRating": [
                        {
                            "team": {
                                "name": "Manchester City",
                                "slug": "manchester-city",
                                "shortName": "Manchester City",
                                "gender": "M",
                                "userCount": 2901739,
                                "national": false,
                                "type": 0,
                                "id": 17,
                                "entityType": "team",
                                "teamColors": {
                                    "primary": "#374df5",
                                    "secondary": "#374df5",
                                    "text": "#ffffff"
                                }
                            },
                            "statistics": {
                                "avgRating": 7.1757097791798,
                                "id": 24789,
                                "matches": 23,
                                "awardedMatches": 0
                            }
                        }
                    ]
                }
            }
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/top-teams/overall")

    async def get_latest_highlights(self) -> Dict[str, Any]:
        """
        Get the latest match highlights for the league.

        Returns:
            Dict[str, Any]: A dictionary containing the latest match highlights.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "media": [
                    {
                        "title": "Fulham 0 - 1 Man Utd",
                        "subtitle": "Full Highlights",
                        "url": "https://www.youtube.com/watch?v=1BYRn04UOaw",
                        "thumbnailUrl": "https://i.ytimg.com/vi/1BYRn04UOaw/hqdefault.jpg",
                        "mediaType": 1,
                        "doFollow": false,
                        "keyHighlight": false,
                        "id": 6193980,
                        "createdAtTimestamp": 1737944333,
                        "sourceUrl": "https://www.youtube.com/watch?v=1BYRn04UOaw"
                    }
                ]
            }
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/media")

    async def standings(self, season: int) -> Dict[str, Dict[str, Any]]:
        """
        Get the current league standings for a specific season.

        Args:
            season (int): The season ID to fetch standings for.

        Returns:
            Dict[str, Dict[str, Any]]: A dictionary containing the league standings.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "standings": [
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
                                "displayInverseHomeAwayTeams": false
                            },
                            "priority": 617,
                            "isGroup": false,
                            "isLive": false,
                            "id": 1
                        },
                        "type": "total",
                        "name": "Premier League",
                        "descriptions": [],
                        "tieBreakingRule": {
                            "text": "In the event that two (or more) teams have an equal number of points, the following rules break the tie: 1. Goal difference 2. Goals scored 3. H2H",
                            "id": 2393
                        },
                        "rows": [
                            {
                                "team": {
                                    "name": "Liverpool",
                                    "slug": "liverpool",
                                    "shortName": "Liverpool",
                                    "gender": "M",
                                    "sport": {
                                        "name": "Football",
                                        "slug": "football",
                                        "id": 1
                                    },
                                    "userCount": 2600079,
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
                                    }
                                },
                                "descriptions": [],
                                "promotion": {
                                    "text": "Champions League",
                                    "id": 804
                                },
                                "position": 1,
                                "matches": 22,
                                "wins": 16,
                                "scoresFor": 54,
                                "scoresAgainst": 21,
                                "id": 1134312,
                                "losses": 1,
                                "draws": 5,
                                "points": 53,
                                "scoreDiffFormatted": "+33"
                            }
                        ]
                    }
                ]
            }
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/standings/total")

    async def standings_home(self, season: int) -> Dict[str, Dict[str, Any]]:
        """
        Get the current league standings for home games in a specific season.

        Args:
            season (int): The season ID to fetch home standings for.

        Returns:
            Dict[str, Dict[str, Any]]: A dictionary containing the home standings.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "standings": [
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
                                "displayInverseHomeAwayTeams": false
                            },
                            "priority": 617,
                            "isGroup": false,
                            "isLive": false,
                            "id": 1
                        },
                        "type": "home",
                        "name": "Premier League",
                        "descriptions": [],
                        "tieBreakingRule": {
                            "text": "In the event that two (or more) teams have an equal number of points, the following rules break the tie: 1. Goal difference 2. Goals scored 3. H2H",
                            "id": 2393
                        },
                        "rows": [
                            {
                                "team": {
                                    "name": "Liverpool",
                                    "slug": "liverpool",
                                    "shortName": "Liverpool",
                                    "gender": "M",
                                    "sport": {
                                        "name": "Football",
                                        "slug": "football",
                                        "id": 1
                                    },
                                    "userCount": 2600079,
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
                                    }
                                },
                                "descriptions": [],
                                "promotion": {
                                    "text": "Champions League",
                                    "id": 804
                                },
                                "position": 1,
                                "matches": 11,
                                "wins": 8,
                                "scoresFor": 24,
                                "scoresAgainst": 9,
                                "id": 1134332,
                                "losses": 1,
                                "draws": 2,
                                "points": 26,
                                "scoreDiffFormatted": "+15"
                            }
                        ]
                    }
                ]
            }
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/standings/home")

    async def standings_away(self, season: int) -> Dict[str, Dict[str, Any]]:
        """
        Get the current league standings for away games in a specific season.

        Args:
            season (int): The season ID to fetch away standings for.

        Returns:
            Dict[str, Dict[str, Any]]: A dictionary containing the away standings.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "standings": [
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
                                "displayInverseHomeAwayTeams": false
                            },
                            "priority": 617,
                            "isGroup": false,
                            "isLive": false,
                            "id": 1
                        },
                        "type": "away",
                        "name": "Premier League",
                        "descriptions": [],
                        "tieBreakingRule": {
                            "text": "In the event that two (or more) teams have an equal number of points, the following rules break the tie: 1. Goal difference 2. Goals scored 3. H2H",
                            "id": 2393
                        },
                        "rows": [
                            {
                                "team": {
                                    "name": "Liverpool",
                                    "slug": "liverpool",
                                    "shortName": "Liverpool",
                                    "gender": "M",
                                    "sport": {
                                        "name": "Football",
                                        "slug": "football",
                                        "id": 1
                                    },
                                    "userCount": 2600079,
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
                                    }
                                },
                                "descriptions": [],
                                "promotion": {
                                    "text": "Champions League",
                                    "id": 804
                                },
                                "position": 1,
                                "matches": 11,
                                "wins": 8,
                                "scoresFor": 30,
                                "scoresAgainst": 12,
                                "id": 1134352,
                                "losses": 0,
                                "draws": 3,
                                "points": 27,
                                "scoreDiffFormatted": "+18"
                            }
                        ]
                    }
                ]
            }
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/standings/away")

    async def player_of_the_season(self, season: int) -> Dict:
        """
        Get the player of the season for a specific season.

        Args:
            season (int): The season ID to fetch the player of the season for.

        Returns:
            Dict: A dictionary containing the player of the season details.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "player": {
                    "name": "Rodri",
                    "slug": "rodri",
                    "shortName": "Rodri",
                    "position": "M",
                    "userCount": 100726,
                    "id": 827606,
                    "fieldTranslations": {
                        "nameTranslation": {
                            "ar": "رودري",
                            "hi": "रोड्री",
                            "bn": "রডরি"
                        },
                        "shortNameTranslation": {
                            "ar": "رودري",
                            "hi": "रोड्री",
                            "bn": "রডরি"
                        }
                    }
                },
                "statistics": {
                    "rating": 8.0117647058824,
                    "id": 1069463,
                    "type": "overall",
                    "appearances": 34
                },
                "team": {
                    "name": "Manchester City",
                    "slug": "manchester-city",
                    "shortName": "Manchester City",
                    "userCount": 2901739,
                    "national": false,
                    "id": 17,
                    "entityType": "team",
                    "teamColors": {
                        "primary": "#374df5",
                        "secondary": "#374df5",
                        "text": "#ffffff"
                    }
                }
            }
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/player-of-the-season")

    async def featured_game(self, season: int) -> Dict:
        """
        Get the featured game for a specific season.

        Args:
            season (int): The season ID to fetch the featured game for.

        Returns:
            Dict: A dictionary containing the featured game details.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "featuredEvents": [
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
                                "country": {
                                    "alpha2": "EN",
                                    "alpha3": "ENG",
                                    "name": "England",
                                    "slug": "england"
                                },
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
                                    "country": {
                                        "alpha2": "EN",
                                        "alpha3": "ENG",
                                        "name": "England",
                                        "slug": "england"
                                    },
                                    "flag": "england",
                                    "alpha2": "EN"
                                },
                                "userCount": 1361165,
                                "hasPerformanceGraphFeature": true,
                                "id": 17,
                                "country": {},
                                "hasEventPlayerStatistics": true,
                                "displayInverseHomeAwayTeams": false
                            },
                            "priority": 617,
                            "isGroup": false,
                            "isLive": false,
                            "id": 1
                        },
                        "season": {
                            "name": "Premier League 24/25",
                            "year": "24/25",
                            "editor": false,
                            "id": 61627
                        },
                        "roundInfo": {
                            "round": 24
                        },
                        "customId": "osF",
                        "status": {
                            "code": 0,
                            "description": "Not started",
                            "type": "notstarted"
                        },
                        "homeTeam": {
                            "name": "Nottingham Forest",
                            "slug": "nottingham-forest",
                            "shortName": "Forest",
                            "gender": "M",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 349426,
                            "nameCode": "NFO",
                            "disabled": false,
                            "national": false,
                            "type": 0,
                            "id": 14,
                            "country": {
                                "alpha2": "EN",
                                "alpha3": "ENG",
                                "name": "England",
                                "slug": "england"
                            },
                            "entityType": "team",
                            "subTeams": [],
                            "teamColors": {
                                "primary": "#cc0000",
                                "secondary": "#cc0000",
                                "text": "#cc0000"
                            }
                        },
                        "awayTeam": {
                            "name": "Brighton & Hove Albion",
                            "slug": "brighton-and-hove-albion",
                            "shortName": "Brighton",
                            "gender": "M",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 621440,
                            "nameCode": "BHA",
                            "disabled": false,
                            "national": false,
                            "type": 0,
                            "id": 30,
                            "country": {
                                "alpha2": "EN",
                                "alpha3": "ENG",
                                "name": "England",
                                "slug": "england"
                            },
                            "entityType": "team",
                            "subTeams": [],
                            "teamColors": {
                                "primary": "#0054a6",
                                "secondary": "#ffffff",
                                "text": "#ffffff"
                            }
                        },
                        "homeScore": {},
                        "awayScore": {},
                        "time": {},
                        "changes": {
                            "changeTimestamp": 0
                        },
                        "hasGlobalHighlights": false,
                        "detailId": 1,
                        "crowdsourcingDataDisplayEnabled": false,
                        "id": 12436930,
                        "startTimestamp": 1738413000,
                        "slug": "brighton-and-hove-albion-nottingham-forest",
                        "finalResultOnly": false,
                        "feedLocked": true,
                        "isEditor": false
                    }
                ]
            }
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/player-of-the-season")

    async def totw_rounds(self, season: int) -> Dict:
        """
        Get the available team of the week rounds for a specific season.

        Args:
            season (int): The season ID to fetch team of the week rounds for.

        Returns:
            Dict: A dictionary containing the available rounds.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "rounds": [
                    {
                        "roundId": 23,
                        "roundName": "23",
                        "roundSlug": "23:23",
                        "id": 16987,
                        "createdAtTimestamp": 1737966749
                    }
                ]
            }
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/team-of-the-week/rounds")

    async def totw(self, season: int, round: int) -> Dict[str, Any]:
        """
        Get the team of the week for a specific round in a season.

        Args:
            season (int): The season ID to fetch the team of the week for.
            round (int): The round ID to fetch the team of the week for.

        Returns:
            Dict[str, Any]: A dictionary containing the team of the week details.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "formation": "3-4-3",
                "players": [
                    {
                        "player": {
                            "name": "Jakub Stolarczyk",
                            "firstName": "",
                            "lastName": "",
                            "slug": "jakub-stolarczyk",
                            "shortName": "J. Stolarczyk",
                            "position": "G",
                            "jerseyNumber": "41",
                            "userCount": 952,
                            "id": 997830,
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "ياكوب ستولارتشيك",
                                    "hi": "जकूब स्टोलार्स्की",
                                    "bn": "জ্যাকুব স্টোলারকজিক"
                                },
                                "shortNameTranslation": {
                                    "ar": "ي. ستولارتشيك",
                                    "hi": "जे. स्टोलार्स्की",
                                    "bn": "জে. স্টোলারজিক"
                                }
                            }
                        },
                        "team": {
                            "name": "Leicester City",
                            "slug": "leicester-city",
                            "shortName": "Leicester",
                            "gender": "M",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 536747,
                            "nameCode": "LEI",
                            "disabled": false,
                            "national": false,
                            "type": 0,
                            "id": 31,
                            "entityType": "team",
                            "teamColors": {
                                "primary": "#003090",
                                "secondary": "#ffffff",
                                "text": "#ffffff"
                            }
                        },
                        "event": {
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
                                    "id": 17,
                                    "displayInverseHomeAwayTeams": false
                                },
                                "priority": 617,
                                "isLive": false,
                                "id": 1
                            },
                            "customId": "MXpf",
                            "status": {
                                "code": 100,
                                "description": "Ended",
                                "type": "finished"
                            },
                            "winnerCode": 2,
                            "homeTeam": {
                                "name": "Tottenham Hotspur",
                                "slug": "tottenham-hotspur",
                                "shortName": "Tottenham ",
                                "gender": "M",
                                "sport": {
                                    "name": "Football",
                                    "slug": "football",
                                    "id": 1
                                },
                                "userCount": 1327772,
                                "nameCode": "TOT",
                                "disabled": false,
                                "national": false,
                                "type": 0,
                                "id": 33,
                                "entityType": "team",
                                "teamColors": {
                                    "primary": "#ffffff",
                                    "secondary": "#000066",
                                    "text": "#000066"
                                }
                            },
                            "awayTeam": {
                                "name": "Leicester City",
                                "slug": "leicester-city",
                                "shortName": "Leicester",
                                "gender": "M",
                                "sport": {
                                    "name": "Football",
                                    "slug": "football",
                                    "id": 1
                                },
                                "userCount": 536747,
                                "nameCode": "LEI",
                                "disabled": false,
                                "national": false,
                                "type": 0,
                                "id": 31,
                                "entityType": "team",
                                "teamColors": {
                                    "primary": "#003090",
                                    "secondary": "#ffffff",
                                    "text": "#ffffff"
                                }
                            },
                            "homeScore": {
                                "current": 1,
                                "display": 1,
                                "period1": 1,
                                "period2": 0,
                                "normaltime": 1
                            },
                            "awayScore": {
                                "current": 2,
                                "display": 2,
                                "period1": 0,
                                "period2": 2,
                                "normaltime": 2
                            },
                            "hasXg": true,
                            "id": 12436907,
                            "startTimestamp": 1737900000,
                            "slug": "tottenham-hotspur-leicester-city",
                            "finalResultOnly": false
                        },
                        "rating": "8.1",
                        "order": 1,
                        "id": 198034
                    }
                ]
            }
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/team-of-the-week/{round}")

    async def rounds(self, season: int) -> Dict:
        """
        Get the available rounds for a specific season.

        Args:
            season (int): The season ID to fetch rounds for.

        Returns:
            Dict: A dictionary containing the available rounds.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "currentRound": {
                    "round": 24
                },
                "rounds": [
                    {
                        "round": 1
                    },
                    ...
                ]
            }
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/rounds")

    async def current_round(self, season: int) -> int:
        """
        Get the current round for a specific season.

        Args:
            season (int): The season ID to fetch the current round for.

        Returns:
            int: The current round number.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            24
        """
        data = await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/rounds")
        return data.get("currentRound", {}).get("round", None)
    
    async def fixtures(self, season: int, round: int) -> Dict[str, Any]:
        """
        Fetch the fixtures for a specific season and round.

        This method retrieves the fixtures of a particular round in a given season 
        for a league. It filters events where the status is "Not Started" (status 
        code 0).

        :param season: The season ID for which to fetch the fixtures (e.g., 61627 for Premier League 24/25).
        :param round: The round number for which to fetch the fixtures (e.g., 24).

        :return: A dictionary of fixtures for the specified season and round, with 
                events where the status code is 0 (Not Started).
                Returns an empty list if no fixtures match the criteria.
        :rtype: dict

        Example response:
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
                "userCount": 1360406,
                "hasPerformanceGraphFeature": true,
                "id": 17,
                "hasEventPlayerStatistics": true,
                "displayInverseHomeAwayTeams": false
                },
                "priority": 617,
                "isGroup": false,
                "isLive": false,
                "id": 1
            },
            "season": {
                "name": "Premier League 24/25",
                "year": "24/25",
                "editor": false,
                "id": 61627
            },
            "roundInfo": {
                "round": 24
            },
            "customId": "osF",
            "status": {
                "code": 0,
                "description": "Not started",
                "type": "notstarted"
            },
            "homeTeam": {
                "name": "Nottingham Forest",
                "slug": "nottingham-forest",
                "shortName": "Forest",
                "gender": "M",
                "sport": {
                "name": "Football",
                "slug": "football",
                "id": 1
                },
                "userCount": 350038,
                "nameCode": "NFO",
                "disabled": false,
                "national": false,
                "type": 0,
                "id": 14
            },
            "awayTeam": {
                "name": "Manchester City",
                "slug": "manchester-city",
                "shortName": "City",
                "gender": "M",
                "sport": {
                "name": "Football",
                "slug": "football",
                "id": 1
                },
                "userCount": 498380,
                "nameCode": "MCI",
                "disabled": false,
                "national": false,
                "type": 0,
                "id": 13
            }
            }
        ]
        }

        Example usage:
        >>> fixtures = await league.fixtures(season=61627, round=24)
        >>> print(fixtures)
        """
        return await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/round/{round}")

    
    async def next_fixtures(self) -> Dict[Dict, Any]:
        """
        Fetch the next fixtures for the current season and round.

        This method retrieves the next fixtures based on the current round of 
        the current season for a league. It filters events where the status is 
        "Not Started" (status code 0).

        :return: A list of dictionaries representing the fixtures for the next round 
                where the status is "Not Started". If no fixtures match the criteria, 
                it returns None.
        :rtype: list or None

        Example response:
        [
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
                    "userCount": 1360406,
                    "hasPerformanceGraphFeature": true,
                    "id": 17,
                    "hasEventPlayerStatistics": true,
                    "displayInverseHomeAwayTeams": false
                },
                "priority": 617,
                "isGroup": false,
                "isLive": false,
                "id": 1
                },
                "season": {
                "name": "Premier League 24/25",
                "year": "24/25",
                "editor": false,
                "id": 61627
                },
                "roundInfo": {
                "round": 24
                },
                "customId": "osF",
                "status": {
                "code": 0,
                "description": "Not started",
                "type": "notstarted"
                },
                "homeTeam": {
                "name": "Nottingham Forest",
                "slug": "nottingham-forest",
                "shortName": "Forest",
                "gender": "M",
                "sport": {
                    "name": "Football",
                    "slug": "football",
                    "id": 1
                },
                "userCount": 350038,
                "nameCode": "NFO",
                "disabled": false,
                "national": false,
                "type": 0,
                "id": 14
                },
                "awayTeam": {
                "name": "Manchester City",
                "slug": "manchester-city",
                "shortName": "City",
                "gender": "M",
                "sport": {
                    "name": "Football",
                    "slug": "football",
                    "id": 1
                },
                "userCount": 498380,
                "nameCode": "MCI",
                "disabled": false,
                "national": false,
                "type": 0,
                "id": 13
                }
            }
        ]

        """
        season_obj = await self.current_season()
        season = season_obj["id"]
        round = await self.current_round(season)

        data = await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/events/round/{round}")
        fixtures = [event for event in data.get("events", []) if event.get("status", {}).get("code") == 0]

        return sorted(fixtures, key = lambda x: x["startTimestamp"]) if fixtures else None
    
    async def last_fixtures(self) -> Dict[Dict, Any]:
        """
        Fetch the last fixtures for the current season and round or previous round.
        
        This method retrieves fixtures based on the current round of the current 
        season for a league. If there is at least one fixture with the status code 
        100, those fixtures are returned. If no such fixtures are found, it fetches 
        fixtures from the previous round (if the current round is not the first).

        :return: A list of dictionaries representing the fixtures for the last round 
                with at least one fixture with status code 100, or from the previous 
                round if no fixtures match the criteria.
        :rtype: list or None

        Example response:
        [
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
                        "userCount": 1360406,
                        "hasPerformanceGraphFeature": true,
                        "id": 17,
                        "hasEventPlayerStatistics": true,
                        "displayInverseHomeAwayTeams": false
                    },
                    "priority": 617,
                    "isGroup": false,
                    "isLive": false,
                    "id": 1
                },
                "season": {
                    "name": "Premier League 24/25",
                    "year": "24/25",
                    "editor": false,
                    "id": 61627
                },
                "roundInfo": {
                    "round": 24
                },
                "customId": "osF",
                "status": {
                    "code": 100,
                    "description": "Started",
                    "type": "started"
                },
                "homeTeam": {
                    "name": "Nottingham Forest",
                    "slug": "nottingham-forest",
                    "shortName": "Forest",
                    "gender": "M",
                    "sport": {
                        "name": "Football",
                        "slug": "football",
                        "id": 1
                    },
                    "userCount": 350038,
                    "nameCode": "NFO",
                    "disabled": false,
                    "national": false,
                    "type": 0,
                    "id": 14
                },
                "awayTeam": {
                    "name": "Manchester City",
                    "slug": "manchester-city",
                    "shortName": "City",
                    "gender": "M",
                    "sport": {
                        "name": "Football",
                        "slug": "football",
                        "id": 1
                    },
                    "userCount": 498380,
                    "nameCode": "MCI",
                    "disabled": false,
                    "national": false,
                    "type": 0,
                    "id": 13
                }
            }
        ]

        """
        season_obj = await self.current_season()
        season = season_obj["id"]
        round_obj = await self.current_round(season)

        data = await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/events/round/{round_obj}")

        fixtures = [event for event in data.get("events", []) if event.get("status", {}).get("code") == 100]

        if fixtures:
            return sorted(fixtures, key = lambda x: x["startTimestamp"], reverse = True)
        
        round = round_obj - 1 if round_obj > 1 else 1

        data = await self.api._get(f"/unique-tournament/{self.league_id}/season/{season}/events/round/{round}")
        last_fixtures = [event for event in data.get("events", []) if event.get("status", {}).get("code") == 100]
        fixtures = sorted(last_fixtures, key = lambda x: x["startTimestamp"], reverse = True)

        return fixtures if fixtures else None
    

