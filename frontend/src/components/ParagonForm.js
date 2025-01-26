import React, { useState, useEffect } from 'react';
import { TextField, Button, Container, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material';
import { addParagon, fetchParagony } from '../services/api';

const ParagonForm = () => {
  const [paragony, setParagony] = useState([]);
  const [formData, setFormData] = useState({
    sklep: '',
    data: '',
    cena: '',
  });

  useEffect(() => {
    const pobierzParagony = async () => {
      try {
        const response = await fetchParagony();
        setParagony(Array.isArray(response.data) ? response.data : []);
      } catch (error) {
        console.error('Błąd podczas pobierania paragonów:', error);
        setParagony([]);
      }
    };
    pobierzParagony();
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await addParagon(formData);
      const response = await fetchParagony();
      setParagony(Array.isArray(response.data) ? response.data : []);
      alert('Paragon zapisany!');
    } catch (error) {
      console.error('Błąd przy zapisywaniu paragonu:', error);
    }
  };

  return (
    <Container>
      <TableContainer component={Paper} sx={{ marginBottom: 4 }}>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Data</TableCell>
              <TableCell>Sklep</TableCell>
              <TableCell align="right">Cena</TableCell>
              <TableCell align="right">Rabat</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {paragony.map((paragon) => (
              <TableRow key={paragon.id}>
                <TableCell>
                  {new Date(paragon.data).toLocaleDateString()}
                </TableCell>
                <TableCell>{paragon.sklep}</TableCell>
                <TableCell align="right">{paragon.laczna_cena.toFixed(2)} zł</TableCell>
                <TableCell align="right">{paragon.rabat.toFixed(2)} zł</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

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