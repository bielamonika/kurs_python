#Zadanie 1 - 'Wisielec':
Program, będący implementacją gry "wisielec".
1. Program zaczyna od pobrania z pliku json listy dostepnych hasel 
   w ramach 3 kategorii. Wybiera losowe haslo z kategorii wybranej
   przez uzytkownika.
   Haslo sklada sie wylacznie z malych liter:

        word = str(data[category][random.randint(0,8)]).lower()
 
2. Program tworzy dwie listy - litery, ktore uzytkownik odgadl (letters_guessed)
   oraz te, ktore jeszcze zostaly do odgadniecia (letters_left).
   Program konczy dzialanie kiedy iterator runda osiagnie wartosc runda_max 
   lub kiedy letters_left bedzie pusta (czyli kiedy wszystkie litery zostana odgadniete).
3. Program wyswietla calkowita ilosc znakow oraz odgadniete do tej pory litery po czym prosi
   uzytkownika o podanie litery.
    a. Jesli znajduje sie na liscie letters_left, zostaje z niej usunieta i dodana do listy 
       letters_guessed w miejscu, gdzie oryginalnie znajduje sie w hasle:
       
            for i in range(0, len(password)):
                if password[i] == new_letter:
                    letters_guessed[i] = new_letter
       
       Wyswietlony zostaje komunikat o wygranej.
    b. Jesli uzytkownik zgadnie haslo od razu, petla konczy dzialanie
    c. Jesli nie ma jej na liscie, pojawia sie komunikat o przegranej oraz ilosci pozostalych rund.
4. Po zakonczeniu petli wyswietlony zostaje komunikat o wygranej lub przegranej wraz z haslem.

#Zadanie 2 - "Ksiazka adresowa":
Program przechowujący danę kontaktowe znajomych/klientów.
1. Program zaczyna dzialanie od wyswietlenia listy dostepnych operacji na ksiazce adresowej, zapisanej jako slownik.
2. Uzytkownik po wpisaniu okreslonego slowa kluczowego moze wyswietlic ksiazke adresowa, dodac lub usunac dowolny wpis
   lub zakonczyc dzialanie programu.
3. Uzytkownik nie moze dodac osoby, ktora juz widnieje w ksiazce oraz usunac osoby, ktorej w niej nie ma.
   Petla wymusza podanie prawidlowych danych.
   Po dokonaniu zmian wyswietlona zostaje zawartosc ksiazki.
