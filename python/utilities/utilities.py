import datetime

def get_time(locale="US"):

    date_list = str(datetime.date.today()).split("-")
    hours = int(datetime.datetime.now().strftime("%H"))
    minutes = datetime.datetime.now().strftime("%M:%S")

    if locale == "US":
        date_list = [date_list[1],date_list[2],date_list[0]]
        date = "/".join(date_list)
    
        if int(hours) > 12:
            ampm = "PM"
        else:
            ampm = "AM"
        return "{} {}:{} {}".format(date,hours%12,minutes,ampm)
    else:
        print("Locale {} is not supported.".format(locale))
        return None