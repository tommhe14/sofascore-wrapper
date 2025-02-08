.. sofascore-wrapper documentation master file, created by
   sphinx-quickstart on Tue Jan 30 2025.

Welcome to sofascore-wrapper's documentation!
============================================

This is the Python API wrapper for the Sofascore undocumented API.
It allows you to fetch and interact with data from Sofascore, including information about matches, players, teams, and more.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api_reference

   modules

Installation
============
To install the package, use pip:

.. code-block:: bash

   pip install sofascore-wrapper

Usage
=====
Here's a simple example of how to use the wrapper to search for a player:

.. code-block:: python

   import asyncio
   from sofascore_wrapper.api import SofascoreAPI
   from sofascore_wrapper.search import Search

   async def main():
      api = SofascoreAPI()  # Initialize the API client

      # Create an instance of the Search class
      search = Search(api, search_string="saka")

      # Perform the search and print the result
      player = await search.search_all()
      print(player)

      # Close the API client
      await api.close()

   if __name__ == "__main__":
      asyncio.run(main())

In this example, we initialize the `SofascoreAPI`, create a `Search` instance with the search string `"saka"`, and call `search_all()` to fetch the player data. The result is printed to the console.

From Me!
========
Will slowly be adding more sports along our journey! SofaScore API is written to re-use requests for multiple sports, So in theory making requests for a sport other than football (soccer) will allow you to make requests with any class (match, player, etc). Any requests for the dedicated sport that you cannot, they will be under the dedicated sport i.e Basketball.player_stats() rather than Player.stats()

API Reference
=============
The following sections provide detailed information on the available methods and classes in the `sofascore-wrapper` API.