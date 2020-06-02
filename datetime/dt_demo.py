import time, datetime

epoch_seconds = time.time()
print(epoch_seconds)

t = time.ctime(epoch_seconds)
print(t)

dt = datetime.datetime.today()
print(dt, dt.hour, dt.minute, dt.day, dt.month)