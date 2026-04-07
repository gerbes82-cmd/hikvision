import requests
from requests.auth import HTTPBasicAuth
from config import HIKVISION
from database import add_event, event_exists


def fetch():
    url = f"http://{HIKVISION['ip']}/ISAPI/AccessControl/AcsEvent?format=json"

    try:
        r = requests.get(url, auth=HTTPBasicAuth(
            HIKVISION["username"], HIKVISION["password"]
        ), timeout=5)

        data = r.json()

        for ev in data.get("AcsEvent", {}).get("InfoList", []):
            emp = ev.get("employeeNoString")
            ts = ev.get("checkTime")

            if emp and ts and not event_exists(emp, ts):
                add_event(emp, ts)

    except Exception as e:
        print(e)
