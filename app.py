"""Is it crisp?

Simple service to decide if it's currently crisp out in Portland

Authors:
Scott Ogle
Brian Borealis
Michele Greenwood
Steven Weeks
Robert Calon
"""

import os

import requests


def get_crisp_status():
    """Tells us whether it's crisp out based on the temperature and humidity

    https://api.darksky.net/forecast/[key]/[latitude],[longitude]

    Returns:

    dict status - a dict with information on whether it's crisp or not
    """
    base_url = os.getenv("DARK_SKY_BASE_URL")
    token = os.getenv("DARK_SKY_API_TOKEN")
    vacasa_lat_long = "45.5335,-122.6501"

    res = requests.get(f"{base_url}/forecast/{token}/{vacasa_lat_long}")
    import pdb

    pdb.set_trace()


if __name__ == "__main__":
    get_crisp_status()
