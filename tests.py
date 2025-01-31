import asyncio
from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.team import Team
from sofascore_wrapper.league import League
from sofascore_wrapper.manager import Manager
import json

async def main():
    api = SofascoreAPI()

    league = League(api, 17)
    league_data = await league.totw(61627, round=16987)
    print(json.dumps(league_data, indent = 4))


if __name__ == "__main__":
    asyncio.run(main())
