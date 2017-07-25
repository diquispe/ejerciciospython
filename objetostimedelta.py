from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365, hours=24, minutes=20))

print("En un año será ", datetime.now() + timedelta(days=365, weeks=2, minutes=10))
