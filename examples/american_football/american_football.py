from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.american_football import AmericanFootball
from sofascore_wrapper.league import League
from sofascore_wrapper.search import Search
from sofascore_wrapper.player import Player
import asyncio
import json

async def tourn_and_games():
    api = SofascoreAPI()

    # Search for the league
    search_init = Search(api, "NFL")
    league_search = await search_init.search_leagues(sport="american-football")

    league_id = league_search["results"][0]["entity"]["id"]

    league = League(api, league_id)
    league_season = await league.current_season()
    
    season = league_season["id"]

    football = AmericanFootball(api)
    games = await football.season_games(league_id, season)
    print(json.dumps(games, indent = 4))

    player_search = Search(api, "mahomes")
    player = await player_search.search_players(sport="american-football")

    player_id = player["results"][0]["entity"]["id"]

    player_init = Player(api, player_id)
    info = await player_init.get_player()
    print(json.dumps(info, indent = 4))

    last_games = await player_init.last_fixtures()
    print(json.dumps(last_games, indent = 4))

    await api.close()

asyncio.run(tourn_and_games()) 