def classify_status(satellite_count: int, accuracy_m: float) -> str:
    """Classify a toy status. This is not an SIH navigation algorithm."""
    if satellite_count < 0:
        raise ValueError("satellite_count must be non-negative")
    if accuracy_m < 0:
        raise ValueError("accuracy_m must be non-negative")
    if satellite_count == 0:
        return "BLACKOUT"
    if satellite_count < 4 or accuracy_m > 25.0:
        return "DEGRADED"
    return "HEALTHY"
