from .api import SofascoreAPI
import datetime
from typing import Optional, Dict

class Match:
    def __init__(self, api: SofascoreAPI, match_id: int = None):
        self.api = api
        self.match_id = match_id

    async def total_games(self) -> Dict[str, int]:
        """
        Retrieves the total count of today's football games and how many are currently live.

        Returns:
            Dict[str, int]: A dictionary containing two keys:
                - "live": The number of live football games.
                - "total": The total number of football games scheduled for today.

        Example Response:
            .. code-block:: json
            {
                "live": 21,
                "total": 270
            }
        """
        data = await self.api._get("/sport/0/event-count")
        return data.get("football", {})
    
    from typing import Dict, Any, List

    async def live_games(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Retrieves all currently live football games.

        Returns:
            Dict[str, List[Dict[str, Any]]]: A dictionary containing a list of live football games under the key "events".
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
        return await self.api._get("/sport/football/events/live")

    async def games_by_date(self, date: str = None) -> Dict[str, Any]:
        """
        Retrieves the fixtures for today or a specific date.

        Args:
            date (str, optional): The date in the format "YYYY-MM-DD". If not provided, today's date is used.

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
        
        return await self.api._get(f"/sport/football/scheduled-events/{date}")

        
    async def match_odds(self) -> Dict[str, Any]:
        """
        Fetches the match odds for the specified match.

        Returns:
            Dict[str, Any]: A dictionary containing the match odds data. The structure includes:
                - markets (List[Dict[str, Any]]): A list of market objects, each containing:
                    - sourceId (int): The source ID of the market.
                    - structureType (int): The structure type of the market.
                    - marketId (int): The ID of the market.
                    - marketName (str): The name of the market.
                    - isLive (bool): Indicates if the market is live.
                    - fid (int): The fid of the market.
                    - suspended (bool): Indicates if the market is suspended.
                    - id (int): The ID of the market.
                    - choices (List[Dict[str, Any]]): A list of choices/outcomes for the market, each containing:
                        - initialFractionalValue (str): The initial fractional odds value.
                        - fractionalValue (str): The current fractional odds value.
                        - sourceId (int): The source ID of the choice.
                        - name (str): The name of the choice.
                        - winning (bool): Indicates if the choice is winning.
                        - change (int): The change in odds.

        Example Response:
            .. code-block:: json
            {
                "markets": [
                    {
                        "sourceId": 168664758,
                        "structureType": 1,
                        "marketId": 1,
                        "marketName": "Full time",
                        "isLive": false,
                        "fid": 168664758,
                        "suspended": false,
                        "id": 1962878117,
                        "choices": [
                            {
                                "initialFractionalValue": "17/4",
                                "fractionalValue": "9/2",
                                "sourceId": 2114984998,
                                "name": "1",
                                "winning": false,
                                "change": 1
                            },
                            {
                                "initialFractionalValue": "10/3",
                                "fractionalValue": "31/10",
                                "sourceId": 2114985000,
                                "name": "X",
                                "winning": false,
                                "change": -1
                            },
                            {
                                "initialFractionalValue": "53/100",
                                "fractionalValue": "57/100",
                                "sourceId": 2114985001,
                                "name": "2",
                                "winning": true,
                                "change": 1
                            }
                        ]
                    }
                ]
            }

        Raises:
            Exception: If the API request fails or returns an error.
        """
        return await self.api._get(f"/event/{self.match_id}/odds/1/all")
    
    async def featured_odds(self) -> Dict[str, Any]:
        """
        Fetches the featured odds for the specified match.

        Returns:
            Dict[str, Any]: A dictionary containing the featured odds data. The structure includes:
                - featured (Dict[str, Dict[str, Any]]): A dictionary of featured markets, each containing:
                    - default (Dict[str, Any]): The default market data, including:
                        - sourceId (int): The source ID of the market.
                        - structureType (int): The structure type of the market.
                        - marketId (int): The ID of the market.
                        - marketName (str): The name of the market.
                        - isLive (bool): Indicates if the market is live.
                        - fid (int): The fid of the market.
                        - suspended (bool): Indicates if the market is suspended.
                        - id (int): The ID of the market.
                        - choices (List[Dict[str, Any]]): A list of choices/outcomes for the market, each containing:
                            - initialFractionalValue (str): The initial fractional odds value.
                            - fractionalValue (str): The current fractional odds value.
                            - sourceId (int): The source ID of the choice.
                            - name (str): The name of the choice.
                            - winning (bool): Indicates if the choice is winning.
                            - change (int): The change in odds.
                    - asian (Dict[str, Any]): The Asian handicap market data, with the same structure as `default`.
                    - fullTime (Dict[str, Any]): The full-time market data, with the same structure as `default`.
                - hasMoreOdds (bool): Indicates if there are more odds available.

        Example Response:
            .. code-block:: json
            {
                "featured": {
                    "default": {
                        "sourceId": 168664758,
                        "structureType": 1,
                        "marketId": 1,
                        "marketName": "Full time",
                        "isLive": false,
                        "fid": 168664758,
                        "suspended": false,
                        "id": 1962878117,
                        "choices": [
                            {
                                "initialFractionalValue": "17/4",
                                "fractionalValue": "9/2",
                                "sourceId": 2114984998,
                                "name": "1",
                                "winning": false,
                                "change": 1
                            },
                            {
                                "initialFractionalValue": "10/3",
                                "fractionalValue": "31/10",
                                "sourceId": 2114985000,
                                "name": "X",
                                "winning": false,
                                "change": -1
                            },
                            {
                                "initialFractionalValue": "53/100",
                                "fractionalValue": "57/100",
                                "sourceId": 2114985001,
                                "name": "2",
                                "winning": true,
                                "change": 1
                            }
                        ]
                    },
                    "asian": {
                        "sourceId": 168664758,
                        "structureType": 1,
                        "marketId": 17,
                        "marketName": "Asian handicap",
                        "isLive": false,
                        "fid": 168664760,
                        "suspended": false,
                        "id": 1962996370,
                        "choices": [
                            {
                                "initialFractionalValue": "49/50",
                                "fractionalValue": "22/25",
                                "sourceId": 2114985005,
                                "name": "(1) Girona FC",
                                "change": -1
                            },
                            {
                                "initialFractionalValue": "23/25",
                                "fractionalValue": "51/50",
                                "sourceId": 2114985008,
                                "name": "(-1) Arsenal",
                                "change": 1
                            }
                        ]
                    },
                    "fullTime": {
                        "sourceId": 168664758,
                        "structureType": 1,
                        "marketId": 1,
                        "marketName": "Full time",
                        "isLive": false,
                        "fid": 168664758,
                        "suspended": false,
                        "id": 1962878117,
                        "choices": [
                            {
                                "initialFractionalValue": "17/4",
                                "fractionalValue": "9/2",
                                "sourceId": 2114984998,
                                "name": "1",
                                "winning": false,
                                "change": 1
                            },
                            {
                                "initialFractionalValue": "10/3",
                                "fractionalValue": "31/10",
                                "sourceId": 2114985000,
                                "name": "X",
                                "winning": false,
                                "change": -1
                            },
                            {
                                "initialFractionalValue": "53/100",
                                "fractionalValue": "57/100",
                                "sourceId": 2114985001,
                                "name": "2",
                                "winning": true,
                                "change": 1
                            }
                        ]
                    }
                },
                "hasMoreOdds": true
            }

        Raises:
            Exception: If the API request fails or returns an error.
        """
        return await self.api._get(f"/event/{self.match_id}/odds/1/featured")
    
    async def h2h(self) -> Dict[str, Any]:
        """
        Fetches the head-to-head (H2H) data for the teams involved in the specified match.

        Returns:
            Dict[str, Any]: A dictionary containing the head-to-head data. The structure includes:
                - teamDuel (Dict[str, int]): A dictionary representing the head-to-head results between the teams:
                    - homeWins (int): The number of wins for the home team.
                    - awayWins (int): The number of wins for the away team.
                    - draws (int): The number of draws between the teams.
                - managerDuel (Dict[str, int]): A dictionary representing the head-to-head results between the managers:
                    - homeWins (int): The number of wins for the home team's manager.
                    - awayWins (int): The number of wins for the away team's manager.
                    - draws (int): The number of draws between the managers.

        Example Response:
            .. code-block:: json
            {
                "teamDuel": {
                    "homeWins": 0,
                    "awayWins": 1,
                    "draws": 0
                },
                "managerDuel": {
                    "homeWins": 0,
                    "awayWins": 1,
                    "draws": 0
                }
            }

        Raises:
            Exception: If the API request fails or returns an error.
        """
        return await self.api._get(f"/event/{self.match_id}/h2h")
    
    async def incidents(self):
        """
        Retrieves important incidents during the match, including game status changes.

        This function returns a list of incidents that occurred in the match, such as 
        goals, substitutions, or other significant game events. Each incident contains 
        details such as the time, player involved (if applicable), description, and 
        game status (e.g., score updates, penalties).

        :returns: A dictionary containing a list of incidents with details about each 
                incident, including time, player, description, and the type of incident.
        :rtype: dict

        Example Response:
            .. code-block:: json

                {
                    "incidents": [
                        {
                            "text": "FT",
                            "homeScore": 1,
                            "awayScore": 2,
                            "isLive": false,
                            "time": 90,
                            "addedTime": 999,
                            "timeSeconds": 5400,
                            "reversedPeriodTime": 1,
                            "reversedPeriodTimeSeconds": 0,
                            "incidentType": "period"
                        },
                        {
                            "time": 90,
                            "player": {
                                "name": "Raheem Sterling",
                                "slug": "raheem-sterling",
                                "shortName": "R. Sterling",
                                "position": "M",
                                "jerseyNumber": "30",
                                "height": 170,
                                "userCount": 49508,
                                "id": 138534,
                                "marketValueCurrency": "EUR",
                                "dateOfBirthTimestamp": 786844800,
                                "proposedMarketValueRaw": {
                                    "value": 21000000,
                                    "currency": "EUR"
                                },
                                "fieldTranslations": {
                                    "nameTranslation": {
                                        "ar": "رحيم ستيرلينغ",
                                        "hi": "रहीम स्टर्लिंग",
                                        "bn": "রাহিম স্টার্লিং"
                                    },
                                    "shortNameTranslation": {
                                        "ar": "ر. سترلينغ",
                                        "hi": "आर. स्टर्लिंग",
                                        "bn": "আর. স্টার্লিং"
                                    }
                                }
                            },
                            "description": "Goalkeeper save",
                            "id": 118513874,
                            "addedTime": 3,
                            "incidentType": "inGamePenalty",
                            "isHome": false,
                            "incidentClass": "missed",
                            "reason": "goalkeeperSave",
                            "reversedPeriodTime": 1
                        }
                    ]
                }
        """
        return await self.api._get(f"/event/{self.match_id}/incidents")

    
    async def incidents(self) -> Dict[str, Any]:
        """
        Fetches the important incidents for the specified match, including game status changes and key events.

        Returns:
            Dict[str, Any]: A dictionary containing the incidents data. The structure includes:
                - incidents (List[Dict[str, Any]]): A list of incident objects, each containing:
                    - text (str): A description or label for the incident (e.g., "FT" for full-time).
                    - homeScore (int): The home team's score at the time of the incident.
                    - awayScore (int): The away team's score at the time of the incident.
                    - isLive (bool): Indicates if the match was live at the time of the incident.
                    - time (int): The time in minutes when the incident occurred.
                    - addedTime (int): The added or stoppage time when the incident occurred.
                    - timeSeconds (int): The time in seconds when the incident occurred.
                    - reversedPeriodTime (int): The reversed period time (e.g., 1 for first half, 2 for second half).
                    - reversedPeriodTimeSeconds (int): The reversed period time in seconds.
                    - incidentType (str): The type of incident (e.g., "period", "inGamePenalty").
                    - player (Dict[str, Any], optional): Details about the player involved in the incident, including:
                        - name (str): The player's full name.
                        - slug (str): The player's slug or unique identifier.
                        - shortName (str): The player's short name.
                        - position (str): The player's position on the field.
                        - jerseyNumber (str): The player's jersey number.
                        - height (int): The player's height in centimeters.
                        - userCount (int): The number of users following the player.
                        - id (int): The player's unique ID.
                        - marketValueCurrency (str): The currency of the player's market value.
                        - dateOfBirthTimestamp (int): The player's date of birth as a timestamp.
                        - proposedMarketValueRaw (Dict[str, Any]): The player's proposed market value, including:
                            - value (int): The market value amount.
                            - currency (str): The currency of the market value.
                        - fieldTranslations (Dict[str, Any]): Translations of the player's name and short name in various languages.
                    - description (str, optional): A description of the incident (e.g., "Goalkeeper save").
                    - id (int): The unique ID of the incident.
                    - isHome (bool, optional): Indicates if the incident involved the home team.
                    - incidentClass (str, optional): The class of the incident (e.g., "missed").
                    - reason (str, optional): The reason for the incident (e.g., "goalkeeperSave").

        Example Response:
            .. code-block:: json
            {
                "incidents": [
                    {
                        "text": "FT",
                        "homeScore": 1,
                        "awayScore": 2,
                        "isLive": false,
                        "time": 90,
                        "addedTime": 999,
                        "timeSeconds": 5400,
                        "reversedPeriodTime": 1,
                        "reversedPeriodTimeSeconds": 0,
                        "incidentType": "period"
                    },
                    {
                        "time": 90,
                        "player": {
                            "name": "Raheem Sterling",
                            "slug": "raheem-sterling",
                            "shortName": "R. Sterling",
                            "position": "M",
                            "jerseyNumber": "30",
                            "height": 170,
                            "userCount": 49508,
                            "id": 138534,
                            "marketValueCurrency": "EUR",
                            "dateOfBirthTimestamp": 786844800,
                            "proposedMarketValueRaw": {
                                "value": 21000000,
                                "currency": "EUR"
                            },
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "رحيم ستيرلينغ",
                                    "hi": "रहीम स्टर्लिंग",
                                    "bn": "রাহিম স্টার্লিং"
                                },
                                "shortNameTranslation": {
                                    "ar": "ر. سترلينغ",
                                    "hi": "आर. स्टर्लिंग",
                                    "bn": "আর. স্টার্লিং"
                                }
                            }
                        },
                        "description": "Goalkeeper save",
                        "id": 118513874,
                        "addedTime": 3,
                        "incidentType": "inGamePenalty",
                        "isHome": false,
                        "incidentClass": "missed",
                        "reason": "goalkeeperSave",
                        "reversedPeriodTime": 1
                    }
                ]
            }

        Raises:
            Exception: If the API request fails or returns an error.
        """
        return await self.api._get(f"/event/{self.match_id}/incidents")
    
    async def best_away_players(self) -> Optional[List[Dict[str, Any]]]:
        """
        Fetches the best-rated players of the away team for the specified match.

        Returns:
            Optional[List[Dict[str, Any]]]: A list of dictionaries containing the best-rated players of the away team.
                Each dictionary includes:
                    - value (str): The rating value of the player.
                    - label (str): The label for the value (e.g., "rating").
                    - player (Dict[str, Any]): Details about the player, including:
                        - name (str): The player's full name.
                        - slug (str): The player's slug or unique identifier.
                        - shortName (str): The player's short name.
                        - position (str): The player's position on the field.
                        - jerseyNumber (str): The player's jersey number.
                        - height (int): The player's height in centimeters.
                        - userCount (int): The number of users following the player.
                        - id (int): The player's unique ID.
                        - marketValueCurrency (str): The currency of the player's market value.
                        - dateOfBirthTimestamp (int): The player's date of birth as a timestamp.
                        - proposedMarketValueRaw (Dict[str, Any]): The player's proposed market value, including:
                            - value (int): The market value amount.
                            - currency (str): The currency of the market value.
                        - fieldTranslations (Dict[str, Any]): Translations of the player's name and short name in various languages.
                Returns `None` if no data is available.

        Example:
            [
                {
                    "value": "7.8",
                    "label": "rating",
                    "player": {
                        "name": "Pau López",
                        "slug": "pau-lopez",
                        "shortName": "P. López",
                        "position": "G",
                        "jerseyNumber": "25",
                        "height": 189,
                        "userCount": 1060,
                        "id": 548848,
                        "marketValueCurrency": "EUR",
                        "dateOfBirthTimestamp": 787276800,
                        "proposedMarketValueRaw": {
                            "value": 3700000,
                            "currency": "EUR"
                        },
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "باو لوبيز",
                                "hi": "पाऊ लोपेज़",
                                "bn": "পাউ লোপেজ"
                            },
                            "shortNameTranslation": {
                                "ar": "ب. لوبيز",
                                "hi": "पी. लोपेज़",
                                "bn": "পি. লোপেজ"
                            }
                        }
                    }
                }
            ]

        Raises:
            Exception: If the API request fails or returns an error.
        """
        data = await self.api._get(f"/event/{self.match_id}/best-players/summary")
        return data.get("bestAwayTeamPlayers", None)
    
    async def best_home_players(self) -> Optional[List[Dict[str, Any]]]:
        """
        Fetches the best-rated players of the Home team for the specified match.

        Returns:
            Optional[List[Dict[str, Any]]]: A list of dictionaries containing the best-rated players of the away team.
                Each dictionary includes:
                    - value (str): The rating value of the player.
                    - label (str): The label for the value (e.g., "rating").
                    - player (Dict[str, Any]): Details about the player, including:
                        - name (str): The player's full name.
                        - slug (str): The player's slug or unique identifier.
                        - shortName (str): The player's short name.
                        - position (str): The player's position on the field.
                        - jerseyNumber (str): The player's jersey number.
                        - height (int): The player's height in centimeters.
                        - userCount (int): The number of users following the player.
                        - id (int): The player's unique ID.
                        - marketValueCurrency (str): The currency of the player's market value.
                        - dateOfBirthTimestamp (int): The player's date of birth as a timestamp.
                        - proposedMarketValueRaw (Dict[str, Any]): The player's proposed market value, including:
                            - value (int): The market value amount.
                            - currency (str): The currency of the market value.
                        - fieldTranslations (Dict[str, Any]): Translations of the player's name and short name in various languages.
                Returns `None` if no data is available.

        Example:
            [
                {
                    "value": "7.8",
                    "label": "rating",
                    "player": {
                        "name": "Pau López",
                        "slug": "pau-lopez",
                        "shortName": "P. López",
                        "position": "G",
                        "jerseyNumber": "25",
                        "height": 189,
                        "userCount": 1060,
                        "id": 548848,
                        "marketValueCurrency": "EUR",
                        "dateOfBirthTimestamp": 787276800,
                        "proposedMarketValueRaw": {
                            "value": 3700000,
                            "currency": "EUR"
                        },
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "باو لوبيز",
                                "hi": "पाऊ लोपेज़",
                                "bn": "পাউ লোপেজ"
                            },
                            "shortNameTranslation": {
                                "ar": "ب. لوبيز",
                                "hi": "पी. लोपेज़",
                                "bn": "পি. লোপেজ"
                            }
                        }
                    }
                }
            ]

        Raises:
            Exception: If the API request fails or returns an error.
        """
        data = await self.api._get(f"/event/{self.match_id}/best-players/summary")
        return data.get("bestHomeTeamPlayers", None)
    
    async def motm(self) -> dict:
        """
        Get the Man of the Match (MOTM) for the given game.

        This function returns the player who was awarded Man of the Match based on the performance 
        in a given game. The result includes the player's details such as name, position, jersey 
        number, market value, and translations for the player's name in various languages.

        Example Response:
            .. code-block:: json
            {
                "value": "7.8",
                "label": "rating",
                "player": {
                    "name": "Pau López",
                    "slug": "pau-lopez",
                    "shortName": "P. López",
                    "position": "G",
                    "jerseyNumber": "25",
                    "height": 189,
                    "userCount": 1060,
                    "id": 548848,
                    "marketValueCurrency": "EUR",
                    "dateOfBirthTimestamp": 787276800,
                    "proposedMarketValueRaw": {
                        "value": 3700000,
                        "currency": "EUR"
                    },
                    "fieldTranslations": {
                        "nameTranslation": {
                            "ar": "باو لوبيز",
                            "hi": "पाऊ लोपेज़",
                            "bn": "পাউ লোপেজ"
                        },
                        "shortNameTranslation": {
                            "ar": "ب. لوبيز",
                            "hi": "पी. लोपेज़",
                            "bn": "পি. লোপেজ"
                        }
                    }
                }
            }

        Returns:
            dict: The player information for the Man of the Match, including player details and ratings.
            If no player of the match is found, it returns None.
        """
        data = await self.api._get(f"/event/{self.match_id}/best-players/summary")
        return data.get("playerOfTheMatch", None)


    async def votes(self) -> dict:
        """
        Get the SofaScore votes for the given match.

        This function returns various votes related to a match, including votes for the 
        most popular outcome (home win, away win, draw), as well as votes for specific 
        events, such as who will score first or whether both teams will score.

        Example Response:
            .. code-block:: json
            {
                "vote": {
                    "vote1": 8779,
                    "vote2": 98254,
                    "voteX": 11223
                },
                "bothTeamsToScoreVote": {
                    "voteYes": 16294,
                    "voteNo": 8891
                },
                "firstTeamToScoreVote": {
                    "voteHome": 2429,
                    "voteNoGoal": 404,
                    "voteAway": 20338
                },
                "whoShouldHaveWonVote": {
                    "vote1": 0,
                    "vote2": 0
                }
            }

        Returns:
            dict: A dictionary containing the vote results, including vote counts for 
            different match outcomes and events.
        """
        return await self.api._get(f"/event/{self.match_id}/votes")

    
    async def pre_match_form(self) -> dict:
        """
        Get the pre-match form of the two teams for the given game.

        This function returns the recent form of both the home and away teams, 
        along with their average ratings, position, and points value.

        Example Response:
            .. code-block:: json
            {
                "homeTeam": {
                    "avgRating": "6.81",
                    "position": 31,
                    "value": "3",
                    "form": [
                        "W",  # Win
                        "L",  # Loss
                        "L",  # Loss
                        "L",  # Loss
                        "L"   # Loss
                    ]
                },
                "awayTeam": {
                    "avgRating": "7.08",
                    "position": 3,
                    "value": "16",
                    "form": [
                        "W",  # Win
                        "L",  # Loss
                        "W",  # Win
                        "W",  # Win
                        "W"   # Win
                    ]
                },
                "label": "Pts"  # Label for the points value (optional)
            }

        Returns:
            dict: A dictionary containing the pre-match form data for both teams, 
            including their recent results, average ratings, and positions.
        """
        return await self.api._get(f"/event/{self.match_id}/pregame-form")

    
    async def match_channels(self) -> dict:
        """
        Get all the available channels for the given match, grouped by country code.

        This function returns a dictionary of available channels for a match based on 
        different country codes. The user can use `get_channel()` to fetch the channel names.

        Example Response:
            .. code-block:: json
            {
                "countryChannels": {
                    "TG": [2781, 3025, 644],  # Country code "TG" with channel IDs
                    "EN": [1234, 5678],        # Country code "EN" with channel IDs
                    "US": [9876, 5432]         # Country code "US" with channel IDs
                }
            }

        Returns:
            dict: A dictionary containing country codes as keys and a list of 
            channel IDs as values.
        """
        return await self.api._get(f"/tv/event/{self.match_id}/country-channels")

    
    async def get_channel(self, channel_id: int) -> str:
        """
        Get the channel name for the given channel ID.

        This function retrieves the name of a TV channel based on the provided channel ID 
        for a specific match. It returns the name of the channel if available.

        Example Response:
            .. code-block:: json
            "TV2 Play"  # The channel name corresponding to the channel ID.

        Args:
            channel_id (int): The ID of the TV channel for which the name is required.

        Returns:
            str: The name of the channel associated with the given channel ID, or None 
            if the channel name is not found.
        """
        data = await self.api._get(f"/tv/channel/{channel_id}/event/{self.match_id}/votes")
        return data.get("tvChannelVotes", {}).get("tvChannel", {}).get("name", None)

    
    async def managers(self) -> Dict:
        """
        Get the managers for the given match.

        This function retrieves the managers for the home and away teams in the 
        given match. It returns the managers' names, IDs, and translations in 
        different languages.

        :returns: A dictionary containing the home and away team managers' details, 
                including names, IDs, and translations in multiple languages.
        :rtype: dict

        Example Response:
            .. code-block:: json

                {
                    "homeManager": {
                        "name": "Michel",
                        "slug": "michel",
                        "shortName": "Michel",
                        "id": 788163,
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "ميشيل",
                                "hi": "मिशेल",
                                "bn": "মিশেল"
                            },
                            "shortNameTranslation": {
                                "ar": "ميشيل",
                                "hi": "मिशेल",
                                "bn": "মিশেল"
                            }
                        }
                    },
                    "awayManager": {
                        "name": "Mikel Arteta",
                        "slug": "mikel-arteta",
                        "shortName": "M. Arteta",
                        "id": 794075,
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "ميكيل أرتيتا",
                                "hi": "मिकेल आर्टेटा",
                                "bn": "মিকেল আর্তেতা"
                            },
                            "shortNameTranslation": {
                                "ar": "م. أرتيتا",
                                "hi": "एम. आर्टेटा",
                                "bn": "এম. আরতেতা"
                            }
                        }
                    }
                }
        """
        return await self.api._get(f"/event/{self.match_id}/managers")

    
    async def lineups_home(self) -> Dict:
        """
        Get the lineup of the home team for the given match.

        This function retrieves the confirmed lineup of the home team, including 
        details of the players such as name, position, jersey number, market value, 
        and translations in different languages.

        :returns: A dictionary containing the home team's confirmed lineup and 
                details of each player, including player name, position, 
                jersey number, country, market value, and translations.
        :rtype: dict

        Example Response:
            .. code-block:: json
                {
                    "confirmed": true,
                    "players": [
                        {
                            "player": {
                                "name": "Pau López",
                                "slug": "pau-lopez",
                                "shortName": "P. López",
                                "position": "G",
                                "jerseyNumber": "25",
                                "height": 189,
                                "userCount": 1060,
                                "id": 548848,
                                "country": {
                                    "alpha2": "ES",
                                    "alpha3": "ESP",
                                    "name": "Spain",
                                    "slug": "spain"
                                },
                                "marketValueCurrency": "EUR",
                                "dateOfBirthTimestamp": 787276800,
                                "proposedMarketValueRaw": {
                                    "value": 3700000,
                                    "currency": "EUR"
                                },
                                "fieldTranslations": {
                                    "nameTranslation": {
                                        "ar": "باو لوبيز",
                                        "hi": "पाऊ लोपेज़",
                                        "bn": "পাউ লোপেজ"
                                    },
                                    "shortNameTranslation": {
                                        "ar": "ب. لوبيز",
                                        "hi": "पी. लोपेज़",
                                        "bn": "পি. লোপেজ"
                                    }
                                }
                            }
                        }
                    ]
                }
        """
        data = await self.api._get(f"/event/{self.match_id}/lineups")
        return {
            "confirmed": data["confirmed"],
            "players": data["home"]["players"]
        }


    async def lineups_away(self) -> Dict:
        """
        Get the lineup of the away team for the given match.

        This function retrieves the confirmed lineup of the away team, including 
        details of the players such as name, position, jersey number, market value, 
        and translations in different languages.

        :returns: A dictionary containing the away team's confirmed lineup and 
                details of each player, including player name, position, 
                jersey number, country, market value, and translations.
        :rtype: dict

        Example Response:
            .. code-block:: json

                {
                    "confirmed": true,
                    "players": [
                        {
                            "player": {
                                "name": "Pau López",
                                "slug": "pau-lopez",
                                "shortName": "P. López",
                                "position": "G",
                                "jerseyNumber": "25",
                                "height": 189,
                                "userCount": 1060,
                                "id": 548848,
                                "country": {
                                    "alpha2": "ES",
                                    "alpha3": "ESP",
                                    "name": "Spain",
                                    "slug": "spain"
                                },
                                "marketValueCurrency": "EUR",
                                "dateOfBirthTimestamp": 787276800,
                                "proposedMarketValueRaw": {
                                    "value": 3700000,
                                    "currency": "EUR"
                                },
                                "fieldTranslations": {
                                    "nameTranslation": {
                                        "ar": "باو لوبيز",
                                        "hi": "पाऊ लोपेज़",
                                        "bn": "পাউ লোপেজ"
                                    },
                                    "shortNameTranslation": {
                                        "ar": "ب. لوبيز",
                                        "hi": "पी. लोपेज़",
                                        "bn": "পি. লোপেজ"
                                    }
                                }
                            }
                        }
                    ]
                }
        """
        data = await self.api._get(f"/event/{self.match_id}/lineups")
        return {
            "confirmed": data["confirmed"],
            "players": data["away"]["players"]
        }



    async def shotmap(self) -> Dict:
        """
        Retrieves the shot map for the given match.

        This function returns a list of shot events that occurred during the match, 
        including details about each shot, such as the player who took the shot, 
        the shot type, situation, coordinates, expected goal (xG), and other 
        relevant information such as body part used and goal mouth location.

        :returns: A dictionary containing a list of shot events, including player information, 
                shot type, coordinates, xG value, and additional shot data.
        :rtype: dict

        Example Response:
            .. code-block:: json

                {
                    "shotmap": [
                        {
                            "player": {
                                "name": "Mikel Merino",
                                "slug": "mikel-merino",
                                "shortName": "M. Merino",
                                "position": "M",
                                "jerseyNumber": "23",
                                "userCount": 7943,
                                "id": 592010,
                                "fieldTranslations": {
                                    "nameTranslation": {
                                        "ar": "ميكيل ميرينو",
                                        "hi": "मिकेल मेरिनो",
                                        "bn": "মাইকেল মেরিনো"
                                    },
                                    "shortNameTranslation": {
                                        "ar": "م. ميرينو",
                                        "hi": "एम. मेरिनो",
                                        "bn": "এম. মেরিনো"
                                    }
                                }
                            },
                            "isHome": false,
                            "shotType": "block",
                            "situation": "assisted",
                            "playerCoordinates": {
                                "x": 15.8,
                                "y": 33.6,
                                "z": 0
                            },
                            "bodyPart": "left-foot",
                            "goalMouthLocation": "low-centre",
                            "goalMouthCoordinates": {
                                "x": 0,
                                "y": 50.3,
                                "z": 19
                            },
                            "blockCoordinates": {
                                "x": 11.8,
                                "y": 37.7,
                                "z": 0
                            },
                            "xg": 0.073860235512257,
                            "xgot": 0,
                            "id": 4347934,
                            "time": 90,
                            "addedTime": 4,
                            "timeSeconds": 5637,
                            "draw": {
                                "start": {
                                    "x": 33.6,
                                    "y": 15.8
                                },
                                "block": {
                                    "x": 37.7,
                                    "y": 11.8
                                },
                                "end": {
                                    "x": 49.7,
                                    "y": 0
                                },
                                "goal": {
                                    "x": 49.7,
                                    "y": 81
                                }
                            },
                            "reversedPeriodTime": 1,
                            "reversedPeriodTimeSeconds": 663,
                            "incidentType": "shot"
                        }
                    ]
                }
        """
        return await self.api._get(f"/event/{self.match_id}/shotmap")


    
    async def heatmap(self, team_id: int) -> Dict:
        """
        Retrieves the heatmap data for the given team in the specified match.

        The heatmap contains the coordinates of player activity during the match, 
        represented by points on the field. This data provides insights into the 
        movement and positioning of players on the field.

        :param team_id: The ID of the team for which the heatmap is to be fetched.
        :type team_id: int
        :returns: A dictionary containing the heatmap data with player points, each represented by x and y coordinates.
        :rtype: dict

        Example Response:
            .. code-block:: json
            {
                "playerPoints": [
                    {
                        "x": 55.3,
                        "y": 10.3
                    },
                    {
                        "x": 40.5,
                        "y": 30.2
                    },
                    ...
                ]
            }
        """
        return await self.api._get(f"/event/{self.match_id}/heatmap/{team_id}")


    async def stats(self):
        """
        Retrieves the statistics for the game.

        This function returns detailed statistics for the match, including various 
        performance metrics for both teams (e.g., ball possession, shots, etc.), 
        grouped by categories such as "Match overview".

        :returns: A dictionary containing the match statistics, with grouped statistics 
                for home and away teams.
        :rtype: dict

        Example Response:
            .. code-block:: json

                {
                    "statistics": [
                        {
                            "period": "ALL",
                            "groups": [
                                {
                                    "groupName": "Match overview",
                                    "statisticsItems": [
                                        {
                                            "name": "Ball possession",
                                            "home": "39%",
                                            "away": "61%",
                                            "compareCode": 2,
                                            "statisticsType": "positive",
                                            "valueType": "event",
                                            "homeValue": 39,
                                            "awayValue": 61,
                                            "renderType": 2,
                                            "key": "ballPossession"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
        """
        return await self.api._get(f"/event/{self.match_id}/statistics")

        
    async def stats(self) -> Dict:
        """
        Retrieves the statistics for the given game.

        The statistics provide a detailed overview of various match metrics, such as ball possession, 
        shots, and other performance indicators for both teams.

        Example Response:
            .. code-block:: json
            {
            "statistics": [
                {
                "period": "ALL",
                "groups": [
                    {
                    "groupName": "Match overview",
                    "statisticsItems": [
                        {
                        "name": "Ball possession",
                        "home": "39%",
                        "away": "61%",
                        "compareCode": 2,
                        "statisticsType": "positive",
                        "valueType": "event",
                        "homeValue": 39,
                        "awayValue": 61,
                        "renderType": 2,
                        "key": "ballPossession"
                        },
                        ...
                    ]
                    },
                    ...
                ]
                }
            ]
            }

        Returns:
            dict: A dictionary containing the statistics for the match, including various categories like 
                "Match overview", and performance indicators for both home and away teams.
        """
        return await self.api._get(f"/event/{self.match_id}/statistics")

    
    async def highlight(self) -> Dict:
        """
        Retrieves a match highlight video for the given game.

        :returns: A dictionary containing a list of highlights for the match. Each highlight contains the 
                video title, subtitle, URL, thumbnail, and additional metadata like whether it's a key highlight.
        :rtype: dict

        Example Response:
            .. code-block:: json

                {
                    "highlights": [
                        {
                            "title": "Girona FC 1-2 Arsenal",
                            "subtitle": "Full Highlights",
                            "url": "https://youtu.be/3C0wBjYhqLE",
                            "thumbnailUrl": "https://i.ytimg.com/vi/3C0wBjYhqLE/hqdefault.jpg",
                            "mediaType": 1,
                            "doFollow": false,
                            "keyHighlight": true,
                            "id": 6209847,
                            "createdAtTimestamp": 1738195753,
                            "sourceUrl": "https://youtu.be/3C0wBjYhqLE"
                        }
                    ]
                }
        """
        return await self.api._get(f"/event/{self.match_id}/highlights")
    
    async def commentary(self) -> Dict[str, int]:
        """
        Retrieves commentary and highlights for the given match.

        This function fetches the live commentary and highlights for a specific match,
        including text comments such as match events, player actions, and game status updates.

        :returns: A dictionary containing a list of commentary objects, each of which includes details about
                the comment, type, time, and optionally player information.
        :rtype: dict

        Example Response:
            .. code-block:: json

                {
                    "comments": [
                        {
                            "text": "Match ends, Girona 1, Arsenal 2.",
                            "type": "matchEnded",
                            "id": 27698855,
                            "time": 0
                        },
                        {
                            "text": "Second Half ends, Girona 1, Arsenal 2.",
                            "type": "endSecondHalf",
                            "id": 27698807,
                            "periodName": "2ND",
                            "time": 96
                        },
                        {
                            "text": "Foul by Cristhian Stuani (Girona).",
                            "type": "freeKickLost",
                            "isHome": true,
                            "player": {
                                "name": "Cristhian Stuani",
                                "slug": "cristhian-stuani",
                                "shortName": "C. Stuani",
                                "position": "F",
                                "jerseyNumber": "7",
                                "height": 184,
                                "userCount": 1757,
                                "id": 32048,
                                "marketValueCurrency": "EUR",
                                "dateOfBirthTimestamp": 529459200,
                                "proposedMarketValueRaw": {
                                    "value": 1100000,
                                    "currency": "EUR"
                                },
                                "fieldTranslations": {
                                    "nameTranslation": {
                                        "ar": "كريستيان ستواني",
                                        "hi": "क्रिस्टियन स्टुआनी",
                                        "bn": "ক্রিশ্চিয়ান স্টুয়ানি"
                                    },
                                    "shortNameTranslation": {
                                        "ar": "ك. ستواني",
                                        "hi": "सी. स्टुआनी",
                                        "bn": "সি. স্টুয়ানি"
                                    }
                                }
                            },
                            "id": 27698809,
                            "periodName": "2ND",
                            "time": 96
                        }
                    ]
                }

        Commentary Object Details:
            - ``text``: The text of the commentary, describing the match event or action.
            - ``type``: The type of comment (e.g., "matchEnded", "freeKickLost").
            - ``id``: Unique identifier for the comment.
            - ``time``: The time (in seconds) when the comment occurred in the match.
            - ``periodName`` (optional): The name of the period, such as "1ST", "2ND".
            - ``isHome`` (optional): Boolean indicating if the event relates to the home team.
            - ``player`` (optional): Player information for player-related events.
                - ``name``: Player's full name.
                - ``slug``: URL-friendly identifier for the player.
                - ``shortName``: Shortened player name.
                - ``position``: Player's position (e.g., "F" for forward).
                - ``jerseyNumber``: Player's jersey number.
                - ``height``: Player's height in centimeters.
                - ``marketValueCurrency``: The currency for the player's market value.
                - ``proposedMarketValueRaw``: Proposed market value for the player, including currency.
                - ``fieldTranslations``: Translations for the player's name and short name in different languages.
            """
        return await self.api._get(f"/event/{self.match_id}/comments")



    
