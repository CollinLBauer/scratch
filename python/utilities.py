import datetime

def get_time():
    date = datetime.date.today()
    time = datetime.datetime.now().strftime("%H:%M:%S")

    return "{}: {}".format(date,time)

