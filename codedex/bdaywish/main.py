import datetime, bday_messages
today = datetime.date.today()
next_birthday = datetime.date(today.year, 5, 12)
days_away = (next_birthday - today).days
if today == next_birthday:
    print(bday_messages.random_message)
else:
    if days_away < 0:
        next_birthday = datetime.date(today.year + 1, 5, 12)
        days_away = (next_birthday - today).days
    print(f"Your birthday is in {days_away} days. Get ready to celebrate!")
