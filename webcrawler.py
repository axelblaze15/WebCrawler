import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/Float_(project_management)")

html = response.text

soup = BeautifulSoup(html,'html.parser')

print soup.prettify()
# anchors = soup.find_all('a')
# for each_element in anchors:
#   print each_element

# for link in soup.find_all('a'):
#   print link.get('href')

print soup.find(id = "mw-context-text").find(class_="mw-parser-output").p.a.get('href')

# search_history = ['https://en.wikipedia.org/wiki/Floating_point']
# target_url = 'https://en.wikipedia.org/wiki/Philosophy'
# if len(search_history) > 25:
#     print False
#     #pass
# if search_history[-1] == target_url:
#     print False
#         #pass
# visited = {}
# for key in search_history:
#     if not visited.get(key):
#         visited[key] = 1
#     else:
#         print False
# print True