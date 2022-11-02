from datetime import datetime

now = datetime.now()

day = now.strftime('%d/%m/%Y')
time = now.strftime('%H:%M:%S')
print(f"Today is {day}")
print(f"Time right now: {time}")
