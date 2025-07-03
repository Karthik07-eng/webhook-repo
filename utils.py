from datetime import datetime, timedelta

def is_fresh_data(timestamp: datetime, window_minutes: int) -> bool:
    """
    Check if a timestamp is within the freshness window.
    """
    now = datetime.utcnow()
    return now - timestamp <= timedelta(minutes=window_minutes)
