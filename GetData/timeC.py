from datetime import datetime, timedelta

"Date Reminder"
month = str(datetime.now().month)
if len(month) < 2:
    month = '0' + month
day = str(datetime.now().day)
if len(day) < 2:
    day = '0' + day
datefornow = f'{month}/{day}/{datetime.now().year}'
datefortogether = '07/12/2019'
date_together = datetime.strptime(datefortogether, '%m/%d/%Y')
date_now = datetime.strptime(datefornow, '%m/%d/%Y')
x = 1
while True:
    if date_now - timedelta(days=x) == date_together:
        print(f"We Have Been Together For: {x} Days")
        break
    x += 1
