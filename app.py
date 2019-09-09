"""Is it crisp?

Simple service to decide if it's currently crisp out in Portland

Authors:
Scott Ogle
Brian Borealis
Michele Greenwood
Steven Weeks
"""

import os

import requests


def get_crisp_status():
    """Tells us whether it's crisp out based on the temperature and humidity

    Returns:

    dict status - a dict with information on whether it's crisp or not
    """

    return {"status": "maybe"}
