import datetime

def validate_auction(data):
    
    if (valid_description(data["description"]) and 
        valid_date(data["end_time"])):
            return True
    return False


def valid_description(description):
    if len(description) > 255:
        return False
    return True

def valid_date(date):
    try:
        datetime.datetime.strptime(date)
        return True
    except Exception:
        return False