import requests

url =requests.get('https://randomfox.ca/floof')
fox = url.json()

print(fox['image'])
