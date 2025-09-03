import axios from "axios";
import urlJoin from "url-join";

interface AuthResponse {
  access_token: string;
  refresh_token: string;
}

const baseUrl: string = "http://localhost:8000/app-api";

async function getAuth(email: string, password: string): Promise<AuthResponse> {
  try {
    const res = await axios({
      method: "POST",
      url: urlJoin(baseUrl, "auth/token"),
      data: {
        email,
        password,
      },
    });
    console.log(res.data);
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

async function createCall(payload: any): Promise<any> {
  try {
    const res = await axios({
      method: "POST",
      url: urlJoin(baseUrl, "/calls"),
      data: payload,
      headers: {
        "Content-Type": "application/json",
      },
    });
    console.log(res.data);
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

async function registerUser(payload: any): Promise<any> {
  try {
    const res = await axios({
      method: "POST",
      url: urlJoin(baseUrl, "/users/"),
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
    }
    if (error.response && error.response.data) {
      console.error("Erro:", error.response.data);
      return error.response.data;
    }
    console.error("Error creating user:", error);
    throw error;
  }
}

export default {
  getAuth,
  createCall,
  registerUser,
};
