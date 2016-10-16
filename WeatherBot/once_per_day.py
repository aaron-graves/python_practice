from datetime import datetime
from threading import Timer
from weather_bot import weather_update

x=datetime.today()
y=x.replace(day=x.day+1, hour=7, minute=0, second=0, microsecond=0)

delta_t=y-x
secs=delta_t.seconds+1

t = Timer(secs, weather_update)
t.start()