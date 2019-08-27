import requests
r=requests.get('https://www.edureka.co')
c=r.content
print(c)
