import requests, json

url = "http://challenge.code2040.org/api/register"
tokenString = "be23993249a637699f148b0f39c889e0"
gitString = "https://github.com/RaquelFigueroa/code2040Challenge"


data = json.dumps({'token': tokenString, 'github': gitString})

send = requests.post(url, data)

print send.json