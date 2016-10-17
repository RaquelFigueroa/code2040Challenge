import json, requests

token = "be23993249a637699f148b0f39c889e0"
url = "http://challenge.code2040.org/api/haystack"

payload = {'token': token}

r = requests.post(url, payload)
data = json.loads(r.text)

needle = data["needle"]
haystack = data["haystack"]

index = -1
for idx in range(len(haystack)):
	if needle == haystack[idx]:
		index = idx

needle = index
url = "http://challenge.code2040.org/api/haystack/validate"

payload = {'token': token, 'needle': needle}
r = requests.post(url, payload)

