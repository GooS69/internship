import datetime


def date_in_future(n):
    if type(n) != int:
        print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        return
    print((datetime.datetime.now() + datetime.timedelta(days=n)).strftime("%d-%m-%Y %H:%M:%S"))


date_in_future([])
date_in_future(2)
