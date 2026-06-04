''' pip install tzdata for windows'''
from datetime import datetime
from zoneinfo import ZoneInfo

dt_utc = datetime.now(tz=ZoneInfo("UTC"))
dt_ny = datetime.now(tz=ZoneInfo("America/New_York"))
dt_chicago = datetime.now(tz=ZoneInfo("America/Chicago"))
dt_mumbai = datetime.now(tz=ZoneInfo("Asia/Kolkata"))


print("Current time in different timezones:")
print(f"UTC: {dt_utc}\nNewYork: {dt_ny}\nChicago: {dt_chicago}\nMumbai: {dt_mumbai}")
