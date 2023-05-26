from dataclasses import dataclass
from urllib.request import urlopen, Request
import json

@dataclass
class Article:
    Title: str
    UserId: int
    Id: int
    

def getArticlesToShow(userIDFilter):



    lista = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    reg_url = "https://fakestoreapi.com/products"
    req = Request(url=reg_url, headers=headers)
    response = urlopen(req)
    data_json = json.loads(response.read().decode('utf-8'))
    for album in data_json:
        title = album['title']
        userId = int(album['userId'])
        id = int(album['id'])
        if userId == int(userIDFilter):
            lista.append(Article(title,userId,id))        
    return lista



x = getArticlesToShow(1)
print(x)
