import React, { useState } from 'react';
import { TextField, Button, Container } from '@mui/material';
import { addParagon } from '../services/api';

const ParagonForm = () => {
  const [formData, setFormData] = useState({
    sklep: '',
    data: '',
    cena: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await addParagon(formData);
      alert('Paragon zapisany!');
    } catch (error) {
      console.error('Błąd przy zapisywaniu paragonu:', error);
    }
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