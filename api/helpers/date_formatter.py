from datetime import datetime


# convert date string to datetime object
def date_formatter(date_string):
    date_object = datetime.strptime(date_string, '%m/%d/%Y')
    return date_object