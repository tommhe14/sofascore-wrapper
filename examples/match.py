from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.search import Search
from sofascore_wrapper.match import Match
import asyncio
import json


async def match():
    api = SofascoreAPI()

    # Search for a match
    init_search = Search(api, search_string = "girona v arsenal")
    search_match = await init_search.search_match()
    #print(json.dumps(search_match, indent = 4))

    # Pick match from entries
    selected_match = search_match["results"][0]
    match_id = selected_match["entity"]["id"]

    # Init the match class for a single match
    match_init = Match(api, match_id = match_id)

    # match stats
    match_stats = await match_init.stats()
    #print(json.dumps(match_stats, indent = 4))

    # Live updated match commentary
    match_commentary = await match_init.commentary()
    #print(json.dumps(match_commentary, indent = 4))

    # List all match channels for each country
    channels = await match_init.match_channels()
    #print(json.dumps(channels, indent = 4))

    # Select country and filter through the list of channels and grab the channel name
    gb_channel = channels["countryChannels"]["GB"]
    channels = []
    for channel in gb_channel:
        channel_name = await match_init.get_channel(channel)
        channels.append(channel_name)

    #print("GB Channels:\n" + "\n".join(channels))

    match_lineups = await match_init.lineups_away()
    print(json.dumps(match_lineups.keys(), indent = 4))
    await api.close()

async def global_matches():
    api = SofascoreAPI()

    # init match class
    match_init = Match()

    # Get all current live games
    live_matches = await match_init.live_games()
    print(json.dumps(live_matches, indent = 4))

    # Get games from today or provide a date for a specific day
    todays_games = await match_init.games_by_date()
    print(json.dumps(todays_games, indent = 4))

    await api.close()

asyncio.run(match())
#asyncio.run(global_matches())