from .api import SofascoreAPI
import datetime
from typing import Optional, Dict, Any
from pathlib import Path
import json

class UserData:
    ENUMS_PATH = Path(__file__).parent / "tools" / "enums.json"

    with open(ENUMS_PATH, "r", encoding="utf-8") as file:
        ENUMS = json.load(file)

    def __init__(self, api: SofascoreAPI):
        self.api = api
        self.enums = self.ENUMS

    async def sofascore_news_rss_feed(self) -> str:
        """
        Retrieves the current sofascore news RSS feed.

        """
        return await self.api._raw_get("https://www.sofascore.com/news/category/app/iphone/feed/")
    
    async def user_account(self, user_id: str) -> Dict:
        """
        Retrieves the given user data.

        To get your User ID, go to profile -> share account which will provide a link such as https://www.sofascore.com/user/profile/[userid]

        """
        return await self.api._get(f"/user-account/{user_id}")
    
    async def user_flares(self, user_id: str) -> Dict:
        """
        Retrieves the given user flares data.

        To get your User ID, go to profile -> share account which will provide a link such as https://www.sofascore.com/user/profile/[userid]

        """
        return await self.api._get(f"/flare/user/{user_id}")
    
    async def last_user_predictions(self, user_id: str) -> Dict:
        """
        Retrieves the given user last predictions

        To get your User ID, go to profile -> share account which will provide a link such as https://www.sofascore.com/user/profile/[userid]

        """
        return await self.api._get(f"/user-account/{user_id}/predictions/last/0")
    
    async def next_user_predictions(self, user_id: str) -> Dict:
        """
        Retrieves the given user last predictions

        To get your User ID, go to profile -> share account which will provide a link such as https://www.sofascore.com/user/profile/[userid]

        """
        return await self.api._get(f"/user-account/{user_id}/predictions/next/0")
    
    async def contribution_leaderboard(self) -> Dict:
        """
        Retrieves the top 100 contribution leaderboard.

        """
        return await self.api._get("/user-account/contribution-ranking-score")
    
    async def predictions_leaderboard(self) -> Dict:
        """
        Retrieves the top 100 predictions leaderboard.

        """
        return await self.api._get("/user-account/vote-ranking")
    
    async def editor_leaderboard(self) -> Dict:
        """
        Retrieves the top 100 editors leaderboard.

        """
        return await self.api._get("/user-account/editor-ranking")
    
    
