from datetime import datetime
import math
def days_before_event(hours: bool) -> int:
    time_now = datetime.now()
    NY_time = datetime(2022, 1, 1)
    rest_time = NY_time - time_now
    rest_time_days = rest_time.days
    if hours:
        rest_time_hours = math.floor(rest_time.seconds / 3600)
        print(f"{rest_time_days} days, {rest_time_hours} hour")
    else:
        print(f"{rest_time_days} days")
    return 0
days_before_event(True)