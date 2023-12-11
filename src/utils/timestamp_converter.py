from datetime import datetime


def convert_datetime_to_str(datetime: datetime) -> str:
    datetime_formatted = datetime.strftime("%Y-%m-%dT%H:%M:%S")
    return datetime_formatted
