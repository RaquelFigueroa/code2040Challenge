import requests, json

url = "http://challenge.code2040.org/api/register"
tokenString = "be23993249a637699f148b0f39c889e0"
gitString = "https://github.com/RaquelFigueroa/code2040Challenge"


#payload = json.dumps({'token': tokenString, 'github': gitString})

payload = {'token': 'be23993249a637699f148b0f39c889e0', 'github': 'https://github.com/RaquelFigueroa/code2040Challenge'}

r = requests.post(url , payload)

print r.text