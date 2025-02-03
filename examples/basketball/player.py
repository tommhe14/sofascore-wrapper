from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.basketball import Basketball
from sofascore_wrapper.league import League
from sofascore_wrapper.search import Search
import asyncio
import json

async def player_and_games():
    api = SofascoreAPI()

    # Search for the league
    search_init = Search(api, "NBA")
    league_search = await search_init.search_leagues(sport="basketball")
    # player search
    search_player_init = Search(api, "giannis")
    player_search = await search_player_init.search_players(sport="basketball")

    player_id = player_search["results"][0]["entity"]["id"]
    league_id = league_search["results"][0]["entity"]["id"]
    
    # get stats for Giannis 
    banggg = Basketball(api)
    player = await banggg.player_stats(player_id = player_id, league_id = league_id)
    print(json.dumps(player, indent = 4))

    # get all current live basketball games
    live_basketball_games = await banggg.live_games()
    print(json.dumps(live_basketball_games, indent = 4))

    await api.close()

asyncio.run(player_and_games())