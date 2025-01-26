import axios from 'axios';
import { addParagon } from '../api';

jest.mock('axios');

const mockAPI = {
  post: jest.fn()
};

axios.create.mockReturnValue(mockAPI);

test('sends POST request to add paragon', async () => {
  const data = { sklep: 'Lidl', data: '2025-01-25', cena: 100 };
  mockAPI.post.mockResolvedValue({ data: 'Success' });

  const response = await addParagon(data);
  expect(response.data).toBe('Success');
  expect(mockAPI.post).toHaveBeenCalledWith('/paragony', data);
});