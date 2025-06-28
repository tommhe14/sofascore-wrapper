# Sofascore Wrapper

A Python API wrapper for the Sofascore undocumented API. This library allows you to fetch and interact with Sofascore data, including information about matches, players, teams, and more.

[![PyPI Downloads](https://static.pepy.tech/badge/sofascore-wrapper)](https://pepy.tech/projects/sofascore-wrapper)

## 📖 Documentation
For detailed usage and API reference, visit the official documentation:
👉 [Sofascore Wrapper Docs](https://tommhe14.github.io/sofascore-wrapper)

## 📥 Installation

### 1. Install the Package and Playwright
```bash
pip install sofascore-wrapper
# REQUIRED FOR USE
python -m playwright install chromium
```

## 🚀 Usage Example
Here's a quick example to get you started:
```python
import asyncio
import json
from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.search import Search

async def main():
    api = SofascoreAPI()  # Initialize the API client
    search = Search(api, search_string="saka")
    player = await search.search_all()
    print(json.dumps(player, indent = 4))
    await api.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## Example Response!
```json
{
    "results": [
        {
            "entity": {
                "id": 934235,
                "name": "Bukayo Saka",
                "slug": "bukayo-saka",
                "retired": false,
                "userCount": 205496,
                "team": {
                    "id": 42,
                    "name": "Arsenal",
                    "nameCode": "ARS",
                    "slug": "arsenal",
                    "national": false,
                    "sport": {
                        "id": 1,
                        "slug": "football",
                        "name": "Football"
                    },
                    "userCount": 2540585,
                    "teamColors": {
                        "primary": "#cc0000",
                        "secondary": "#ffffff",
                        "text": "#ffffff"
                    },
                    "gender": "M",
                    "fieldTranslations": {
                        "nameTranslation": {
                            "ar": "\u0627\u0631\u0633\u0646\u0627\u0644",
                            "ru": "\u0410\u0440\u0441\u0435\u043d\u0430\u043b",
                            "hi": "\u0906\u0930\u094d\u0938\u0947\u0928\u0932",
                            "bn": "\u0986\u09b0\u09cd\u09b8\u09c7\u09a8\u09be\u09b2"
                        },
                        "shortNameTranslation": {}
                    }
                },
                "deceased": false,
                "country": {
                    "alpha2": "EN",
                    "name": "England",
                    "slug": "england"
                },
                "shortName": "B. Saka",
                "position": "F",
                "jerseyNumber": "7",
                "fieldTranslations": {
                    "nameTranslation": {
                        "ar": "\u0628. \u0633\u0627\u0643\u0627",
                        "hi": "\u092c\u0940. \u0938\u093e\u0915\u093e",
                        "bn": "\u09ac\u09bf. \u09b8\u09be\u0995\u09be"
                    },
                    "shortNameTranslation": {}
                }
            },
            "score": 651868.6,
            "type": "player"
        },
        ...
```

## 💬 Need Help?
Join our Discord community for support and discussions:
👉 [Discord Support Server](https://discord.gg/pGYmZxUKB7)

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## From Me!
Will slowly be adding more sports along our journey! SofaScore API is written to re-use requests for multiple sports, So in theory making requests for a sport other than football (soccer) will allow you to make requests with any class (match, player, etc). Any requests for the dedicated sport that you cannot, they will be under the dedicated sport i.e Basketball.player_stats() rather than Player.stats()

- If you encounter any issues feel free to open an issue.
- If you have any enhancement requests, feel free to open an issue with the front end proof of what you're looking to get.
- Always open to pull requests!

*This is an unofficial API wrapper and not affiliated with Sofascore. You may be at risk via Sofascore's TOS.*

**RECENTLY CHANGED TO CHROMIUM BASED REQUESTS TO ADVERT 403 ON ALL REST REQUESTS**

## Examples
Check out some more use cases from the examples folder!

---
Enjoy using **Sofascore Wrapper**! 🎉

