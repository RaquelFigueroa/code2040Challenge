import json, requests

token = "be23993249a637699f148b0f39c889e0"
url = "http://challenge.code2040.org/api/prefix"
payload = {'token' : token}

r = requests.post(url, payload)

dictionary = json.loads(r.text)

prefix = dictionary["prefix"]
array = dictionary["array"]

newArray = []
for word in array:
	if not word.startswith(prefix):
		newArray.append(word)
print newArray

url = "http://challenge.code2040.org/api/prefix/validate"
payload ={"token": token, "array":newArray}


r = requests.post(url, payload)
print r