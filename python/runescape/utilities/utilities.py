import datetime

def get_time():
    dateList = str(datetime.date.today()).split("-")
    dateList = [dateList[1],dateList[2],dateList[0]]
    date = "/".join(dateList)
    hours = int(datetime.datetime.now().strftime("%H"))
    minutes = datetime.datetime.now().strftime("%M:%S")
    if int(hours) > 12:
        ampm = "PM"
    else:
        ampm = "AM"
    return "{} {}:{} {}".format(date,hours%12,minutes,ampm)
