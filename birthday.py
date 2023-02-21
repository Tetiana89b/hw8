from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    weekdays = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    birthday_dict = {}
    for user in users:
        name = user["name"]
        bday = user["birthday"].date()
        if bday < today:
            bday = bday.replace(year=next_week.year)
        if bday.weekday() == 5:  # Saturday
            bday = bday + timedelta(days=2)
        elif bday.weekday() == 6:  # Sunday
            bday = bday + timedelta(days=1)
        days_since_birthday = (today - bday).days
        if days_since_birthday > 0:
            continue
        if bday < next_week:
            bday_weekday = weekdays[bday.weekday()]
            if bday_weekday not in birthday_dict:
                birthday_dict[bday_weekday] = [name]
            else:
                birthday_dict[bday_weekday].append(name)
    for i in range(7):
        weekday = weekdays[(today.weekday() + i) % 7]
        if weekday in birthday_dict:
            names = ", ".join(birthday_dict[weekday])
            print(f"{weekday}: {names}")


users = [
    {'name': 'Bill', 'birthday': datetime(2023, 2, 22)},
    {'name': 'Jill', 'birthday': datetime(1999, 2, 20)},
    {'name': 'Kim', 'birthday': datetime(1993, 2, 25)},
    {'name': 'Jan', 'birthday': datetime(1991, 2, 24)},
    {'name': 'Ann', 'birthday': datetime(1988, 2, 27)},
    {'name': 'Tom', 'birthday': datetime(1992, 3, 1)}
]
get_birthdays_per_week(users)
