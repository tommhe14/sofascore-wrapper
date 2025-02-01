import asyncio
from sofascore_wrapper.api import SofascoreAPI  # Import your actual API class
from sofascore_wrapper.league import League  # Import your League class
import json

async def test():
    api = SofascoreAPI()  
    league_id = 17  

    league = League(api, league_id)  
    fixtures = await league.next_fixtures()  

    print(json.dumps(fixtures, indent = 4))  

    await api.close()

if __name__ == "__main__":
    asyncio.run(test())
