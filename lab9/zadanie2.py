import json
import yaml
from dataclasses import dataclass

"""
1. Wczytaj strukturę z pliku posts.json
2. Za pomocą dataclasses utwórz klasę odpowiadającą tej strukturze i przetwórz dane z pliku na listę instancji Twojej nowej klasy.
3. Spraw, by pole z tytułem i pole z treścią posta nie były elementem metody `__repr__` tej klasy.
4. Dodaj metodę, która zwróci całkowitą ilość znaków w poście (tytuł + treść). Posortuj listę postów po tej całkowitej długości.
5. Dodaj metodę, która zrzuci listę postów do pliku w formacie YAML.
"""

@dataclass
class Post:
    user_id: int
    id: int
    title: str
    body: str

    def __repr__(self):
        return f"user_id: {self.user_id}, id: {self.id}"

    def get_length(self):
        return len(self.title) + len(self.body)


with open("posts.json", "r") as file:
    data = ""
    for i in file:
        i.rstrip()
        data += i
    items = json.loads(data)
    posts = []
    for i in items:
        posts.append(Post(user_id=i['userId'], id=i['id'], title=i['title'], body=i['body']))

with open("posts.yaml", "w") as file:
    file.write(yaml.dump(items))