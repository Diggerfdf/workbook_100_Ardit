import requests

response = requests.get("http://www.pythonhow.com/data/universe.txt")
text = response.text


count = text.count("a")

print(count)
