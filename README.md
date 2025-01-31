# Sofascore Wrapper

A Python API wrapper for the Sofascore undocumented API. This library allows you to fetch and interact with Sofascore data, including information about matches, players, teams, and more.

## 📖 Documentation
For detailed usage and API reference, visit the official documentation:
👉 [Sofascore Wrapper Docs](https://tommhe14.github.io/sofascore-wrapper)

## 📥 Installation
You can install the package using pip:
```bash
pip install sofascore-wrapper
```

## 🚀 Usage Example
Here's a quick example to get you started:
```python
import asyncio
from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.search import Search

async def main():
    api = SofascoreAPI()  # Initialize the API client
    search = Search(api, search_string="saka")
    player = await search.search_all()
    print(player)
    await api.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## 💬 Need Help?
Join our Discord community for support and discussions:
👉 [Discord Support Server](https://discord.gg/pGYmZxUKB7)

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## From Me!

- If you encounter any issues feel free to open an issue.
- If you have any enhancement requests, feel free to open an issue with the front end proof of what you're looking to get.
- Always open to pull requests!

## Examples
Check out some more use cases from the examples folder!

---
Enjoy using **Sofascore Wrapper**! 🎉

