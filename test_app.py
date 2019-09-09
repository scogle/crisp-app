import pytest
from unittest import mock

from app import get_crisp_status


@mock.patch("app.get")
@pytest.mark.parametrize(
    "mock_response,expected",
    [
        (
            {
                "currently": {
                    "apparentTemperature": 65.02,
                    "cloudCover": 1,
                    "dewPoint": 57.26,
                    "humidity": 0.76,
                    "icon": "cloudy",
                    "nearestStormBearing": 307,
                    "nearestStormDistance": 2,
                    "ozone": 312.9,
                    "precipIntensity": 0,
                    "precipProbability": 0,
                    "pressure": 1012.43,
                    "summary": "Overcast",
                    "temperature": 65.02,
                    "time": 1568055083,
                    "uvIndex": 3,
                    "visibility": 7.7,
                    "windBearing": 191,
                    "windGust": 7.89,
                    "windSpeed": 7.89,
                }
            },
            False,
        ),
        (
            {
                "currently": {
                    "apparentTemperature": 55.02,
                    "cloudCover": 1,
                    "dewPoint": 57.26,
                    "humidity": 0.42,
                    "icon": "cloudy",
                    "nearestStormBearing": 307,
                    "nearestStormDistance": 2,
                    "ozone": 312.9,
                    "precipIntensity": 0,
                    "precipProbability": 0,
                    "pressure": 1012.43,
                    "summary": "Overcast",
                    "temperature": 65.02,
                    "time": 1568055083,
                    "uvIndex": 3,
                    "visibility": 7.7,
                    "windBearing": 191,
                    "windGust": 7.89,
                    "windSpeed": 7.89,
                }
            },
            True,
        ),
    ],
)
def test_get_crisp_status(mock_get, mock_response, expected):
    #
    # Arrange
    #

    # get().json() => value
    mock_get.return_value.json.return_value = mock_response

    #
    # Act
    #
    res = get_crisp_status()

    #
    # Assert
    #
    assert res is not None
    assert "crisp" in res
    assert res["crisp"] == expected
