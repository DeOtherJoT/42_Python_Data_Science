import datetime as dt
import time

seconds = time.time()
date = dt.datetime.now()

print("Seconds since January 1, 1970: {0:,.4f} or {0:.2e} in scientific notation".format(seconds))
print(date.strftime("%b %d %Y"))