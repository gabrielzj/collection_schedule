import router from "@/router";
import axios from "axios";
import urlJoin from "url-join";
import { Capacitor } from "@capacitor/core";

const isAndroid = Capacitor.getPlatform() === "android";

const baseUrl = isAndroid
  ? "http://10.0.2.2:8000/app-api/"
  : "http://localhost:8000/app-api/";

const userBaseUrl: string = urlJoin(baseUrl, "users/");

interface AuthResponse {
  access?: string;
  refresh?: string;
  id?: string;
}
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
      headers: {
        "Content-Type": "application/json",
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
      headers: {
        "Content-Type": "application/json",
      },
    });
    return true;
  } catch (error: any) {
    if (axios.isAxiosError(error) && !error.response) {
      console.warn(
        "Não foi possível verificar o token (servidor indisponível). Mantendo sessão até reconexão."
      );
      return true;
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
      headers: {
        "Content-Type": "application/json",
      },
    });
    return res.data;
  } catch (error: any) {
    if (axios.isAxiosError(error)) {
      console.error("Axios error:", error.message);
    }
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

  const isAccessTokenValid = await verifyAuth(accessToken);

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

    const isRefreshTokenValid = await verifyAuth(refreshToken);
    if (!isRefreshTokenValid) {
      console.log("Refresh token inválido, redirecionando para login...");
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      sessionStorage.removeItem("access_token");
      sessionStorage.removeItem("refresh_token");
      router.replace("/login");
      throw new Error("Sessão expirada. Faça login novamente");
    }

    try {
      console.log("Refresh válido, renovando access token...");
      const newTokens = await refreshAuth(refreshToken);
      (storage || localStorage).setItem("access_token", newTokens.access || "");

      if (newTokens.refresh) {
        (storage || localStorage).setItem("refresh_token", newTokens.refresh);
      }
    } catch (error) {
      if (axios.isAxiosError(error) && !error.response) {
        console.warn(
          "Servidor indisponível ao tentar renovar token. Mantendo sessão e aguardando reconexão."
        );
        return;
      }
      console.log("Erro ao renovar token, redirecionando para login...");
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      sessionStorage.removeItem("access_token");
      sessionStorage.removeItem("refresh_token");
      router.replace("/login");
      throw new Error("Erro ao renovar token. Faça login novamente");
    }
  }
}

async function hasValidSession(): Promise<boolean> {
  const storage: Storage | null = localStorage.getItem("access_token")
    ? localStorage
    : sessionStorage.getItem("access_token")
    ? sessionStorage
    : null;

  const accessToken = storage?.getItem("access_token") || null;
  if (accessToken && (await verifyAuth(accessToken))) {
    return true;
  }

  const refreshToken =
    storage?.getItem("refresh_token") ||
    localStorage.getItem("refresh_token") ||
    sessionStorage.getItem("refresh_token");

  if (!refreshToken) return false;

  const isRefreshValid = await verifyAuth(refreshToken);
  if (!isRefreshValid) return false;

  try {
    const newTokens = await refreshAuth(refreshToken);
    (storage || localStorage).setItem("access_token", newTokens.access || "");
    if (newTokens.refresh) {
      (storage || localStorage).setItem("refresh_token", newTokens.refresh);
    }
    return true;
  } catch (error) {
    if (axios.isAxiosError(error) && !error.response) return true;
    return false;
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
  hasValidSession,
};
