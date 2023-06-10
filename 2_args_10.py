from datetime import datetime, timedelta


def calculate_previous_date(date, n):
    date_obj = datetime.strptime(date, "%y-%m-%d")
    timedelta_obj = timedelta(days=n)
    previous_date = date_obj - timedelta_obj
    previous_date_str = previous_date.strftime("%y-%m-%d")

    return previous_date_str


print(calculate_previous_date("16-12-10", 11))