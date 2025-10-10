import router from "@/router";
import axios from "axios";
import urlJoin from "url-join";

interface AuthResponse {
  access?: string;
  refresh?: string;
}

const baseUrl: string =
  process.env.NGROK_URL || "http://localhost:8000/app-api/";
const userBaseUrl: string = urlJoin(baseUrl, "users/");

/**
 *
 * @param email
 * @param password
 * @returns access_token e refresh_token
 */
async function getAuth(email: string, password: string): Promise<AuthResponse> {
  try {
    const res = await axios({
      method: "POST",
      url: urlJoin(baseUrl, "auth/token/"),
      data: {
        email,
        password,
      },
    });
    localStorage.setItem("user_id", res.data.id);
    return res.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      console.error("Axios error:", error.message);
    }
    if (error.response && error.response.data) {
      return error.response.data;
    }
    console.error("Error fetching auth token:", error);
    throw error;
  }
}

/**
 * @param token
 * Verifica se um token é válido
 */
async function verifyAuth(token: string): Promise<boolean> {
  try {
    const res = await axios({
      method: "POST",
      url: urlJoin(baseUrl, "auth/token/verify/"),
      data: {
        token: token,
      },
    });
    return true;
  } catch (error: any) {
    // Se for erro de rede (ex.: backend offline), não considerar o token inválido.
    if (axios.isAxiosError(error) && !error.response) {
      console.warn(
        "Não foi possível verificar o token (servidor indisponível). Mantendo sessão até reconexão."
      );
      return true; // Preserva sessão para evitar logout indevido quando o backend estiver offline
    }
    console.error(
      "Token inválido:",
      axios.isAxiosError(error) ? error.response?.data || error.message : error
    );
    return false;
  }
}

/**
 * @param token
 * Renova um token a partir de um refresh token, retorna um novo refresh token
 */
async function refreshAuth(token: string): Promise<AuthResponse> {
  try {
    const res = await axios({
      method: "POST",
      url: urlJoin(baseUrl, "auth/token/refresh/"),
      data: {
        refresh: token,
      },
    });
    return res.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      console.error("Axios error:", error.message);
    }
    if (error.response && error.response.data) {
      return error.response.data;
    }
    console.error("Error refreshing auth token:", error);
    throw error;
  }
}

/**
 * @returns void
 * Verifica e renova tokens conforme necessário, redireciona para login se inválido
 */
async function handleAuthToken(): Promise<void> {
  const storage: Storage | null = localStorage.getItem("access_token")
    ? localStorage
    : sessionStorage.getItem("access_token")
    ? sessionStorage
    : null;

  const accessToken = storage?.getItem("access_token") || null;

  if (!accessToken) {
    router.replace("/login");
    throw new Error("Token de acesso não encontrado");
  }

  // Verifica se o access token é válido
  const isAccessTokenValid = await verifyAuth(accessToken);

  // Access token inválido, tenta renovar com refresh token
  if (!isAccessTokenValid) {
    console.log("Access token inválido, tentando renovar...");

    const refreshToken =
      storage?.getItem("refresh_token") ||
      localStorage.getItem("refresh_token") ||
      sessionStorage.getItem("refresh_token");

    if (!refreshToken) {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      sessionStorage.removeItem("access_token");
      sessionStorage.removeItem("refresh_token");
      router.replace("/login");
      throw new Error("Refresh token não encontrado");
    }

    // Verifica se o refresh token é válido
    const isRefreshTokenValid = await verifyAuth(refreshToken);
    if (!isRefreshTokenValid) {
      console.log("Refresh token inválido, redirecionando para login...");
      // Refresh token também inválido, redireciona para login
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      sessionStorage.removeItem("access_token");
      sessionStorage.removeItem("refresh_token");
      router.replace("/login");
      throw new Error("Sessão expirada. Faça login novamente");
    }

    try {
      console.log("Refresh válido, renovando access token...");
      // Renova o access token usando o refresh token
      const newTokens = await refreshAuth(refreshToken);
      (storage || localStorage).setItem("access_token", newTokens.access || "");
      (storage || localStorage).setItem(
        "refresh_token",
        newTokens.refresh || ""
      );
    } catch (error) {
      // Se for erro de rede, manter sessão e permitir que a chamada original falhe por rede.
      if (axios.isAxiosError(error) && !error.response) {
        console.warn(
          "Servidor indisponível ao tentar renovar token. Mantendo sessão e aguardando reconexão."
        );
        return; // Não limpa tokens nem redireciona em caso de offline
      }
      console.log("Erro ao renovar token, redirecionando para login...");
      // Erro ao renovar token (não relacionado à rede)
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      sessionStorage.removeItem("access_token");
      sessionStorage.removeItem("refresh_token");
      router.replace("/login");
      throw new Error("Erro ao renovar token. Faça login novamente");
    }
  }
}

/**
 *
 * @param payload
 * @returns data da chamada criada
 * Cria uma nova chamada na API
 */
async function createCall(payload: any): Promise<any> {
  await handleAuthToken();
  try {
    const res = await axios({
      method: "POST",
      url: urlJoin(baseUrl, "calls/"),
      data: payload,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${
          localStorage.getItem("access_token") ||
          sessionStorage.getItem("access_token")
        }`,
      },
    });
    console.log(res.data);
    // router.replace({ name: "Login" });
    return res.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      console.error("Axios error:", error.message);
      console.error("Headers:", error.response?.headers);
    }
    if (error.response && error.response.data) {
      return error.response.data;
    }
    console.error("Error fetching auth token:", error);
    throw error;
  }
}

/**
 *
 * @param payload
 * @returns data novo user
 */

async function registerUser(payload: any): Promise<any> {
  try {
    const res = await axios({
      method: "POST",
      // url: urlJoin(baseUrl, "users/"),
      url: userBaseUrl,
      data: payload,
      headers: {
        "Content-Type": "application/json",
      },
    });
    console.log("Usuário criado");
    return res.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      console.error("Axios error:", error.message);
      console.error("Response data:", error.response?.data);
    }
    console.error("Error creating user:", error);
    throw error;
  }
}

/**
 *
 * @param userID
 * @returns user data
 */

async function getUser(userID: any): Promise<any> {
  await handleAuthToken();
  try {
    const res = await axios({
      method: "GET",
      url: urlJoin(userBaseUrl, userID.toString()),
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${
          localStorage.getItem("access_token") ||
          sessionStorage.getItem("access_token")
        }`,
      },
    });
    return res.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      console.error("Axios error:", error.message);
      console.error("Response data:", error.response?.data);
    }
  }
}

/**
 *
 * @param userID
 * @param method
 * @param payload
 * @returns updated user
 */
async function updateUser(
  userID: number | string | null,
  method: "PUT",
  payload: any
): Promise<any> {
  await handleAuthToken();
  try {
    const res = await axios({
      method,
      url: urlJoin(userBaseUrl, String(userID), "/"),
      data: payload,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${
          localStorage.getItem("access_token") ||
          sessionStorage.getItem("access_token")
        }`,
      },
    });
    return res.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      console.error("Axios error:", error.message);
      console.error("Response data:", error.response?.data);
    }
  }
}

/**
 *
 * @returns call info
 */
async function getCalls(): Promise<any> {
  await handleAuthToken();
  try {
    const res = await axios({
      method: "GET",
      url: urlJoin(baseUrl, "calls/"),
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${
          localStorage.getItem("access_token") ||
          sessionStorage.getItem("access_token")
        }`,
      },
    });
    return res.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      console.error("Axios error:", error.message);
      console.error("Response data:", error.response?.data);
    }
  }
}

/**
 *
 * @param callID
 *
 */

async function deleteCall(callID: number): Promise<any> {
  await handleAuthToken();
  try {
    const res = await axios({
      method: "DELETE",
      url: urlJoin(baseUrl, "calls/", callID.toString(), "/"),
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${
          localStorage.getItem("access_token") ||
          sessionStorage.getItem("access_token")
        }`,
      },
    });
    return res.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      console.error("Axios error:", error.message);
      console.error("Response data:", error.response?.data);
    }
  }
}

/**
 *
 * @param callID
 * @returns call updated
 */
async function updateCall(
  callID: number | string | null,
  payload: any
): Promise<any> {
  await handleAuthToken();
  console.log("id no apiclient:", callID);
  console.log("data no apiclient:", payload);
  // String(callID)
  try {
    const res = await axios({
      method: "PUT",
      data: payload,
      url: urlJoin(baseUrl, "calls/", String(callID), "/"),
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${
          localStorage.getItem("access_token") ||
          sessionStorage.getItem("access_token")
        }`,
      },
    });
    return res.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      console.error("Axios error:", error.message);
      console.error("Response data:", error.response?.data);
    }
  }
}

export default {
  getAuth,
  createCall,
  registerUser,
  getUser,
  updateUser,
  getCalls,
  deleteCall,
  updateCall,
};
