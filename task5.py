import datetime


def date_in_future(n = None):
    if not n or type(n) != int:
        return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return (datetime.datetime.now() + datetime.timedelta(days=n)).strftime("%d-%m-%Y %H:%M:%S")


date_in_future([])
date_in_future(2)
