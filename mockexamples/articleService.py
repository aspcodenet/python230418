from dataclasses import dataclass
from urllib.request import urlopen
import json

@dataclass
class Article:
    Title: str
    UserId: int
    Id: int
    

def getArticlesToShow(userIDFilter):
    lista = []
    response = urlopen("https://jsonplaceholder.typicode.com/albums")
    data_json = json.loads(response.read().decode('utf-8'))
    for album in data_json:
        title = album['title']
        userId = int(album['userId'])
        id = int(album['id'])
        if userId == int(userIDFilter):
            lista.append(Article(title,userId,id))        
    return lista