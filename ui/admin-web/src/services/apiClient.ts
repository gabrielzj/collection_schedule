import router from '@/router';
import axios from 'axios';
import urlJoin from 'url-join';

const baseUrl: string = 'http://localhost:8000/web-api/';

async function updateCallStatus(id: number, status: string): Promise<any> {
  try {
    console.log('ID:', id);
    console.log('Payload convertido:', JSON.stringify(status));

    const res = await axios({
      method: 'PUT',
      data: JSON.stringify({ status }),
      url: urlJoin(baseUrl, 'calls/status/', String(id), '/'),
      headers: {
        'Content-Type': 'application/json',
      },
    });
    console.log('Status updated');
    return res.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      console.error('Axios error:', error.message);
      console.error('Response data:', error.response?.data);
    }
    console.error('Error updating status:', error);
    throw error;
  }
}

async function listAllCalls() {
  try {
    const res = await axios({
      method: 'GET',
      url: urlJoin(baseUrl, '/calls'),
      headers: {
        'Content-Type': 'application/json',
      },
    });
    return res.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      console.error('Axios error:', error.message);
      console.error('Response data:', error.response?.data);
    }
    console.error('Error updating status:', error);
    throw error;
  }
}

export default {
  updateCallStatus,
  listAllCalls,
};
