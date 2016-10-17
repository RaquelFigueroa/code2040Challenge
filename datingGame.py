import requests, json
from datetime import datetime, time, timedelta

token = "be23993249a637699f148b0f39c889e0"
url = "http://challenge.code2040.org/api/dating"

#Request dictionary for challenge:
payload = {"token": token}
r = requests.post(url, payload)

#convert dictionary from json to python and store values:
data = json.loads(r.text)
datestamp = data["datestamp"]
interval = data["interval"]

#convert datestamp from iso 8601 to date string
time = datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")
increment = timedelta(seconds = interval)

#add increment time to datestamp
finaldate = time+increment

#convert finadate to iso 8601 format and add 'Z':
isodate = finaldate.isoformat()
isodate = isodate + 'Z'


url = "http://challenge.code2040.org/api/dating/validate"
payload = {"token": token, "datestamp": isodate}
r = requests.post(url, payload)
print r