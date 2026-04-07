import pandas as pd
from datetime import date
from database import get_users, get_events, get_schedule
from logic import calculate


def generate():
    today = str(date.today())

    rows = []

    for emp, name in get_users():
        events = get_events(emp, today)
        schedule = get_schedule(emp)

        h, l, o, s = calculate(events, schedule)

        rows.append({
            "Имя": name,
            "Часы": h,
            "Опоздание": l,
            "Переработка": o,
            "Статус": s
        })

    file = "report.xlsx"
    pd.DataFrame(rows).to_excel(file, index=False)
    return file
