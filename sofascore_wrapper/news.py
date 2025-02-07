from .api import SofascoreAPI
from typing import List, Dict, Any, Literal

class News:
    def __init__(self, api: SofascoreAPI):
        """
        Initializes the News class with the sofascore API.

        Args:
            api (SofascoreAPI): An instance of the SofascoreAPI class.
        """
        self.api = api

    async def news_feed(self) -> Dict[str, Any]:
      """
      Retrieves sofascore's latest football published news articles
  
      Returns:
          Dict[str, Any]: A dict containg a list of objects.
  
      Example Response:
          {
            "newsArticles": [
                        {
                          "source": 8,
                          "description": "Arsenal remain comfortably adrift of relentless Premier League leaders Liverpool despite a 5-1 hammering of Manchester City on Sunday, but midfielder Declan Rice says there is a determination to hunt them down.",
                          "thumbnailUrl": "https://a.espncdn.com/combiner/i?img=%2Fphoto%2F2025%2F0202%2Fr1446625_1024x576_16%2D9.jpg",
                          "tags": [
                            "player",
                            "team",
                            "tournament"
                          ],
                          "header": "Rice says Arsenal ready to 'hunt down' Liverpool",
                          "externalUrl": "https://www.espn.com/soccer/story/_/id/43667029/arsenal-hunt-liverpool-title-race-rice-says",
                          "contentId": "8:US-EN-43667029",
                          "publishedAtTimestamp": 1738544104
                        },
            ]
          }
      """
      return self.api._get(f"/media/news-articles/sport/football")
