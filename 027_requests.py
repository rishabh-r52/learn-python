import requests

res = requests.get('http://www.example.com/test.txt')
res.raise_for_status()
playFile = open('test.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()