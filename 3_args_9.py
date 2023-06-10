from datetime import datetime, timedelta

def compare_dates(from_date, to_date, difference):
    
    from_date = datetime.strptime(from_date, "%y-%m-%d")
    to_date = datetime.strptime(to_date, "%y-%m-%d")
    
    
    date_difference = abs(from_date - to_date).days
    
    
    if date_difference < difference:
        return True
    else:
        return False
print(compare_dates("23-06-10", "23-06-07", 7))
print(compare_dates("23-06-01", "23-06-15", 7))
