import datetime

def days_before_new_year():
    now = datetime.datetime.today()
    NY = datetime.datetime(2023,1,1)
    d = NY-now 
    mins, sec = divmod(d.seconds, 60)
    hours, mins = divmod(mins, 60)
    print(f'До нового года: {d.days} дней {hours} часа {mins} мин {sec} сек.')
