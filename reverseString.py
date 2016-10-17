import requests, json

url = "http://challenge.code2040.org/api/reverse"
tokenString = "be23993249a637699f148b0f39c889e0"

reversedUrl = "http://challenge.code2040.org/api/reverse/validate"

payload = {'token': tokenString}

r = requests.post(url , payload)

toReverse = r.text
reversedWord = toReverse[::-1]

payload = {'token': tokenString, 'string': reversedWord}
rFinal = requests.post(reversedUrl, payload)
print rFinal