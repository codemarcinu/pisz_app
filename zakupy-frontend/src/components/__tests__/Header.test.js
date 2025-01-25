import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import Header from '../Header';

test('renders header with correct title', () => {
  render(<Header />);
  const headerElement = screen.getByText(/Zakupy App/i);
  expect(headerElement).toBeInTheDocument();
});