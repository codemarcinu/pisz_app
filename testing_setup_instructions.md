# Instrukcja testowania aplikacji (Backend + Frontend)

## Wymagania wstępne

1. **Zainstalowane narzędzia testowe**:
   - Dla backendu:
     - `pytest`
     - `pytest-flask` (do testowania aplikacji Flask)
   - Dla frontendu:
     - `jest`
     - `react-testing-library`

2. **Uruchomiona baza danych testowa**:
   - Utwórz osobną bazę danych na potrzeby testów (np. `zakupy_db_test`).

## Etapy konfiguracji testów

### 1. Testowanie backendu

#### 1.1. Instalacja narzędzi

W wirtualnym środowisku backendu zainstaluj wymagane biblioteki:

```bash
pip install pytest pytest-flask
```

#### 1.2. Tworzenie folderu testów

W katalogu projektu backendowego stwórz folder `tests`:

```plaintext
zakupy_app/
├── app.py
├── models.py
├── config.py
├── tests/
│   ├── __init__.py
│   ├── test_app.py
└── requirements.txt
```

#### 1.3. Przykładowy test API

W pliku `tests/test_app.py` napisz przykładowy test:

```python
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"API Zakupy działa!" in response.data
```

#### 1.4. Uruchamianie testów

Aby uruchomić testy backendu, użyj polecenia:

```bash
pytest
```

### 2. Testowanie frontendu

#### 2.1. Instalacja narzędzi

Przejdź do folderu projektu frontendowego i zainstaluj wymagane biblioteki:

```bash
npm install --save-dev jest @testing-library/react @testing-library/jest-dom
```

#### 2.2. Konfiguracja testów

Upewnij się, że plik `package.json` zawiera sekcję skryptów dla testów:

```json
"scripts": {
  "test": "react-scripts test"
}
```

#### 2.3. Tworzenie testów dla komponentów

W folderze `src` stwórz strukturę testów:

```plaintext
src/
├── components/
│   ├── Header.js
│   ├── __tests__/
│   │   ├── Header.test.js
└── App.js
```

#### 2.4. Przykładowy test komponentu

W pliku `components/__tests__/Header.test.js` napisz test dla nagłówka:

```javascript
import { render, screen } from '@testing-library/react';
import Header from '../Header';

test('renders header with correct title', () => {
  render(<Header />);
  const headerElement = screen.getByText(/Zakupy App/i);
  expect(headerElement).toBeInTheDocument();
});
```

#### 2.5. Testowanie integracji z API

Dodaj test żądania do backendu, np. w pliku `services/__tests__/api.test.js`:

```javascript
import axios from 'axios';
import { addParagon } from '../api';

jest.mock('axios');

test('sends POST request to add paragon', async () => {
  const data = { sklep: 'Lidl', data: '2025-01-25', cena: 100 };
  axios.post.mockResolvedValue({ data: 'Success' });

  const response = await addParagon(data);
  expect(response.data).toBe('Success');
  expect(axios.post).toHaveBeenCalledWith('/paragony', data);
});
```

#### 2.6. Uruchamianie testów

Aby uruchomić testy frontendu, użyj polecenia:

```bash
npm test
```

### 3. Tworzenie bazy danych testowej

#### 3.1. Konfiguracja bazy testowej

Dodaj konfigurację dla bazy danych testowej w pliku `config.py`:

```python
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:<haslo>@localhost/zakupy_db_test'
    TESTING = True
```

W testach backendu upewnij się, że aplikacja korzysta z tej konfiguracji.

#### 3.2. Migracje bazy testowej

Przed uruchomieniem testów wykonaj migracje dla bazy danych testowej.

### 4. Raportowanie wyników testów

Po zakończeniu testów można wygenerować raport za pomocą narzędzi takich jak `pytest-html` dla backendu lub `jest-html-reporter` dla frontendu.

Jeśli potrzebujesz szczegółów lub napotkasz problemy, daj znać! 😊
