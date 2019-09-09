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

from requests import get


class Crisp:
    def __init__(self):
        self.base_url = os.getenv("DARK_SKY_BASE_URL")
        self.token = os.getenv("DARK_SKY_API_TOKEN")
        self.vacasa_lat_long = "45.5335,-122.6501"

    def get_crisp_status(self):
        """Tells us whether it's crisp out based on the temperature and humidity

        https://api.darksky.net/forecast/[key]/[latitude],[longitude]

        Returns:

        dict status - a dict with information on whether it's crisp or not
        """

        res = get(f"{self.base_url}/forecast/{self.token}/{self.vacasa_lat_long}")

        currently = res.json()["currently"]
        humidity = currently["humidity"]
        temp = currently["apparentTemperature"]

        status = 40.0 <= temp <= 60.0 and humidity < 0.5
        return {"crisp": status, "temperature": temp, "humidity": humidity}


if __name__ == "__main__":
    crisp = Crisp()
    crisp.get_crisp_status()
