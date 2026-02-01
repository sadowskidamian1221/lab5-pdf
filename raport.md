# Lab 5 – Wybór Biblioteki - obsługa PDF w Pythonie

## Wybrana dziedzina
Obsługa plików PDF: generowanie dokumentów oraz podstawowe operacje na istniejących PDF (łączenie, odczyt).


## Biblioteka 1: ReportLab
**Przeznaczenie:** tworzenie plików PDF od zera.

### Główne funkcje
- generowanie PDF (tekst, układ strony),
- ustawianie czcionek i pozycjonowanie elementów.

### Zalety
- duża kontrola nad wyglądem PDF,
- dużo przykładów w dokumentacji.

### Ograniczenia
- trzeba ręcznie ustawiać pozycje elementów.

### Linki
- Dokumentacja: https://www.reportlab.com/documentation/
- PyPI: https://pypi.org/project/reportlab/


## Biblioteka 2: PyPDF2
**Przeznaczenie:** praca na istniejących plikach PDF (łączenie, odczyt).

### Główne funkcje
- łączenie wielu PDF w jeden,
- odczyt stron i próba ekstrakcji tekstu.

### Zalety
- proste użycie do typowych operacji,
- szybkie łączenie PDF.

### Ograniczenia
- ekstrakcja tekstu może działać różnie w zależności od typu PDF (skan).

### Linki
- Dokumentacja: https://pypdf2.readthedocs.io/
- PyPI: https://pypi.org/project/PyPDF2/