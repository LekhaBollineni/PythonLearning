from datetime import datetime, timedelta, timezone
import time

ts1 = time.time()
seconds_since_epoch = time.time()
print(f"\n{seconds_since_epoch} seconds since epoch")
dt_utc = datetime.fromtimestamp(seconds_since_epoch, tz=timezone.utc) #datetime.now()
print(f"\nseconds_since_epoch in utc time: {dt_utc}")

def n_days_after(now, n):
    date_n_days_after = now + timedelta(days=n)
    after = date_n_days_after.strftime("%m-%d-%Y")
    return after, n

def n_days_before(now, n):
    date_n_days_before = now - timedelta(days=n)
    before = date_n_days_before.strftime("%m-%d-%Y")
    return before, n

after, a = n_days_after(dt_utc, 120)
before, b = n_days_before(dt_utc, 40)

now_formatted = dt_utc.strftime("%m-%d-%Y")
print(f"\n{a} days after {now_formatted} : {after}")
print(f"\n{b} days before {now_formatted} : {before}")

time.sleep(0.5)

ts2 = time.time()

dt1=datetime.fromtimestamp(ts1, tz=timezone.utc)
dt2=datetime.fromtimestamp(ts2, tz=timezone.utc)

time_delta = dt2-dt1
print(f"\nExecution time: {time_delta}")