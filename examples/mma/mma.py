from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.mma import MMA
from sofascore_wrapper.match import Match
from sofascore_wrapper.search import Search
import asyncio
import json

async def fighter_and_fights():
    api = SofascoreAPI()

    # Search for the league
    search_init = Search(api, "UFC")
    league_search = await search_init.search_leagues(sport="mma")
    
    # player search
    search_fighter_init = Search(api, "plessis")
    fighter_search = await search_fighter_init.search_players(sport="mma")

    fighter_id = fighter_search["results"][0]["entity"]["id"]
    tournament_id = league_search["results"][0]["entity"]["id"]
    
    mma_init = MMA(api)
    ufc = await mma_init.tournament_info(tournament_id)
    print(json.dumps(ufc, indent = 4))
    
    last_fights = await mma_init.fighter_last_fights(fighter_id)
    print(json.dumps(last_fights, indent = 4))

    stats = await mma_init.fighter_career_stats(fighter_id)
    print(json.dumps(stats, indent = 4))

    fights_this_month = await mma_init.main_events_month(tournament_id)
    print(json.dumps(fights_this_month, indent = 4))

    live_fights = await mma_init.live_fights()
    print(json.dumps(live_fights, indent = 4))

    await api.close()

asyncio.run(fighter_and_fights())