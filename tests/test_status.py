import pytest

from sandbox_nav.status import classify_status


def test_healthy_status() -> None:
    assert classify_status(8, 4.5) == "HEALTHY"


def test_blackout_status() -> None:
    assert classify_status(0, 99.0) == "BLACKOUT"


def test_negative_satellite_count_is_rejected() -> None:
    with pytest.raises(ValueError, match="satellite_count"):
        classify_status(-1, 5.0)
