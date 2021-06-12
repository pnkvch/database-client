### Artur Pinkevych, GL 05

<br>

# Klient bazy danych

## Funkcjonalność

- Głowne okno programu wyświetla nazwę oraz tabele jeżeli one są w bazie. Jeżeli nie, to będzie wyświetlony napis "No available tables". Głowne okno także zawiera przycisk do dodania tabeli.
- Po wciśnięciu przycisku "Add table" pojawi się okienko do dodania nazwy tabeli oraz odpowiednich kolumn z ich typami. Po wciśnięciu przycisku "Submit Data" będzie przeprowadzone sprawdzenie, czy nazwa tabeli nie jest pusta oraz czy wszystkie kolumny zawierają nazwy.
- Po dodaniu tabeli pojawią się przyciski "Add Row" oraz "Remove Row" do zarządzania recordami.
- Po wciśnięciu przycisku "Add Row" pojawi się okno, gdzie użytkownik wprowadza dane do wypełnienia tabeli. Po wciśnięciu prycisku "Sumbit data" odbywa się sprawdzenie każdej wartości w odpowiednich kolumnach z ich typami.
- Po wciśnięciu przycisku "Remove Row" pojawi się okno, gdzie użytkownik wprowadza indeks rekordu, który program ma usunąć. Po wciśnięciu prycisku "Sumbit data" pojawi się okienko, które pyta użytkownika czy napewno chce usunąć ten wiersz. Po wciśnięciu przycisku "Yes" odbywa się sprawdzenie czy indeks jest napewno liczbą oraz czy takie rekord istnieje, po czym usuwa odpowiedni rekord.
- Po wciśnięciu przycisku "Remove Table" pojawi się okno, gdzie użytkownik wprowadza indeks tabeli, którą program ma usunąć. Po wciśnięciu prycisku "Sumbit data" pojawi się okienko, które pyta użytkownika czy napewno chce usunąć tą tabelkę. Po wciśnięciu przycisku "Yes" odbywa się sprawdzenie czy indeks jest napewno liczbą oraz czy taka tabela istnieje, po czym usuwa odpowiedni rekord.

## Klasy i funkcje głowne zawarte w projekcie

### Funkcja <code>main</code>

- Zawiera inicjalizacje modułu <code>tkinter</code> oraz głownego modułu programu <code>MainInterface</code>. Na końcu funkcji jest nieskończona pętla <code>root.mainloop()</code>.

### Klasa <code>MainInterface</code>

- Głowna klasa programu, zawierająca wszystkie funkcje do sterowania danymi, zawartymi w liście <code>self.databases</code>.

### Funkcja <code>createMainInterface</code>

- Głowna funkcja programu, która tworzy wszystkie przyciski oraz tabele bazując na danych, zawartych w liście <code>self.databases</code>.

## Testy

- <code>test_00_AddTable</code> - tworzy tabele "test1" z kolumnami liczbową "ID" (typ int), dwoma tekstowymi "imię" oraz "nazwisko" oraz liczbową "wzrost" (typ float)

- <code>test_01_AddTableRow</code> - dodanie wiersza do tabeli "test1" z danymi "1", "Roch", "Przyłbipięt", "1.50"

- <code>test_02_AddTableRow</code> - dodanie wiersza do tabeli "test1" z danymi "2", "Ziemniaczysław", "Bulwiasty", "1.91"

- <code>test_03_AddIncorrectTableRow</code> - dodanie wiersza do tabeli "test1" z danymi "cztery", "bla", "bla", "-90"

- <code>test_04_AddIncorrectTableRow</code> - dodanie wiersza do tabeli "test1" z danymi "3.14", "pi", "ludolfina", "314e-2"

- <code>test_05_AttemptToDeleteTableRow</code> - próba usuwania wiersza z tabeli "test1", po czym anulowanie operacji

- <code>test_06_DeleteTableRow</code> - próba usuwania wiersza z tabeli "test1", po czym akceptacja operacji

- <code>test_07_AddSecondTable</code> - tworzy tabele "test2" z kolumnami liczbową "reserved" (typ string) oraz "kolor" typu liczba całkowita

- <code>test_08_AddTableRow</code> - dodanie wiersza do tabeli "test2" z danymi (puste pole), "1337"

- <code>test_09_AddIncorrectTableRow</code> - dodanie wiersza do tabeli "test2" z danymi "bla", "1939b"

- <code>test_10_DeleteTable</code> - próba usuwania tabeli "test1", po czym anulowanie operacji

- <code>test_11_DeleteTable</code> - próba usuwania tabeli "test1", po czym akceptacja operacji

- <code>test_12_AddTableWithIncorrectName</code> - próba utworzenia tabeli o nazwie ""

- <code>test_13_AddTableWithNoName</code> - próba utworzenia tabeli bez nazwy

- <code>test_14_AddTableWithNoColumnName</code> - próba utworzenia kolumny bez nazwy albo o nazwie ""
