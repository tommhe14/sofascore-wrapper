from .api import SofascoreAPI
from typing import Dict, List, Any, Literal

class Team:
    def __init__(self, api: SofascoreAPI, team_id: int):
        """
        Initializes the Team class with the SofascoreAPI instance and team ID.

        Args:
            api (SofascoreAPI): An instance of the SofascoreAPI class.
            team_id (int): The unique identifier for the team.
        """
        self.api = api
        self.team_id = team_id

    async def get_team(self) -> Dict:
        """
        Retrieves detailed information about the team.

        Returns:
            Dict: A dictionary containing team details such as name, slug, short name, gender, sport, category, tournament, and more.

        Example Response:
            .. code-block:: json
            {
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
                            "displayInverseHomeAwayTeams": false,
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "الدوري الإنجليزي الممتاز",
                                    "hi": "प्रिमियर लीग",
                                    "bn": "প্রিমিয়ার লীग"
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
                    "primaryUniqueTournament": {
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
                        "displayInverseHomeAwayTeams": false,
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "الدوري الإنجليزي الممتاز",
                                "hi": "प्रिमियर लीग",
                                "bn": "প্রিমিয়ার লীग"
                            },
                            "shortNameTranslation": {}
                        }
                    },
                    "userCount": 2341486,
                    "manager": {
                        "name": "Mikel Arteta",
                        "slug": "mikel-arteta",
                        "shortName": "M. Arteta",
                        "id": 794075,
                        "country": {
                            "alpha2": "ES",
                            "alpha3": "ESP",
                            "name": "Spain",
                            "slug": "spain"
                        },
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
                    },
                    "venue": {
                        "city": {
                            "name": "London"
                        },
                        "venueCoordinates": {
                            "latitude": 51.55504,
                            "longitude": -0.1084
                        },
                        "hidden": false,
                        "slug": "emirates-stadium",
                        "name": "Emirates Stadium",
                        "capacity": 60260,
                        "id": 624,
                        "country": {
                            "alpha2": "EN",
                            "alpha3": "ENG",
                            "name": "England",
                            "slug": "england"
                        },
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "الإمارات"
                            },
                            "shortNameTranslation": {}
                        },
                        "stadium": {
                            "name": "Emirates Stadium",
                            "capacity": 60260
                        }
                    },
                    "nameCode": "ARS",
                    "class": 4,
                    "disabled": false,
                    "national": false,
                    "type": 0,
                    "id": 42,
                    "country": {
                        "alpha2": "EN",
                        "alpha3": "ENG",
                        "name": "England",
                        "slug": "england"
                    },
                    "entityType": "team",
                    "fullName": "Arsenal",
                    "teamColors": {
                        "primary": "#cc0000",
                        "secondary": "#ffffff",
                        "text": "#ffffff"
                    },
                    "foundationDateTimestamp": -2627164800,
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
                "pregameForm": {
                    "avgRating": "7.04",
                    "position": 2,
                    "value": "47",
                    "form": [
                        "W",
                        "D",
                        "W",
                        "D",
                        "W"
                    ]
                }
            }
        """
        return await self.api._get(f"/team/{self.team_id}")

    async def image(self) -> str:
        """
        Retrieves the URL of the team's image.

        Returns:
            str: The URL of the team's image.

        Example Response:
            .. code-block:: json
            "https://img.sofascore.com/api/v1/team/42/image"
        """
        return f"https://img.sofascore.com/api/v1/team/{self.team_id}/image"

    async def performance(self) -> Dict:
        """
        Retrieves the performance data of the team.

        Returns:
            Dict: A dictionary containing performance data such as events, tournament details, and team statistics.

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
                                "hasEventPlayerStatistics": true,
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
                            "isGroup": false,
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
                        "season": {
                            "name": "Premier League 24/25",
                            "year": "24/25",
                            "editor": false,
                            "id": 61627
                        },
                        "roundInfo": {
                            "round": 18
                        },
                        "customId": "HsR",
                        "status": {
                            "code": 100,
                            "description": "Ended",
                            "type": "finished"
                        },
                        "winnerCode": 1,
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
                            "name": "Ipswich Town",
                            "slug": "ipswich-town",
                            "shortName": "Ipswich",
                            "gender": "M",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 154510,
                            "nameCode": "IPS",
                            "disabled": false,
                            "national": false,
                            "type": 0,
                            "id": 32,
                            "entityType": "team",
                            "subTeams": [],
                            "teamColors": {
                                "primary": "#0000ff",
                                "secondary": "#ffffff",
                                "text": "#ffffff"
                            },
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "ايبسويتش تاون",
                                    "ru": "Ипсвич Таун"
                                },
                                "shortNameTranslation": {}
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
                            "current": 0,
                            "display": 0,
                            "period1": 0,
                            "period2": 0,
                            "normaltime": 0
                        },
                        "time": {
                            "injuryTime1": 1,
                            "injuryTime2": 4,
                            "currentPeriodStartTimestamp": 1735334227
                        },
                        "changes": {
                            "changes": [
                                "status.code",
                                "status.description",
                                "status.type"
                            ],
                            "changeTimestamp": 1735337210
                        },
                        "hasGlobalHighlights": false,
                        "hasXg": true,
                        "hasEventPlayerStatistics": true,
                        "hasEventPlayerHeatMap": true,
                        "detailId": 1,
                        "crowdsourcingDataDisplayEnabled": false,
                        "id": 12436472,
                        "startTimestamp": 1735330500,
                        "slug": "arsenal-ipswich-town",
                        "finalResultOnly": false,
                        "feedLocked": true,
                        "isEditor": false
                    }
                ]
            }
        """
        return await self.api._get(f"/team/{self.team_id}/performance")

    async def transfers_in(self) -> List:
        """
        Retrieves a list of players who have transferred into the team.

        Returns:
            List: A list of dictionaries containing details about each transfer, including player information, transfer details, and fees.

        Example Response:
            .. code-block:: json
            [
                {
                    "player": {
                        "name": "Charles Sagoe Jr.",
                        "slug": "charles-sagoe-jr",
                        "shortName": "C. S. Jr.",
                        "position": "F",
                        "jerseyNumber": "15",
                        "userCount": 841,
                        "id": 1119436,
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "تشارلز ساغو جونيور",
                                "hi": "चार्ल्स सागो जूनियर.",
                                "bn": "চার্লস সাগো জুনিয়র"
                            },
                            "shortNameTranslation": {
                                "ar": "ت. ساغو جونيور",
                                "hi": "सी.एस. जूनियर.",
                                "bn": "সি. এস. জুনিয়র"
                            }
                        }
                    },
                    "transferFrom": {
                        "name": "Shrewsbury Town",
                        "slug": "shrewsbury-town",
                        "shortName": "Shrewsbury",
                        "gender": "M",
                        "sport": {
                            "name": "Football",
                            "slug": "football",
                            "id": 1
                        },
                        "userCount": 6164,
                        "nameCode": "SHR",
                        "national": false,
                        "type": 0,
                        "id": 82,
                        "entityType": "team",
                        "teamColors": {
                            "primary": "#0000ff",
                            "secondary": "#ffff00",
                            "text": "#ffff00"
                        },
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "شوروسبري تاون",
                                "ru": "Шрусбери Таун"
                            },
                            "shortNameTranslation": {}
                        }
                    },
                    "transferTo": {
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
                    "fromTeamName": "Shrewsbury Town",
                    "toTeamName": "Arsenal",
                    "type": 2,
                    "transferFee": 0,
                    "transferFeeDescription": "-",
                    "id": 2131805,
                    "transferDateTimestamp": 1736121600,
                    "transferFeeRaw": {
                        "value": 0,
                        "currency": "EUR"
                    }
                }
            ]
        """
        data = await self.api._get(f"/team/{self.team_id}/transfers")
        data["transfersIn"].reverse()  
        return data["transfersIn"]

    async def transfers_out(self) -> List:
        """
        Retrieves a list of players who have transferred out of the team.

        Returns:
            List: A list of dictionaries containing details about each transfer, including player information, transfer details, and fees.

        Example Response:
            .. code-block:: json
            [
                {
                    "player": {
                        "name": "Marquinhos",
                        "firstName": "Marquinhos",
                        "slug": "marquinhos",
                        "shortName": "Marquinhos",
                        "position": "M",
                        "jerseyNumber": "17",
                        "userCount": 4202,
                        "id": 1116954,
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "ماركينيوس",
                                "hi": "मार्क्विन्होस",
                                "bn": "মারকুইনহোস"
                            },
                            "shortNameTranslation": {
                                "ar": "ماركينيوس",
                                "hi": "मार्क्विन्होस",
                                "bn": "মারকুইনহোস"
                            }
                        }
                    },
                    "transferFrom": {
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
                        "disabled": False,
                        "national": False,
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
                    "transferTo": {
                        "name": "Cruzeiro",
                        "slug": "cruzeiro",
                        "shortName": "Cruzeiro",
                        "gender": "M",
                        "sport": {
                            "name": "Football",
                            "slug": "football",
                            "id": 1
                        },
                        "userCount": 248252,
                        "nameCode": "CRU",
                        "disabled": False,
                        "national": False,
                        "type": 0,
                        "id": 1954,
                        "entityType": "team",
                        "teamColors": {
                            "primary": "#0033cc",
                            "secondary": "#0033cc",
                            "text": "#0033cc"
                        },
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ru": "Крузейро"
                            },
                            "shortNameTranslation": {}
                        }
                    },
                    "fromTeamName": "Arsenal",
                    "toTeamName": "Cruzeiro",
                    "type": 1,
                    "transferFee": 0,
                    "transferFeeDescription": "-",
                    "id": 2234559,
                    "transferDateTimestamp": 1736380800,
                    "transferFeeRaw": {
                        "value": 0,
                        "currency": "USD"
                    }
                }
            ]
        """
        data = await self.api._get(f"/team/{self.team_id}/transfers")
        data["transfersOut"].reverse()  
        return data["transfersOut"]


    async def next_fixtures(self) -> List:
        """
        Retrieves the next fixtures for the team.

        Returns:
            List: A list of dictionaries containing details about the upcoming fixtures, including tournament, season, round, teams, scores, and more.

        Example Response:
            .. code-block:: json
            [
                {
                    "tournament": {
                        "name": "EFL Cup",
                        "slug": "efl-cup",
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
                            "name": "EFL Cup",
                            "slug": "efl-cup",
                            "primaryColorHex": "#203e93",
                            "secondaryColorHex": "#bc1723",
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
                            "userCount": 167174,
                            "id": 21,
                            "country": {},
                            "hasPerformanceGraphFeature": false,
                            "hasEventPlayerStatistics": true,
                            "displayInverseHomeAwayTeams": false
                        },
                        "priority": 426,
                        "isGroup": false,
                        "isLive": false,
                        "id": 17
                    },
                    "season": {
                        "name": "EFL Cup 24/25",
                        "year": "24/25",
                        "editor": false,
                        "id": 62483
                    },
                    "roundInfo": {
                        "round": 3,
                        "name": "Round 3",
                        "slug": "round-3"
                    },
                    "customId": "fsR",
                    "status": {
                        "code": 100,
                        "description": "Ended",
                        "type": "finished"
                    },
                    "winnerCode": 1,
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
                            "alpha3": "ENG",
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
                        "name": "Bolton Wanderers",
                        "slug": "bolton-wanderers",
                        "shortName": "Bolton",
                        "gender": "M",
                        "sport": {
                            "name": "Football",
                            "slug": "football",
                            "id": 1
                        },
                        "userCount": 21304,
                        "nameCode": "BOL",
                        "disabled": false,
                        "national": false,
                        "type": 0,
                        "id": 5,
                        "country": {
                            "alpha2": "EN",
                            "alpha3": "ENG",
                            "name": "England",
                            "slug": "england"
                        },
                        "entityType": "team",
                        "subTeams": [],
                        "teamColors": {
                            "primary": "#ffffff",
                            "secondary": "#000033",
                            "text": "#000033"
                        },
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "بولتون وانديريرز",
                                "ru": "Болтон Уондерерс"
                            },
                            "shortNameTranslation": {}
                        }
                    },
                    "homeScore": {
                        "current": 5,
                        "display": 5,
                        "period1": 2,
                        "period2": 3,
                        "normaltime": 5
                    },
                    "awayScore": {
                        "current": 1,
                        "display": 1,
                        "period1": 0,
                        "period2": 1,
                        "normaltime": 1
                    },
                    "time": {
                        "injuryTime1": 3,
                        "injuryTime2": 4,
                        "currentPeriodStartTimestamp": 1727293717
                    },
                    "changes": {
                        "changes": [
                            "status.code",
                            "status.description",
                            "status.type"
                        ],
                        "changeTimestamp": 1727296678
                    },
                    "hasGlobalHighlights": false,
                    "hasEventPlayerStatistics": true,
                    "hasEventPlayerHeatMap": true,
                    "detailId": 1,
                    "crowdsourcingDataDisplayEnabled": false,
                    "id": 12785412,
                    "startTimestamp": 1727289900,
                    "slug": "arsenal-bolton-wanderers",
                    "finalResultOnly": false,
                    "feedLocked": true,
                    "isEditor": false
                }
            ]
        """
        data = await self.api._get(f"/team/{self.team_id}/events/next/0")
        data["events"].reverse()  
        return data["events"]

    async def last_fixtures(self) -> List:
        """
        Retrieves the last fixtures for the team.

        Returns:
            List: A list of dictionaries containing details about the past fixtures, including tournament, season, round, teams, scores, and more.

        Example Response:
            .. code-block:: json
            [
                {
                    "tournament": {
                        "name": "EFL Cup",
                        "slug": "efl-cup",
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
                            "name": "EFL Cup",
                            "slug": "efl-cup",
                            "primaryColorHex": "#203e93",
                            "secondaryColorHex": "#bc1723",
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
                            "userCount": 167174,
                            "id": 21,
                            "country": {},
                            "hasPerformanceGraphFeature": false,
                            "hasEventPlayerStatistics": true,
                            "displayInverseHomeAwayTeams": false
                        },
                        "priority": 426,
                        "isGroup": false,
                        "isLive": false,
                        "id": 17
                    },
                    "season": {
                        "name": "EFL Cup 24/25",
                        "year": "24/25",
                        "editor": false,
                        "id": 62483
                    },
                    "roundInfo": {
                        "round": 3,
                        "name": "Round 3",
                        "slug": "round-3"
                    },
                    "customId": "fsR",
                    "status": {
                        "code": 100,
                        "description": "Ended",
                        "type": "finished"
                    },
                    "winnerCode": 1,
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
                            "alpha3": "ENG",
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
                        "name": "Bolton Wanderers",
                        "slug": "bolton-wanderers",
                        "shortName": "Bolton",
                        "gender": "M",
                        "sport": {
                            "name": "Football",
                            "slug": "football",
                            "id": 1
                        },
                        "userCount": 21304,
                        "nameCode": "BOL",
                        "disabled": false,
                        "national": false,
                        "type": 0,
                        "id": 5,
                        "country": {
                            "alpha2": "EN",
                            "alpha3": "ENG",
                            "name": "England",
                            "slug": "england"
                        },
                        "entityType": "team",
                        "subTeams": [],
                        "teamColors": {
                            "primary": "#ffffff",
                            "secondary": "#000033",
                            "text": "#000033"
                        },
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "بولتون وانديريرز",
                                "ru": "Болтон Уондерерс"
                            },
                            "shortNameTranslation": {}
                        }
                    },
                    "homeScore": {
                        "current": 5,
                        "display": 5,
                        "period1": 2,
                        "period2": 3,
                        "normaltime": 5
                    },
                    "awayScore": {
                        "current": 1,
                        "display": 1,
                        "period1": 0,
                        "period2": 1,
                        "normaltime": 1
                    },
                    "time": {
                        "injuryTime1": 3,
                        "injuryTime2": 4,
                        "currentPeriodStartTimestamp": 1727293717
                    },
                    "changes": {
                        "changes": [
                            "status.code",
                            "status.description",
                            "status.type"
                        ],
                        "changeTimestamp": 1727296678
                    },
                    "hasGlobalHighlights": false,
                    "hasEventPlayerStatistics": true,
                    "hasEventPlayerHeatMap": true,
                    "detailId": 1,
                    "crowdsourcingDataDisplayEnabled": false,
                    "id": 12785412,
                    "startTimestamp": 1727289900,
                    "slug": "arsenal-bolton-wanderers",
                    "finalResultOnly": false,
                    "feedLocked": true,
                    "isEditor": false
                }
            ]
        """
        data = await self.api._get(f"/team/{self.team_id}/events/last/0")
        data["events"].reverse()  
        return data["events"]

    async def seasons(self) -> Dict:
        """
        Retrieves the seasons in which the team has participated.

        Returns:
            Dict: A dictionary containing the unique tournament seasons.

        Example Response:
            .. code-block:: json
            {
                "uniqueTournamentSeasons": [
                    {
                        "uniqueTournament": {
                            "name": "UEFA Champions League",
                            "slug": "uefa-champions-league",
                            "primaryColorHex": "#062b5c",
                            "secondaryColorHex": "#086aab",
                            "category": {
                                "name": "Europe",
                                "slug": "europe",
                                "sport": {
                                    "name": "Football",
                                    "slug": "football",
                                    "id": 1
                                },
                                "id": 1465,
                                "flag": "europe"
                            },
                            "userCount": 1321299,
                            "id": 7,
                            "displayInverseHomeAwayTeams": false,
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "دوري أبطال أوروبا",
                                    "hi": "यूईएफए चैंपियंस लीग",
                                    "bn": "উয়েফা চ্যাম্পিয়ন্স লীগ"
                                },
                                "shortNameTranslation": {}
                            }
                        },
                        "seasons": [
                            {
                                "name": "UEFA Champions League 24/25",
                                "year": "24/25",
                                "editor": false,
                                "seasonCoverageInfo": {},
                                "id": 61644
                            }
                        ]
                    }
                ]
            }
        """
        return await self.api._get(f"/team/{self.team_id}/team-statistics/seasons")

    async def squad(self) -> Dict:
        """
        Retrieves the squad of the team.

        Returns:
            Dict: A dictionary containing the players in the team's squad, including their details, positions, and statistics.

        Example Response:
            .. code-block:: json
            {
                "players": [
                    {
                        "player": {
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
                                "primaryUniqueTournament": {
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
                                "userCount": 2341486,
                                "nameCode": "ARS",
                                "disabled": false,
                                "national": false,
                                "type": 0,
                                "id": 42,
                                "country": {
                                    "alpha2": "EN",
                                    "alpha3": "ENG",
                                    "name": "England",
                                    "slug": "england"
                                },
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
                            "position": "F",
                            "jerseyNumber": "7",
                            "height": 178,
                            "preferredFoot": "Left",
                            "retired": false,
                            "userCount": 168684,
                            "gender": "M",
                            "id": 934235,
                            "country": {
                                "alpha2": "EN",
                                "alpha3": "ENG",
                                "name": "England",
                                "slug": "england"
                            },
                            "shirtNumber": 7,
                            "dateOfBirthTimestamp": 999648000,
                            "contractUntilTimestamp": 1814313600,
                            "proposedMarketValue": 157000000,
                            "proposedMarketValueRaw": {
                                "value": 157000000,
                                "currency": "EUR"
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
                        }
                    }
                ]
            }
        """
        return await self.api._get(f"/team/{self.team_id}/players")

    async def top_players(self, league_id: int, season: int) -> Dict:
        """
        Retrieves the top players of the team for a specific league and season.

        Args:
            league_id (int): The unique identifier for the league.
            season (int): The season year.

        Returns:
            Dict: A dictionary containing the top players of the team, including their statistics and performance metrics.

        Example Response:
            .. code-block:: json
            {
                "topPlayers": {
                    "rating": [
                        {
                            "statistics": {
                                "rating": 7.8,
                                "id": 1595229,
                                "type": "overall",
                                "appearances": 5
                            },
                            "playedEnough": true,
                            "player": {
                                "name": "Bukayo Saka",
                                "slug": "bukayo-saka",
                                "shortName": "B. Saka",
                                "position": "F",
                                "userCount": 168684,
                                "id": 934235,
                                "fieldTranslations": {
                                    "nameTranslation": {
                                        "ar": "بوكايو ساكا",
                                        "hi": "बुकायो साका",
                                        "bn": "বুকায়ো সাকা"
                                    },
                                    "shortNameTranslation": {
                                        "ar": "ب. ساكা",
                                        "hi": "बी. साका",
                                        "bn": "বি. সাকা"
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        """
        return await self.api._get(f"/team/{self.team_id}/unique-tournament/{league_id}/season/{season}/top-players/overall")

    async def league_stats(self, league_id: int, season: int) -> Dict:
        """
        Retrieves the league statistics of the team for a specific league and season.

        Args:
            league_id (int): The unique identifier for the league.
            season (int): The season year.

        Returns:
            Dict: A dictionary containing the team's statistics in the league, including goals scored, goals conceded, assists, shots, and more.

        Example Response:
            .. code-block:: json
            {
                "statistics": {
                    "goalsScored": 16,
                    "goalsConceded": 3,
                    "ownGoals": 0,
                    "assists": 9,
                    "shots": 107,
                    "penaltyGoals": 2,
                    "penaltiesTaken": 4,
                    "freeKickGoals": 1,
                    "freeKickShots": 2,
                    "goalsFromInsideTheBox": 13,
                    "goalsFromOutsideTheBox": 2,
                    "shotsFromInsideTheBox": 83,
                    "shotsFromOutsideTheBox": 24,
                    "headedGoals": 4,
                    "leftFootGoals": 7,
                    "rightFootGoals": 4,
                    "bigChances": 27,
                    "bigChancesCreated": 17,
                    "bigChancesMissed": 15,
                    "shotsOnTarget": 43,
                    "shotsOffTarget": 35,
                    "blockedScoringAttempt": 29,
                    "successfulDribbles": 79,
                    "dribbleAttempts": 153,
                    "corners": 51,
                    "hitWoodwork": 2,
                    "fastBreaks": 3,
                    "fastBreakGoals": 0,
                    "fastBreakShots": 3,
                    "averageBallPossession": 53.375,
                    "totalPasses": 3885,
                    "accuratePasses": 3384,
                    "accuratePassesPercentage": 87.104247104247,
                    "totalOwnHalfPasses": 1638,
                    "accurateOwnHalfPasses": 1517,
                    "accurateOwnHalfPassesPercentage": 92.612942612943,
                    "totalOppositionHalfPasses": 2387,
                    "accurateOppositionHalfPasses": 1909,
                    "accurateOppositionHalfPassesPercentage": 79.974863845832,
                    "totalLongBalls": 154,
                    "accurateLongBalls": 82,
                    "accurateLongBallsPercentage": 53.246753246753,
                    "totalCrosses": 140,
                    "accurateCrosses": 42,
                    "accurateCrossesPercentage": 30,
                    "cleanSheets": 5,
                    "tackles": 136,
                    "interceptions": 57,
                    "saves": 17,
                    "errorsLeadingToGoal": 1,
                    "errorsLeadingToShot": 5,
                    "penaltiesCommited": 2,
                    "penaltyGoalsConceded": 1,
                    "clearances": 100,
                    "clearancesOffLine": 0,
                    "lastManTackles": 2,
                    "totalDuels": 735,
                    "duelsWon": 380,
                    "duelsWonPercentage": 51.700680272109,
                    "totalGroundDuels": 544,
                    "groundDuelsWon": 278,
                    "groundDuelsWonPercentage": 51.102941176471,
                    "totalAerialDuels": 191,
                    "aerialDuelsWon": 102,
                    "aerialDuelsWonPercentage": 53.403141361257,
                    "possessionLost": 881,
                    "offsides": 13,
                    "fouls": 88,
                    "yellowCards": 12,
                    "yellowRedCards": 0,
                    "redCards": 0,
                    "avgRating": 7.0694214876033,
                    "accurateFinalThirdPassesAgainst": 647,
                    "accurateOppositionHalfPassesAgainst": 1400,
                    "accurateOwnHalfPassesAgainst": 1608,
                    "accuratePassesAgainst": 2982,
                    "bigChancesAgainst": 5,
                    "bigChancesCreatedAgainst": 2,
                    "bigChancesMissedAgainst": 3,
                    "clearancesAgainst": 192,
                    "cornersAgainst": 27,
                    "crossesSuccessfulAgainst": 26,
                    "crossesTotalAgainst": 101,
                    "dribbleAttemptsTotalAgainst": 101,
                    "dribbleAttemptsWonAgainst": 48,
                    "errorsLeadingToGoalAgainst": 4,
                    "errorsLeadingToShotAgainst": 3,
                    "hitWoodworkAgainst": 4,
                    "interceptionsAgainst": 56,
                    "keyPassesAgainst": 58,
                    "longBallsSuccessfulAgainst": 139,
                    "longBallsTotalAgainst": 339,
                    "offsidesAgainst": 9,
                    "redCardsAgainst": 0,
                    "shotsAgainst": 72,
                    "shotsBlockedAgainst": 18,
                    "shotsFromInsideTheBoxAgainst": 37,
                    "shotsFromOutsideTheBoxAgainst": 35,
                    "shotsOffTargetAgainst": 35,
                    "shotsOnTargetAgainst": 19,
                    "blockedScoringAttemptAgainst": 18,
                    "tacklesAgainst": 140,
                    "totalFinalThirdPassesAgainst": 829,
                    "oppositionHalfPassesTotalAgainst": 1776,
                    "ownHalfPassesTotalAgainst": 1825,
                    "totalPassesAgainst": 3500,
                    "yellowCardsAgainst": 13,
                    "throwIns": 119,
                    "goalKicks": 41,
                    "ballRecovery": 339,
                    "freeKicks": 65,
                    "id": 26614,
                    "matches": 8,
                    "awardedMatches": 0
                }
            }
        """
        return await self.api._get(f"/team/{self.team_id}/unique-tournament/{league_id}/season/{season}/statistics/overall")

    async def latest_highlights(self) -> Dict:
        """
        Retrieves the latest highlights for the team.

        Returns:
            Dict: A dictionary containing the latest highlights, including titles, subtitles, URLs, and thumbnails.

        Example Response:
            .. code-block:: json
            {
                "media": [
                    {
                        "title": "Wolves 0 - 1 Arsenal",
                        "subtitle": "Full Highlights",
                        "url": "https://www.youtube.com/watch?v=HUBQ9rFeDCc",
                        "thumbnailUrl": "https://i.ytimg.com/vi/HUBQ9rFeDCc/hqdefault.jpg",
                        "mediaType": 1,
                        "doFollow": false,
                        "keyHighlight": false,
                        "id": 6193182,
                        "createdAtTimestamp": 1737844523,
                        "sourceUrl": "https://www.youtube.com/watch?v=HUBQ9rFeDCc"
                    },
                    {
                        "title": "Wolves 0 - 1 Arsenal",
                        "subtitle": "Full Highlights",
                        "url": "https://www.youtube.com/watch?v=4SxKKSNOxRI",
                        "thumbnailUrl": "https://i.ytimg.com/vi/4SxKKSNOxRI/hqdefault.jpg",
                        "mediaType": 1,
                        "forCountries": [
                            "BA",
                            "HR",
                            "ME",
                            "MK",
                            "RS",
                            "SI"
                        ],
                        "doFollow": false,
                        "keyHighlight": false,
                        "id": 6192993,
                        "createdAtTimestamp": 1737827674,
                        "sourceUrl": "https://www.youtube.com/watch?v=4SxKKSNOxRI"
                    }
                ]
            }
        """
        return await self.api._get(f"/team/{self.team_id}/media")

    async def performance_graph(self, league_id: int, season: int) -> Dict:
        """
        Retrieves the performance graph data for the team in a specific league and season.

        Args:
            league_id (int): The unique identifier for the league.
            season (int): The season year.

        Returns:
            Dict: A dictionary containing the performance graph data, including events, week, position, and timeframe.

        Example Response:
            .. code-block:: json
            {
                "graphData": [
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
                                        "userCount": 1364893,
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
                                "customId": "NsU",
                                "status": {
                                    "code": 100,
                                    "description": "Ended",
                                    "type": "finished"
                                },
                                "winnerCode": 3,
                                "homeTeam": {
                                    "name": "Chelsea",
                                    "slug": "chelsea",
                                    "shortName": "Chelsea",
                                    "gender": "M",
                                    "sport": {
                                        "name": "Football",
                                        "slug": "football",
                                        "id": 1
                                    },
                                    "userCount": 2114080,
                                    "nameCode": "CHE",
                                    "disabled": false,
                                    "national": false,
                                    "type": 0,
                                    "id": 38,
                                    "entityType": "team",
                                    "teamColors": {
                                        "primary": "#0310a7",
                                        "secondary": "#ffffff",
                                        "text": "#ffffff"
                                    },
                                    "fieldTranslations": {
                                        "nameTranslation": {
                                            "ar": "تشيلسي",
                                            "ru": "Челси",
                                            "hi": "चेल्सी",
                                            "bn": "চেলসি"
                                        },
                                        "shortNameTranslation": {
                                            "ar": "تشيلسي",
                                            "hi": "चेल्सी",
                                            "bn": "চেলসি"
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
                                    "current": 1,
                                    "display": 1,
                                    "period1": 1,
                                    "period2": 0,
                                    "normaltime": 1
                                },
                                "awayScore": {
                                    "current": 1,
                                    "display": 1,
                                    "period1": 1,
                                    "period2": 0,
                                    "normaltime": 1
                                },
                                "hasXg": true,
                                "id": 11352316,
                                "startTimestamp": 1691940600,
                                "slug": "liverpool-chelsea",
                                "finalResultOnly": false
                            }
                        ],
                        "week": 1,
                        "position": 12,
                        "timeframeStart": 1691712000,
                        "timeframeEnd": 1692316800
                    }
                ]
            }
        """
        return await self.api._get(f"/unique-tournament/{league_id}/season/{season}/team/{self.team_id}/team-performance-graph-data")