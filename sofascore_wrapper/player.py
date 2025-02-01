from .api import SofascoreAPI
from typing import Dict, List, Any, Literal

class PlayerSearch:
    def __init__(self, api: SofascoreAPI, query: str):
        """
        Initialize the PlayerSearch class with the API and search query.

        Args:
            api (SofascoreAPI): An instance of the SofascoreAPI class.
            query (str): The search query string.
        """
        self.api = api
        self.query = query.lower().replace(" ", "%20")

    async def search_player(self) -> Dict[str, Any]:
        """
        Perform a dedicated player search. This endpoint is more specific than the general search.

        Returns:
            Dict[str, Any]: A dictionary containing player search results.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "players": [
                    {
                        "name": "Cole Palmer",
                        "slug": "cole-palmer",
                        "shortName": "C. Palmer",
                        "team": {
                            "name": "Chelsea",
                            "slug": "chelsea",
                            "shortName": "Chelsea",
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
                                    "flag": "england",
                                    "alpha2": "EN"
                                },
                                "userCount": 1361165,
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
                            "userCount": 2130321,
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
                        "position": "M",
                        "jerseyNumber": "20",
                        "userCount": 234297,
                        "id": 982780,
                        "dateOfBirthTimestamp": 1020643200,
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "كول بالمر",
                                "hi": "कोल पाल्मर",
                                "bn": "কোল পামার"
                            },
                            "shortNameTranslation": {
                                "ar": "ك. بالمر",
                                "hi": "सी. पाल्मर",
                                "bn": "সি. পামার"
                            }
                        }
                    }
                ]
            }
        """
        return await self.api._get(f"/search/players/{self.query}")


class Player:
    def __init__(self, api: SofascoreAPI, player_id: int):
        """
        Initialize the Player class with the API and player ID.

        Args:
            api (SofascoreAPI): An instance of the SofascoreAPI class.
            player_id (int): The unique ID of the player.
        """
        self.api = api
        self.player_id = player_id

    async def get_player(self) -> Dict[str, Any]:
        """
        Fetch detailed information about the player.

        Returns:
            Dict[str, Any]: A dictionary containing player details.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
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
        """
        return await self.api._get(f"/player/{self.player_id}")

    async def transfer_history(self) -> Dict[str, Any]:
        """
        Fetch the transfer history of the player.

        Returns:
            Dict[str, Any]: A dictionary containing the player's transfer history.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "transferHistory": [
                    {
                        "player": {
                            "name": "Cristiano Ronaldo",
                            "slug": "cristiano-ronaldo",
                            "shortName": "C. Ronaldo",
                            "position": "F",
                            "jerseyNumber": "7",
                            "userCount": 1067318,
                            "id": 750,
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "كريستيانو رونالدو",
                                    "hi": "क्रिस्टियानो रोनाल्डो",
                                    "bn": "ক্রিশ্চিয়ানো রোনালদো"
                                },
                                "shortNameTranslation": {
                                    "ar": "ك. رونالدو",
                                    "hi": "सी. रोनाल्डो",
                                    "bn": "সি. রোনালদো"
                                }
                            }
                        },
                        "transferFrom": {
                            "name": "No team",
                            "slug": "no-team",
                            "shortName": "No team",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 10,
                            "nameCode": "NTE",
                            "disabled": true,
                            "national": false,
                            "type": 0,
                            "id": 241802,
                            "entityType": "team",
                            "teamColors": {
                                "primary": "#d0d0d0",
                                "secondary": "#000000",
                                "text": "#000000"
                            }
                        },
                        "transferTo": {
                            "name": "Al-Nassr",
                            "slug": "al-nassr",
                            "shortName": "Al-Nassr",
                            "gender": "M",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 1481629,
                            "nameCode": "ALN",
                            "disabled": false,
                            "national": false,
                            "type": 0,
                            "id": 23400,
                            "entityType": "team",
                            "teamColors": {
                                "primary": "#ffff00",
                                "secondary": "#ffff00",
                                "text": "#ffff00"
                            },
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "النصر",
                                    "ru": "Аль-Наср",
                                    "hi": "अल-नासर",
                                    "bn": "আল-নাসর"
                                },
                                "shortNameTranslation": {
                                    "ar": "النصر",
                                    "hi": "अल-नासर",
                                    "bn": "আল-নাসর"
                                }
                            }
                        },
                        "fromTeamName": "No team",
                        "toTeamName": "Al-Nassr",
                        "type": 3,
                        "transferFee": 0,
                        "transferFeeDescription": "Free",
                        "id": 1529662,
                        "transferDateTimestamp": 1672531200
                    }
                ]
            }
        """
        return await self.api._get(f"/player/{self.player_id}/transfer-history")

    async def last_fixtures(self) -> List[Dict[str, Any]]:
        """
        Fetch the last matches the player participated in.

        The matches are returned in reverse chronological order, meaning the most recent match
        is the first item in the list.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing match details, with the most recent match first.
                                Each dictionary includes information about the tournament, teams, scores, and timestamps.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            [
                {
                    "tournament": {
                        "name": "Euro, Knockout stage",
                        "slug": "uefa-euro-knockout-stage",
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
                        "uniqueTournament": {
                            "name": "EURO",
                            "slug": "european-championship",
                            "primaryColorHex": "#293cdb",
                            "secondaryColorHex": "#00ba5d",
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
                            "userCount": 1011793,
                            "id": 1,
                            "hasPerformanceGraphFeature": false,
                            "hasEventPlayerStatistics": true,
                            "displayInverseHomeAwayTeams": false
                        },
                        "priority": 683,
                        "isGroup": false,
                        "isLive": false,
                        "id": 2137
                    },
                    "season": {
                        "name": "EURO 2024",
                        "year": "2024",
                        "editor": false,
                        "id": 56953
                    },
                    "roundInfo": {
                        "round": 27,
                        "name": "Quarterfinals",
                        "slug": "quarterfinals",
                        "cupRoundType": 4
                    },
                    "customId": "GObseUb",
                    "status": {
                        "code": 120,
                        "description": "AP",
                        "type": "finished"
                    },
                    "winnerCode": 2,
                    "homeTeam": {
                        "name": "Portugal",
                        "slug": "portugal",
                        "shortName": "Portugal",
                        "gender": "M",
                        "sport": {
                            "name": "Football",
                            "slug": "football",
                            "id": 1
                        },
                        "userCount": 1382625,
                        "nameCode": "POR",
                        "ranking": 6,
                        "national": true,
                        "type": 0,
                        "id": 4704,
                        "country": {
                            "alpha2": "PT",
                            "alpha3": "PRT",
                            "name": "Portugal",
                            "slug": "portugal"
                        },
                        "entityType": "team",
                        "subTeams": [],
                        "teamColors": {
                            "primary": "#cc0000",
                            "secondary": "#66cc66",
                            "text": "#66cc66"
                        },
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "البرتغال",
                                "ru": "Португалия",
                                "hi": "पुर्तगाल",
                                "bn": "পর্তুগাল"
                            }
                        }
                    },
                    "awayTeam": {
                        "name": "France",
                        "slug": "france",
                        "shortName": "France",
                        "gender": "M",
                        "sport": {
                            "name": "Football",
                            "slug": "football",
                            "id": 1
                        },
                        "userCount": 1155922,
                        "nameCode": "FRA",
                        "ranking": 2,
                        "disabled": false,
                        "national": true,
                        "type": 0,
                        "id": 4481,
                        "country": {
                            "alpha2": "FR",
                            "alpha3": "FRA",
                            "name": "France",
                            "slug": "france"
                        },
                        "entityType": "team",
                        "subTeams": [],
                        "teamColors": {
                            "primary": "#01509e",
                            "secondary": "#e30613",
                            "text": "#e30613"
                        },
                        "fieldTranslations": {
                            "nameTranslation": {
                                "ar": "فرنسا",
                                "ru": "Франция",
                                "hi": "फ्रांस",
                                "bn": "ফ্রান্স"
                            }
                        }
                    },
                    "homeScore": {
                        "current": 3,
                        "display": 0,
                        "period1": 0,
                        "period2": 0,
                        "normaltime": 0,
                        "extra1": 0,
                        "extra2": 0,
                        "overtime": 0,
                        "penalties": 3
                    },
                    "awayScore": {
                        "current": 5,
                        "display": 0,
                        "period1": 0,
                        "period2": 0,
                        "normaltime": 0,
                        "extra1": 0,
                        "extra2": 0,
                        "overtime": 0,
                        "penalties": 5
                    },
                    "time": {
                        "injuryTime1": 0,
                        "injuryTime2": 3,
                        "injuryTime3": 0,
                        "injuryTime4": 0,
                        "currentPeriodStartTimestamp": 1720214035
                    },
                    "changes": {
                        "changes": [
                            "status.code",
                            "status.description",
                            "status.type",
                            "homeScore.display",
                            "homeScore.penalties",
                            "awayScore.display",
                            "awayScore.penalties"
                        ],
                        "changeTimestamp": 1720215795
                    },
                    "hasGlobalHighlights": false,
                    "hasXg": true,
                    "hasEventPlayerStatistics": true,
                    "hasEventPlayerHeatMap": true,
                    "detailId": 1,
                    "crowdsourcingDataDisplayEnabled": false,
                    "id": 11874026,
                    "startTimestamp": 1720206000,
                    "slug": "portugal-france",
                    "finalResultOnly": false,
                    "feedLocked": true,
                    "isEditor": false
                },
                ...
            ]
        """
        data = await self.api._get(f"/player/{self.player_id}/events/last/0")
        data["events"].reverse()  # Reverse the list to ensure the most recent match is first
        return data["events"]

    async def attributes(self) -> Dict[str, Any]:
        """
        Fetch the player's attributes and performance overview.

        Returns:
            Dict[str, Any]: A dictionary containing the player's attributes and performance statistics.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "averageAttributeOverviews": [
                    {
                        "attacking": 62,
                        "technical": 54,
                        "tactical": 44,
                        "defending": 32,
                        "creativity": 47,
                        "position": "F",
                        "yearShift": 0,
                        "id": 19812
                    }
                ],
                "playerAttributeOverviews": [
                    {
                        "attacking": 85,
                        "technical": 77,
                        "tactical": 58,
                        "defending": 35,
                        "creativity": 80,
                        "position": "D",
                        "yearShift": 0,
                        "id": 50004
                    }
                ]
            }
        """
        return await self.api._get(f"/player/{self.player_id}/attribute-overviews")

    async def league_stats(self, league_id: int, season: int) -> Dict[str, Any]:
        """
        Fetch the player's statistics for a specific league and season.

        Args:
            league_id (int): The unique ID of the league.
            season (int): The season ID.

        Returns:
            Dict[str, Any]: A dictionary containing the player's statistics for the specified league and season.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "statistics": {
                    "rating": 6.9,
                    "totalRating": 34.5,
                    "countRating": 5,
                    "goals": 0,
                    "bigChancesCreated": 0,
                    "bigChancesMissed": 0,
                    "assists": 0,
                    "expectedAssists": 0.14556703,
                    "goalsAssistsSum": 0,
                    "accuratePasses": 127,
                    "inaccuratePasses": 16,
                    "totalPasses": 143,
                    "accuratePassesPercentage": 88.811188811189,
                    "accurateOwnHalfPasses": 64,
                    "accurateOppositionHalfPasses": 64,
                    "accurateFinalThirdPasses": 31,
                    "keyPasses": 2,
                    "successfulDribbles": 2,
                    "successfulDribblesPercentage": 50,
                    "tackles": 10,
                    "interceptions": 3,
                    "yellowCards": 1,
                    "directRedCards": 0,
                    "redCards": 0,
                    "accurateCrosses": 1,
                    "accurateCrossesPercentage": 100,
                    "totalShots": 4,
                    "shotsOnTarget": 1,
                    "shotsOffTarget": 3,
                    "groundDuelsWon": 15,
                    "groundDuelsWonPercentage": 46.875,
                    "aerialDuelsWon": 3,
                    "aerialDuelsWonPercentage": 50,
                    "totalDuelsWon": 18,
                    "totalDuelsWonPercentage": 47.368421052632,
                    "minutesPlayed": 327,
                    "goalConversionPercentage": 0,
                    "penaltiesTaken": 0,
                    "penaltyGoals": 0,
                    "penaltyWon": 0,
                    "penaltyConceded": 0,
                    "shotFromSetPiece": 0,
                    "freeKickGoal": 0,
                    "goalsFromInsideTheBox": 0,
                    "goalsFromOutsideTheBox": 0,
                    "shotsFromInsideTheBox": 1,
                    "shotsFromOutsideTheBox": 3,
                    "headedGoals": 0,
                    "leftFootGoals": 0,
                    "rightFootGoals": 0,
                    "accurateLongBalls": 1,
                    "accurateLongBallsPercentage": 25,
                    "clearances": 7,
                    "errorLeadToGoal": 0,
                    "errorLeadToShot": 0,
                    "dispossessed": 4,
                    "possessionLost": 30,
                    "possessionWonAttThird": 1,
                    "totalChippedPasses": 3,
                    "accurateChippedPasses": 1,
                    "touches": 211,
                    "wasFouled": 3,
                    "fouls": 5,
                    "hitWoodwork": 0,
                    "ownGoals": 0,
                    "dribbledPast": 6,
                    "offsides": 1,
                    "blockedShots": 0,
                    "passToAssist": 0,
                    "saves": 0,
                    "cleanSheet": 1,
                    "penaltyFaced": 0,
                    "penaltySave": 0,
                    "savedShotsFromInsideTheBox": 0,
                    "savedShotsFromOutsideTheBox": 0,
                    "goalsConcededInsideTheBox": 1,
                    "goalsConcededOutsideTheBox": 1,
                    "punches": 0,
                    "runsOut": 0,
                    "successfulRunsOut": 0,
                    "highClaims": 0,
                    "crossesNotClaimed": 0,
                    "matchesStarted": 4,
                    "penaltyConversion": 0,
                    "setPieceConversion": 0,
                    "totalAttemptAssist": 2,
                    "totalContest": 4,
                    "totalCross": 1,
                    "duelLost": 20,
                    "aerialLost": 3,
                    "attemptPenaltyMiss": 0,
                    "attemptPenaltyPost": 0,
                    "attemptPenaltyTarget": 0,
                    "totalLongBalls": 4,
                    "goalsConceded": 2,
                    "tacklesWon": 9,
                    "tacklesWonPercentage": 90,
                    "scoringFrequency": 0,
                    "yellowRedCards": 0,
                    "savesCaught": 0,
                    "savesParried": 0,
                    "totalOwnHalfPasses": 66,
                    "totalOppositionHalfPasses": 78,
                    "totwAppearances": 0,
                    "expectedGoals": 0.1684,
                    "goalKicks": 0,
                    "ballRecovery": 11,
                    "id": 1595217,
                    "type": "overall",
                    "appearances": 5
                },
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
                }
            }
        """
        return await self.api._get(f"/player/{self.player_id}/unique-tournament/{league_id}/season/{season}/statistics/overall")

    async def image(self) -> str:
        """
        Example Response:
            .. code-block:: json

        https://img.sofascore.com/api/v1/player/934235/image
        """
        return f"https://img.sofascore.com/api/v1/player/{self.player_id}/image"
    
    async def national_stats(self) -> Dict[str, Any]:
        """
        Fetch the player's statistics for their national team.

        Returns:
            Dict[str, Any]: A dictionary containing the player's national team statistics, including appearances, goals, and debut information.

        Raises:
            Exception: If the API request fails.

        Example Response:
            .. code-block:: json
            {
                "statistics": [
                    {
                        "team": {
                            "name": "Italy",
                            "slug": "italy",
                            "shortName": "Italy",
                            "gender": "M",
                            "sport": {
                                "name": "Football",
                                "slug": "football",
                                "id": 1
                            },
                            "userCount": 905551,
                            "nameCode": "ITA",
                            "ranking": 9,
                            "disabled": false,
                            "national": true,
                            "type": 0,
                            "id": 4707,
                            "entityType": "team",
                            "teamColors": {
                                "primary": "#0066ff",
                                "secondary": "#ffffff",
                                "text": "#ffffff"
                            },
                            "fieldTranslations": {
                                "nameTranslation": {
                                    "ar": "إيطاليا",
                                    "ru": "Италия",
                                    "hi": "इटली",
                                    "bn": "ইতালি"
                                },
                                "shortNameTranslation": {
                                    "ar": "إيطاليا",
                                    "hi": "इटली",
                                    "bn": "ইতালি"
                                }
                            }
                        },
                        "appearances": 8,
                        "goals": 0,
                        "debutTimestamp": 1717459200
                    }
                ]
            }
        """
        return await self.api._get(f"/player/{self.player_id}/national-team-statistics")
