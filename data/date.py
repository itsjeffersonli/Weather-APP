from datetime import datetime
from pytz import timezone


def date_converter(_timezone):
    _timezone = str(_timezone)
    format = "%H:%M - %m/%d/%Y"
    now = datetime.now(timezone('UTC'))
    _get_utc_time = now.strftime(format)

    now_timezone = now.astimezone(timezone(_timezone))
    final_date = now_timezone.strftime(format)

    return final_date

