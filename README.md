﻿# Zadanie-rekrutacyjne-Junior-AI-Developer-Oxido

## Opis Projektu
To repozytorium zawiera prostą aplikację w Pythonie, która generuje kod HTML na podstawie dostarczonego pliku tekstowego z artykułem. Aplikacja korzysta z API OpenAI do przetwarzania treści i tworzenia wysokiej jakości, strukturalnego kodu HTML spełniającego określone wytyczne.

## Funkcjonalności
- Odczyt pliku tekstowego z treścią artykułu.
- Generowanie kodu HTML zgodnie z wytycznymi, z użyciem odpowiednich tagów.
- Automatyczne wskazywanie miejsc, gdzie warto dodać obrazy, z generowaniem odpowiednich atrybutów `alt` w języku polskim.
- Zapisanie wygenerowanego kodu HTML do pliku `artykul.html`.

## Wytyczne dla Generowanego HTML
- Kod zawiera tylko zawartość do umieszczenia między tagami `<body>` i `</body>`.
- Dołączono maksymalnie 3 obrazki z odpowiednimi podpisami i atrybutami `alt`.
- Brak użycia CSS ani JavaScript.
- Nie zawiera tagów `<html>`, `<head>`, ani `<body>`.

## Jak Działa Skrypt
1. Skrypt odczytuje treść z pliku `tekst.txt`.
2. Przekazuje treść wraz z odpowiednim promptem do API OpenAI.
3. Otrzymany kod HTML zapisuje w pliku `artykul.html`.

## Użycie API OpenAI
Aplikacja używa modelu `gpt-4o-mini`, który został dobrany pod kątem wysokiej jakości generowanego kodu. 

## Uruchmianie projektu
1. Utwórz plik `.env` w katalogu głównym projektu i dodaj swój klucz API:
   OPENAI_API_KEY=twój-klucz-api
2. Zainstaluj potrzebne biblioteki
   ```
   pip install python-dotenv
   ```
   ```
   pip install openai
   ```
4. Uruchom skrypt:
    ```
   python main.py
    ```
