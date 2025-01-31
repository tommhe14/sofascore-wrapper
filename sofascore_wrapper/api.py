import asyncio
from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.team import Team
from sofascore_wrapper.league import League
from sofascore_wrapper.manager import Manager

async def main():
    api = SofascoreAPI()

    # Fetch team data
    team = Team(api, 42)
    team_data = await team.fetch()
    print("Team Data:", team_data)

    # Fetch league data
    league = League(api, 17)
    league_data = await league.fetch()
    print("League Data:", league_data)

    # Fetch manager data
    manager = Manager(api, 1234)
    manager_data = await manager.fetch()
    print("Manager Data:", manager_data)

    await api.close()

if __name__ == "__main__":
    asyncio.run(main())
