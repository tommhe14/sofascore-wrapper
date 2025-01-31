from .api import SofascoreAPI
from typing import Dict, List, Any

class Search:
    def __init__(self, api: SofascoreAPI, search_string: str, page: int = 0):
        """
        Initialize the Search class with the API, search string, and page number.

        Args:
            api (SofascoreAPI): An instance of the SofascoreAPI class.
            search_string (str): The search query string.
            page (int, optional): The page number for paginated results. Defaults to 0.
        """
        self.api = api
        self.search_string = search_string.lower().replace(" ", "%20")
        self.page = page

    async def search_all(self) -> Dict[str, Any]:
        """
        Perform a search across all categories (teams, players, matches, leagues, managers).

        Returns:
            Dict[str, Any]: A dictionary containing search results across all categories.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "results": [
                    {
                        "type": "team",
                        "entity": {
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
                            "country": {
                                "alpha2": "EN",
                                "name": "England",
                                "slug": "england"
                            },
                            "entityType": "team",
                            "subTeams": [],
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
                        "score": 1358595.1
                    },
                    ...
                ]
            }
        """
        return await self.api._get(f"/search/all/?q={self.search_string}&page={self.page}")

    async def search_match(self) -> List[Dict[str, Any]]:
        """
        Perform a search specifically for matches.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing match details.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            [
                {
                    "type": "event",
                    "entity": {
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
                                        "name": "England",
                                        "slug": "england"
                                    },
                                    "flag": "england",
                                    "alpha2": "EN"
                                },
                                "userCount": 1361165,
                                "id": 17,
                                "country": {},
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
                        "customId": "PR",
                        "status": {
                            "code": 100,
                            "description": "Ended",
                            "type": "finished"
                        },
                        "winnerCode": 3,
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
                            "country": {
                                "alpha2": "EN",
                                "name": "England",
                                "slug": "england"
                            },
                            "entityType": "team",
                            "subTeams": [],
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
                            "country": {
                                "alpha2": "EN",
                                "name": "England",
                                "slug": "england"
                            },
                            "entityType": "team",
                            "subTeams": [],
                            "teamColors": {
                                "primary": "#670e36",
                                "secondary": "#94bee5",
                                "text": "#94bee5"
                            },
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "أستون فيلا",
                                    "ru": "Астон Вилла",
                                    "hi": "एस्टन विला",
                                    "bn": "অ্যাস্টন ভিলা"
                                },
                                "shortNameTranslation": {
                                    "ar": "أستون فيلا",
                                    "hi": "एस्टन विला",
                                    "bn": "অ্যাস্টন ভিলা"
                                }
                            }
                        },
                        "homeScore": {
                            "current": 2,
                            "display": 2,
                            "period1": 1,
                            "period2": 1,
                            "normaltime": 2
                        },
                        "awayScore": {
                            "current": 2,
                            "display": 2,
                            "period1": 0,
                            "period2": 2,
                            "normaltime": 2
                        },
                        "hasXg": true,
                        "id": 12436443,
                        "startTimestamp": 1737221400,
                        "slug": "arsenal-aston-villa",
                        "finalResultOnly": false
                    },
                    "score": 7288.5156
                },
                ...
            ]
        """
        return await self.api._get(f"/search/events/?q={self.search_string}&page={self.page}")

    async def search_players(self) -> List[Dict[str, Any]]:
        """
        Perform a search specifically for players.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing player details.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            [
                {
                    "type": "player",
                    "entity": {
                        "name": "Bukayo Saka",
                        "firstName": "",
                        "lastName": "",
                        "slug": "bukayo-saka",
                        "shortName": "B. Saka",
                        "team": {
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
                            "country": {
                                "alpha2": "EN",
                                "name": "England",
                                "slug": "england"
                            },
                            "entityType": "team",
                            "subTeams": [],
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
                        "position": "F",
                        "jerseyNumber": "7",
                        "userCount": 168684,
                        "id": 934235,
                        "country": {
                            "alpha2": "EN",
                            "name": "England",
                            "slug": "england"
                        },
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "بوكايو ساكا",
                                "hi": "बुकायो साका",
                                "bn": "বুকায়ো সাকা"
                            },
                            "shortNameTranslation": {
                                "ar": "ب. ساكا",
                                "hi": "बी. साका",
                                "bn": "বি. সাকা"
                            }
                        }
                    },
                    "score": 90030.805
                },
                ...
            ]
        """
        return await self.api._get(f"/search/player-team-persons/?q={self.search_string}&page={self.page}")

    async def search_teams(self) -> List[Dict[str, Any]]:
        """
        Perform a search specifically for teams.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing team details.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            [
                {
                    "type": "team",
                    "entity": {
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
                        "country": {
                            "alpha2": "EN",
                            "name": "England",
                            "slug": "england"
                        },
                        "entityType": "team",
                        "subTeams": [],
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
                    "score": 1357694.8
                },
                ...
            ]
        """
        return await self.api._get(f"/search/teams/?q={self.search_string}&page={self.page}")

    async def search_leagues(self) -> List[Dict[str, Any]]:
        """
        Perform a search specifically for leagues.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing league details.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            [
                {
                    "type": "uniqueTournament",
                    "entity": {
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
                                "name": "England",
                                "slug": "england"
                            },
                            "flag": "england",
                            "alpha2": "EN"
                        },
                        "userCount": 1361165,
                        "id": 17,
                        "country": {},
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
                    "score": 577963.7
                },
                ...
            ]
        """
        return await self.api._get(f"/search/unique-tournaments/?q={self.search_string}&page={self.page}")