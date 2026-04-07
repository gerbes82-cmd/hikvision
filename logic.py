from datetime import datetime


def calculate(events, schedule):
    if not schedule or len(events) < 2:
        return 0, 0, 0, "Нет данных"

    days, start, end = schedule
    days = list(map(int, days.split(",")))

    times = [datetime.fromisoformat(e) for e in events]

    worked = 0
    for i in range(0, len(times)-1, 2):
        worked += (times[i+1] - times[i]).total_seconds()

    hours = worked / 3600

    weekday = times[0].weekday() + 1

    if weekday not in days:
        return hours, 0, hours, "Выходной"

    late = max(0, (times[0].hour - start) * 60 + times[0].minute)

    norm = end - start
    overtime = max(0, hours - norm)

    return round(hours, 2), late, round(overtime, 2), "Рабочий"
