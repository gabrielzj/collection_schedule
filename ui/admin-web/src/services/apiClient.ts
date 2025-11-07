import router from '@/router';
import axios, { AxiosError } from 'axios';
import type { InternalAxiosRequestConfig } from 'axios';
import urlJoin from 'url-join';

const baseUrl: string = 'http://localhost:8000/web-api/';

const TOKEN_KEYS = {
  access: 'accessToken',
  refresh: 'refreshToken',
};

/**
 *
 * @param access
 * @param refresh
 *  salva access/refresh no localStorage
 */
function setTokens(access?: string, refresh?: string) {
  if (access) localStorage.setItem(TOKEN_KEYS.access, access);
  if (refresh) localStorage.setItem(TOKEN_KEYS.refresh, refresh);
}

/**
 * remove tokens e limpa Authorization global.
 */
function clearTokens() {
  localStorage.removeItem(TOKEN_KEYS.access);
  localStorage.removeItem(TOKEN_KEYS.refresh);
}

/**
 * lê tokens do storage.
 * @returns token
 */
function getAccessToken() {
  return localStorage.getItem(TOKEN_KEYS.access);
}

function getRefreshToken() {
  return localStorage.getItem(TOKEN_KEYS.refresh);
}

/**
 * POST auth/token/
 * @param email
 * @param password
 * @returns tokens
 */
async function getAuth(email: string, password: string) {
  const res = await axios.post(
    urlJoin(baseUrl, 'auth/token/'),
    { email, password },
    {
      headers: { 'Content-Type': 'application/json' },
    },
  );
  return res.data as { access?: string; refresh?: string };
}

/**
 *
 * @param token
 * @returns boolean
 */
async function verifyAuth(token: string): Promise<boolean> {
  try {
    await axios.post(
      urlJoin(baseUrl, 'auth/token/verify/'),
      { token },
      {
        headers: { 'Content-Type': 'application/json' },
      },
    );
    return true;
  } catch (err: any) {
    if (axios.isAxiosError(err) && !err.response) return true;
    return false;
  }
}

/**
 *
 * @param refresh
 * @returns tokens
 */
async function refreshAuth(refresh: string) {
  const res = await axios.post(
    urlJoin(baseUrl, 'auth/token/refresh/'),
    { refresh },
    {
      headers: { 'Content-Type': 'application/json' },
    },
  );
  return res.data as { access?: string; refresh?: string };
}

/**
 * POST auth/token/ e salva access/refresh
 * @param email
 * @param password
 * @returns tokens
 */
async function login(email: string, password: string) {
  const tokens = await getAuth(email, password);
  setTokens(tokens.access, tokens.refresh);
  return tokens;
}

/**
 * limpa tokens e redireciona para login
 */
async function logout() {
  clearTokens();
  await router.replace({ name: 'login' });
}

/**
 * Verifica validade do token e renova se necessário.
 * Redireciona para login se não for possível renovar.
 */
async function handleAuthToken(): Promise<void> {
  const access = getAccessToken();
  if (access) {
    const ok = await verifyAuth(access);
    if (ok) return;
  }
  const refresh = getRefreshToken();
  if (!refresh) {
    clearTokens();
    await router.replace({ name: 'login' });
    throw new Error('Sessão expirada');
  }
  const refreshIsValid = await verifyAuth(refresh);
  if (!refreshIsValid) {
    clearTokens();
    await router.replace({ name: 'login' });
    throw new Error('Sessão expirada');
  }
  try {
    const tokens = await refreshAuth(refresh);
    setTokens(tokens.access, tokens.refresh);
  } catch (err: any) {
    if (axios.isAxiosError(err) && !err.response) return;
    clearTokens();
    await router.replace({ name: 'login' });
    throw new Error('Erro ao renovar token');
  }
}

/**
 * POST users/ (cria usuário web)
 * @param payload
 * @returns
 */
async function registerUser(payload: {
  first_name: string;
  email: string;
  password: string;
  last_name?: string;
  phone_number?: string;
  address?: string;
}) {
  await handleAuthToken();
  const res = await axios.post(urlJoin(baseUrl, 'users/'), payload, {
    headers: { 'Content-Type': 'application/json' },
  });
  return res.data;
}

/**
 * PUT calls/status/{id}/ com {status}
 * @param id
 * @param status
 * @returns dados atualizados
 */
async function updateCallStatus(id: number, status: string): Promise<any> {
  await handleAuthToken();
  try {
    console.log('ID:', id);
    console.log('Payload convertido:', JSON.stringify(status));

    const res = await axios({
      method: 'PUT',
      data: JSON.stringify({ status }),
      url: urlJoin(baseUrl, 'calls/status/', String(id), '/'),
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
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

/**
 * Lista todas as chamadas
 * @returns dados das chamadas
 */
async function listAllCalls() {
  await handleAuthToken();
  try {
    const res = await axios({
      method: 'GET',
      url: urlJoin(baseUrl, '/calls'),
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
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

/**
 * Lista todos os usuários
 * @returns dados dos usuários
 */
async function listUsers() {
  await handleAuthToken();
  try {
    const res = await axios({
      method: 'GET',
      url: urlJoin(baseUrl, '/users/'),
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
      },
    });
    return res.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      console.error('Axios error:', error.message);
      console.error('Response data:', error.response?.data);
    }
    console.error('Error fetching users:', error);
    throw error;
  }
}

export default {
  login,
  logout,
  registerUser,
  updateCallStatus,
  listAllCalls,
  listUsers,
};
