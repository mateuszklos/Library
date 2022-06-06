
# MyBookStore



Projekt na przykładzie księgarni. Umożliwia przeglądanie dostępnych książek bez konieczności logowania.
Logując się, użytkownik uzyskuje możliwość dodania pozycji do swojej listy wypożyczonych książek.

## tworzenie konta

Użytkownik ma możliwość stworzenia konta. Pod stroną /register pokazuje się formularz rejestracji. Należy wprowadzić username, email, hasło.


## login
Gdy użytkownik utworzył konto, może się zalogować pod adresem /login. W przypadku podania błędnych danych logowania, pokaże się stosowny komunikat. Będąc na stronie głównej po zalogowaniu, wpisując /login raz jeszcze do adresu url, użytkownik zostanie przekierowany z powrotem do strony głównej.

## książki
Serwis zawiera listę książek. Listą tą zarządza administrator, który może dodawać książki i autorów z panelu /admin.
Użytkownik może wypożyczyć książkę (o ile ktoś wcześniej tego nie zrobił). Książka wypożyczona będzie widnieć wciąż w spisie, ale także w liście wypożyczonych książek na profilu użytkownika. Książka wypożyczona dla innych użytkowników będzie mieć zablokowaną możliwość wypożyczenia, póki wypożyczający jej nie zwróci. Zamiast przycisku 'borrow' będzie wtedy widniał 'borrowed by {użytkownik}'. Serwis posiada także zabezpieczenia, które zapobiegają wypożyczanie już zajętych książek. Chcąc w adresie url wypożyczyć zajętą książke, strona zwróci stosowny komunikat.
Model Book odpowiada za książkę i posiada następujące atrybuty:
* title - tytuł, ciąg znaków z maksymalną długością 50
* author - autor, klucz obcy do modelu Author z relacją one-to-one
* date - data wydania książki, pole typu DateField
* genre  - wybór spośród gatunków 
* user - użytkownik posiadający książkę (gdy nikt jej nie posiada - Null)
* is_in_list - boolean informujący o tym, czy książka jest wypożyczona, czy nie

Model Author posiada następujące atrybuty:
* name - imię autora, ciąg znaków z maksymalną długością 50
* last_name - nazwisko autora, ciąg znaków z maksymalną długością 50
* birthday - data urodzenia autora, pole typu DateField

Książki są stronicowane po 8 elementów na stronę (dla str. głównej, listy i wyników wyszukiwania)
## wyszukiwanie

Na stronie głównej znajduje się pole z wyszukiwaniem książki po tytule. Wpisując tytuł (lub jego fragment) i zatwierdzając formularz poprzez kliknięcie 'enter', pokazują się wyniki wyszukiwania. Gdy nie ma wyników, pokazuje się stosowny komunikat.

## responsywność
Front end strony został wykonany w Bootstrap Studio. Użycie frameworka bootstrap, oraz poprawne rozmieszczenie elementów, zapewniają poprawne wyświetlanie strony na wszystkich rozdzielczościach urządzeń.

