# Instrukcja konfiguracji frontendu i integracji z backendem (React + Material-UI)

## Wymagania wstępne

1. **Zainstalowane oprogramowanie**:
   - Node.js 14+ (w tym npm lub yarn).
   - Visual Studio Code.
   - Backend z wcześniejszych kroków uruchomiony lokalnie.

2. **Zainstalowane biblioteki**:
   - React.
   - Material-UI (MUI).
   - Axios (do obsługi żądań HTTP).

## Etapy konfiguracji

### 1. Utworzenie projektu React

1. W terminalu przejdź do głównego folderu projektu, a następnie utwórz nowy projekt React:
   ```bash
   npx create-react-app zakupy-frontend
   cd zakupy-frontend
   ```

2. Uruchom lokalny serwer deweloperski, aby upewnić się, że projekt działa:
   ```bash
   npm start
   ```

### 2. Instalacja dodatkowych bibliotek

1. Zainstaluj Material-UI oraz Axios:
   ```bash
   npm install @mui/material @emotion/react @emotion/styled axios
   ```

2. Opcjonalnie: Zainstaluj ikonki Material-UI:
   ```bash
   npm install @mui/icons-material
   ```

### 3. Struktura projektu

Zmień domyślną strukturę folderów na następującą:

```plaintext
zakupy-frontend/
│
├── public/
├── src/
│   ├── components/
│   │   ├── Header.js
│   │   ├── Footer.js
│   │   └── ParagonForm.js
│   │
│   ├── pages/
│   │   ├── Home.js
│   │   └── Products.js
│   │
│   ├── services/
│   │   └── api.js
│   │
│   ├── App.js
│   ├── index.js
│   └── styles.css
│
└── package.json
```

### 4. Tworzenie podstawowych komponentów

#### 4.1. `Header.js`

Stwórz prosty nagłówek z Material-UI:

```jsx
import React from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';

const Header = () => {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6">Zakupy App</Typography>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
```

#### 4.2. `ParagonForm.js`

Komponent formularza do wprowadzania danych paragonu:

```jsx
import React, { useState } from 'react';
import { TextField, Button, Container } from '@mui/material';

const ParagonForm = () => {
  const [formData, setFormData] = useState({
    sklep: '',
    data: '',
    cena: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
  };

  return (
    <Container>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Sklep"
          name="sklep"
          value={formData.sklep}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Data"
          name="data"
          type="date"
          value={formData.data}
          onChange={handleChange}
          fullWidth
          margin="normal"
          InputLabelProps={{ shrink: true }}
        />
        <TextField
          label="Cena"
          name="cena"
          type="number"
          value={formData.cena}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <Button type="submit" variant="contained" color="primary">
          Zapisz
        </Button>
      </form>
    </Container>
  );
};

export default ParagonForm;
```

### 5. Integracja z backendem

#### 5.1. Utwórz plik `api.js` w folderze `services`

Ten plik będzie odpowiedzialny za obsługę żądań do backendu:

```javascript
import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:5000', // URL backendu
});

export const addParagon = (data) => API.post('/paragony', data);
export const fetchProducts = () => API.get('/produkty');
```

#### 5.2. Użyj `api.js` w `ParagonForm.js`

Zmień funkcję `handleSubmit`, aby wysyłała dane do backendu:

```jsx
import { addParagon } from '../services/api';

const handleSubmit = async (e) => {
  e.preventDefault();
  try {
    await addParagon(formData);
    alert('Paragon zapisany!');
  } catch (error) {
    console.error('Błąd przy zapisywaniu paragonu:', error);
  }
};
```

### 6. Uruchomienie projektu

1. Upewnij się, że backend działa.
2. Uruchom frontend:
   ```bash
   npm start
   ```
3. Otwórz przeglądarkę i przejdź pod adres `http://localhost:3000`.

Jeśli masz pytania lub napotkasz problemy, daj znać! 😊
