from zipfile import ZipFile

"""

1. Wykorzystaj moduł `zipfile` do rozpakowania archiwum z plikami.
Skorzystaj z: https://docs.python.org/3/library/zipfile.html1. 
Wykorzystaj moduł `pathlib`, aby znaleźć w rozpakowanej strukturze katalogów wszystkie pliki z rozszerzeniem .txt. 
Posortuj listę tych plików według ich nazw, a następnie odczytaj każdy z nich i połącz ich treść w jeden napis.
Skorzystaj z: https://docs.python.org/3/library/pathlib.html
Sortowanie: https://docs.python.org/3/howto/sorting.html

"""

with ZipFile("documents.zip", 'r') as zip:
    items = zip.filelist
    zip.extractall()


file = open("text.txt", "w")

sorted_items = sorted(items, key=lambda item: item.filename.split("/")[-1])

for i in sorted_items:
    if i.filename.endswith(".txt"):
        with open(i.filename, "r") as f:
            text = ""
            for j in f:
                text += j
            file.write(text + " ")

file.close()








