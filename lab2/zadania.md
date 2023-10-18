# Zadanie 1

Zaimplementuj funkcję, która przyjmuje jedną wartość liczbową
i zwraca tę wartość podniesioną do 3-ciej potęgi.

Następnie wywołaj i wypisz na ekran wynik działania funkcji dla
wartości: 0, 1, -3, 2e3.


# Zadanie 2

Zaimplementuj funkcję obliczającą wartość wielomianu drugiego stopnia
o parametrach zadanych w jej argumentach. Przetestuj ją dla różnych argumentów.


# Zadanie 3

Napisz funkcję, która przyjmuje parametr określający imię, numer zadania oraz
czas wykonania zadania wyrażony w milisekundach, a następnie generuje i zwraca
tekst informujący o wykonaniu przez podaną osobę danego zadania w określonym czasie.
Wyraź czas w sekundach określonych z dokładnością do trzeciego miejsca po przecinku.

Przykład:

> Adam wykonał(a) zadanie nr 1 w 123.052s.

Użyj jej do napisania programu informującego o ukończeniu przez Ciebie
tego zadania (podaj zmyślony czas wykonania, np. 555111ms).


# Zadanie 4

Napisz funkcję, która akceptuje dwa punkty w przestrzeni dwuwymiarowej i
zwraca punkt znajdujący się na symetralnej odcinka stworzonego przez argumenty wejściowe.
Punkty reprezentuj za pomocą dwuelementowej krotki.


# Zadanie 5

Napisz funkcję, która zwraca liczbę cyfr dwójkowej reprezentacji liczby podanej
w argumencie. Poszukaj stosownej funkcji wbudowanej w dokumentacji Pythona
lub za pomocą podpowiedzi w powłoce interaktywnej (nazwa funkcji
zaczyna się na literę "b").


# Zadanie 6

Napisz funkcje, które obliczają przedział wartości oraz średnią wartość liczb
podanych w krotce. Możesz założyć, że krotka zawiera co najmniej jeden element.


# Zadanie 7

Napisz funkcję, która przyjmuje szerokość, wysokość oraz długość obiektu,
a następnie prezentuje je za pomocą tabeli. Wymiary wypisz jako liczby
dziesiętne z dokładnością do 3-go miejsca po przecinku.

Przykład:
```
 Wymiar    |  Wartość
----------------------
 Szerokość | 2434.400
 Wysokość  |   35.350
 Długość   |    0.202
```

Zadbaj o minimalną szerokość obu kolumn tabeli. Zapewnij margines o szerokości
jednego odstępu. Tekst powinien być wyrównany do zewnętrznej strony tabeli
(do lewej w lewej kolumnie i do prawej w prawej kolumnie).

## Zalecany plan działań

### 1. Zaimplementuj funkcję `format_row`

Każdy wiersz tabeli składa się z dwóch komórek. Funkcja powinna przyjmować
zatem 2 argumenty - odpowiadające lewej i prawej komórce. Każdą komórkę opisz
za pomocą dwuelementowej krotki zawierającej jej tekst i szerokość. Wartością
zwracaną przez funkcję powinien łańcuch tekstu reprezentujący pojedynczy wiersz
tabeli, np.:

```
>>> format_row(("Szerokość", 12), ("240.000", 12))
"  Szerokość  |   240.000   "
```

### 2. Zaimplementuj wstępną wersję docelowej funkcji

We wstępnej wersji funkcji zignoruj wymóg na optymalną szerokość kolumny i
przyjmij dla obu z nich wartość 20. Pamiętaj o wykorzystaniu funkcji
zaimplementowanej wcześniej funkcji `format_row` - ułatwi to wykonanie 
kolejnych kroków.

### 3. Zaimplementuj funkcję `optimal_column_width`

Funkcja ta przyjmuje nagłówek kolumny oraz krotkę zawierającą tekstowe
reprezentacje wartości występujących w kolumnie. Funkcja zwraca najmniejszą
szerokość, przy której w każdej komórce jest zachowany margines o szerokości
co najmniej 1.

```
>>> optimal_column_width("4444", ("333", "22", "55555"))
7
```

### 4. Zaimplementuj finalną wersję docelowej funkcji

Użyj funkcji `optimal_column_width` do obliczenia optymalnej szerokości
każdej z kolumn i zastąp nimi wartość 20 przyjętą w kroku 2.


# Zadanie 8 (Opcjonalne)

Napisz funkcję, która oblicza pierwiastki równania kwadratowego o zadanych
parametrach.
