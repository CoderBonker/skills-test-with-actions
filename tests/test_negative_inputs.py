import sys
import os

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci  # noqa: E402


def test_area_of_circle_negative_radius():
    """Negative radius should raise ValueError."""
    with pytest.raises(ValueError):
        area_of_circle(-1)


def test_get_nth_fibonacci_negative():
    """Negative n should raise ValueError."""
    with pytest.raises(ValueError):
        get_nth_fibonacci(-5)
