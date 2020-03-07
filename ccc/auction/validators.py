import datetime

def validate_Auction(data):
    
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
        datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
        return True
    except expression as identifier:
        return False