import pytest
from unittest import mock

from app import get_crisp_status


def test_get_crisp_status():
    #
    # Arrange
    #

    #
    # Act
    #
    res = get_crisp_status()

    #
    # Assert
    #
    assert res is not None
    assert "status" in res
