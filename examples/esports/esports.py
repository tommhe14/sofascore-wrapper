from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.esports import Esports
from sofascore_wrapper.league import League
from sofascore_wrapper.search import Search
import asyncio
import json

async def tourn_and_games():
    api = SofascoreAPI()

    # Search for the league
    search_init = Search(api, "IEM")
    league_search = await search_init.search_all(sport="esports")

    league_id = league_search["results"][0]["entity"]["id"]

    esports = Esports(api)
    season_check = await esports.tournament_seasons(league_id)
    print(json.dumps(season_check, indent = 4))

    # IEM Katowice 2025: 71011
    next_matches = await esports.next_tournament_matches(league_id,71011)
    print(json.dumps(next_matches, indent = 4))

    await api.close()

asyncio.run(tourn_and_games())