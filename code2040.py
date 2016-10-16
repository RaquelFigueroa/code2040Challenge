import requests, json

tokenString = "http://challenge.code2040.org/api/register"
gitString = "https://github.com/RaquelFigueroa/code2040Challenge"


data = json.dumps({'token': tokenString, 'github': gitString})

send = requests.post(tokenString, data)