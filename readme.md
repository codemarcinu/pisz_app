# Dokumentacja projektu: Aplikacja Zakupy

## Opis projektu

Aplikacja webowa stworzona w Pythonie, zgodna z konwencją Google Material Design. Celem aplikacji jest rejestrowanie zakupów na podstawie danych z paragonu, zarządzanie zawartością lodówki oraz wybieranie produktów do przygotowywania posiłków. Aplikacja będzie korzystać z bazy danych MySQL i będzie przeznaczona do użytku prywatnego.

## Główne funkcjonalności

1. **Strona główna**:

   - Zawiera odnośniki w kształcie ikon do pozostałych funkcjonalności.

2. **Wprowadzanie danych z paragonu**:

   - Formularz umożliwiający rejestrację zakupów.
   - Struktura danych zgodna z wymaganiami:
     - **Data**: Data zakupu.
     - **Sklep**: Nazwa sklepu.
     - **Produkt (nazwa)**: Nazwa zakupionego produktu.
     - **Kategoria**: Kategoria produktu.
     - **Cena jednostkowa**: Cena za jednostkę.
     - **Ilość**: Liczba zakupionych jednostek.
     - **Jednostka miary**: Jednostka miary (np. szt., kg, l).
     - **Cena**: Łączna cena przed rabatem.
     - **Rabat**: Wysokość rabatu.
     - **Cena po rabacie**: Łączna cena po uwzględnieniu rabatu.
     - **Data ważności**: Data przydatności do spożycia (jeśli dotyczy).

3. **Wyświetlanie zawartości lodówki**:

   - Lista aktualnie posiadanych produktów.
   - Opcje filtrowania i sortowania.

4. **Formularz przygotowywania posiłków**:

   - Wybór produktów z lodówki do posiłków.
   - Możliwość dodawania przepisów.

## Dodatkowe dane

Aplikacja obsługuje następujące jednostki miary, sklepy oraz kategorie produktów:

### Jednostki
- opakowanie
- sztuka
- litr
- gram

### Sklepy
- Lidl
- Biedronka
- Carrefour
- Kaufland
- Żabka
- Auchan
- Rossmann

### Kategorie produktów
- nabiał
- pieczywo
- mięso
- wędliny
- mrożonki
- owoce świeże
- warzywa świeże
- produkty suche

### Dodatkowa informacja
- **Czy zamrożone**: Informacja, czy produkt jest przechowywany w stanie zamrożonym (tak/nie).

## Technologie

- Backend: Python (Flask/Django).
- Frontend: React + Material-UI.
- Baza danych: MySQL.

## Wymagania systemowe

- Python 3.9+
- Node.js 14+
- MySQL 8+

## Instalacja

1. Klonuj repozytorium:

   ```bash
   git clone <repo-url>
   ```

2. Zainstaluj zależności backendu:

   ```bash
   pip install -r requirements.txt
   ```

3. Zainstaluj zależności frontendu:

   ```bash
   cd frontend
   npm install
   ```

4. Skonfiguruj bazę danych (pliki migracji zostaną dostarczone).

5. Uruchom aplikację:

   - Backend:
     ```bash
     python app.py
     ```
   - Frontend:
     ```bash
     npm start
     ```

## Plan pracy nad projektem

### Etap 1: Projektowanie

1. Zebranie wymagań (ukończone).
2. Projekt bazy danych:
   - Tabele: Produkty, Kategorie, Paragony, Posiłki.
3. Stworzenie prototypu interfejsu użytkownika (Figma lub inny).

### Etap 2: Backend

1. Konfiguracja środowiska lokalnego.
2. Stworzenie API:
   - Endpointy do zarządzania danymi paragonów, produktów i posiłków.
3. Implementacja funkcji OCR do odczytu danych z paragonów (np. biblioteka Tesseract).
4. Integracja z API Google Drive:
   - Automatyczne pobieranie plików z tekstem przetworzonym przez OCR w Google Docs.
   - Obsługa różnych formatów paragonów.
5. Testowanie API (Postman/Insomnia).

### Etap 3: Frontend

1. Przygotowanie struktury projektu React.
2. Implementacja widoków (Material-UI):
   - Strona główna z ikonami.
   - Formularz wprowadzania paragonów.
   - Wyświetlanie zawartości lodówki.
   - Formularz przygotowywania posiłków.
3. Integracja z API.

### Etap 4: Testowanie i wdrożenie

1. Testy jednostkowe i integracyjne.
2. Wdrożenie aplikacji (np. Heroku lub AWS).
3. Dokumentacja użytkownika.

## Sugestie dodatkowe

1. **Automatyzacja wprowadzania danych z paragonu**:
   - Dodanie funkcji OCR do automatycznego odczytu danych z paragonów (np. biblioteka Tesseract).
   - Integracja z Google Docs OCR dla obsługi bardziej skomplikowanych paragonów.
2. **Personalizacja przepisów**:
   - Opcja zapisywania ulubionych przepisów.
   - System rekomendacji w oparciu o zawartość lodówki.
3. **Bezpieczeństwo**:
   - Autoryzacja i uwierzytelnianie (JWT).
4. **Responsywność**:
   - Zoptymalizowanie interfejsu pod urządzenia mobilne.

Jeśli masz jakieś uwagi lub pomysły na dodatkowe funkcje, daj znać!

