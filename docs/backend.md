# Instrukcja konfiguracji backendu i bazy danych z wtyczką Cline Roo w Visual Studio Code (Linux OpenSUSE)

## Wymagania wstępne

1. **Zainstalowany system operacyjny**: Linux OpenSUSE.
2. **Zainstalowane oprogramowanie**:
   - Visual Studio Code.
   - Wtyczka Cline Roo.
   - Python 3.9+.
   - MySQL 8+.
3. **Biblioteki Python**:
   - Flask lub Django.
   - SQLAlchemy (lub inne ORM).
   - Biblioteka PyMySQL.
4. **Inne narzędzia**:
   - Narzędzie do testowania API (np. Postman).
   - MySQL Workbench (opcjonalnie).

## Etapy konfiguracji

### 1. Instalacja wtyczki Cline Roo w Visual Studio Code
1. Otwórz Visual Studio Code.
2. Przejdź do sekcji "Extensions" (Ctrl+Shift+X).
3. Wyszukaj i zainstaluj wtyczkę **Cline Roo**.
4. Po instalacji uruchom ponownie Visual Studio Code.

### 2. Przygotowanie środowiska projektu

#### 2.1. Stwórz folder projektu

1. W terminalu Linux OpenSUSE uruchom poniższe polecenie:
   ```bash
   mkdir zakupy_app && cd zakupy_app
   ```

#### 2.2. Utwórz wirtualne środowisko Python

1. W terminalu wykonaj polecenie:
   ```bash
   python3 -m venv venv
   ```
2. Aktywuj wirtualne środowisko:
   ```bash
   source venv/bin/activate
   ```

#### 2.3. Zainstaluj wymagane biblioteki

1. Zainstaluj Flask i SQLAlchemy (lub Django, jeśli wybierasz ten framework):
   ```bash
   pip install flask flask-sqlalchemy pymysql
   ```

2. Jeśli używasz Django:
   ```bash
   pip install django mysqlclient
   ```

### 3. Stwórz bazę danych MySQL

#### 3.1. Uruchom MySQL i stwórz schemat bazy danych

1. Zaloguj się do MySQL w terminalu:
   ```bash
   mysql -u root -p
   ```
2. Wykonaj następujące polecenia w MySQL:
   ```sql
   CREATE DATABASE zakupy_db;
   USE zakupy_db;

   CREATE TABLE Kategorie (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nazwa VARCHAR(100) NOT NULL
   );

   CREATE TABLE Produkty (
       id INT AUTO_INCREMENT PRIMARY KEY,
       nazwa VARCHAR(255) NOT NULL,
       kategoria_id INT,
       czy_zamrozone BOOLEAN DEFAULT FALSE,
       data_waznosci DATE,
       FOREIGN KEY (kategoria_id) REFERENCES Kategorie(id)
   );

   CREATE TABLE Paragony (
       id INT AUTO_INCREMENT PRIMARY KEY,
       data DATE NOT NULL,
       sklep VARCHAR(100) NOT NULL,
       laczna_cena DECIMAL(10,2),
       rabat DECIMAL(10,2)
   );

   CREATE TABLE Paragon_Produkty (
       paragon_id INT,
       produkt_id INT,
       ilosc INT,
       jednostka VARCHAR(50),
       cena_jednostkowa DECIMAL(10,2),
       FOREIGN KEY (paragon_id) REFERENCES Paragony(id),
       FOREIGN KEY (produkt_id) REFERENCES Produkty(id)
   );
   ```

### 4. Stwórz backend z API

#### 4.1. Struktura plików projektu Flask

```plaintext
zakupy_app/
│
├── app.py
├── models.py
├── config.py
├── requirements.txt
└── venv/
```

#### 4.2. Kod w `config.py`

```python
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:<haslo>@localhost/zakupy_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

#### 4.3. Kod w `models.py`

```python
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class Kategorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False)

class Produkty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(255), nullable=False)
    kategoria_id = db.Column(db.Integer, db.ForeignKey('kategorie.id'))
    czy_zamrozone = db.Column(db.Boolean, default=False)
    data_waznosci = db.Column(db.Date)

class Paragony(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    sklep = db.Column(db.String(100), nullable=False)
    laczna_cena = db.Column(db.Float)
    rabat = db.Column(db.Float)
```

#### 4.4. Kod w `app.py`

```python
from flask import Flask
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route('/')
def home():
    return "API Zakupy działa!"

if __name__ == '__main__':
    app.run(debug=True)
```

### 5. Uruchomienie aplikacji

1. Upewnij się, że wirtualne środowisko jest aktywne.
2. W terminalu uruchom aplikację:
   ```bash
   python app.py
   ```
3. Sprawdź działanie w przeglądarce pod adresem: `http://127.0.0.1:5000`.

Jeśli masz pytania lub potrzebujesz dodatkowych wyjaśnień, daj znać! 😊
