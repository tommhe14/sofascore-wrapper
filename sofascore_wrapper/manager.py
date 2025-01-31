from .api import SofascoreAPI
from typing import Dict, Any, List

class Manager:
    def __init__(self, api: SofascoreAPI, manager_id: int):
        """
        Initializes the Manager class with the SofascoreAPI instance and manager ID.

        Args:
            api (SofascoreAPI): An instance of the SofascoreAPI class.
            manager_id (int): The unique identifier for the manager.
        """
        self.api = api
        self.manager_id = manager_id

    async def get_manager(self) -> Dict:
        """
        Retrieves detailed information about the manager.

        Returns:
            Dict: A dictionary containing manager details such as name, slug, short name, sport, teams, preferred formation, and more.

        Example Response:
            .. code-block:: json
            {
                "manager": {
                    "name": "Mikel Arteta",
                    "slug": "mikel-arteta",
                    "shortName": "M. Arteta",
                    "sport": {
                        "name": "Football",
                        "slug": "football",
                        "id": 1
                    },
                    "teams": [
                        {
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
                    ],
                    "preferredFormation": "4-3-3",
                    "deceased": false,
                    "id": 794075,
                    "country": {
                        "alpha2": "ES",
                        "name": "Spain"
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
                    "formerPlayerId": 1152,
                    "nationality": "ESP",
                    "nationalityISO2": "ES",
                    "performance": {
                        "total": 267,
                        "wins": 162,
                        "draws": 43,
                        "losses": 62,
                        "goalsScored": 526,
                        "goalsConceded": 281,
                        "totalPoints": 529
                    },
                    "dateOfBirthTimestamp": 385948800,
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
        return await self.api._get(f"/manager/{self.manager_id}")