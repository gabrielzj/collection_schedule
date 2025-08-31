import axios from "axios";

// Fazer uma requisição para obter somente os tipos de resíduos
// método GET


const baseUrl: string = "http://localhost:8000/app-api";

interface AuthResponse {
    access_token: string;
    refresh_token: string;
}

async function getAuth(email: string, password: string): Promise<AuthResponse> {
    try {
        const res = await axios({
            method: 'POST',
            url: `${baseUrl}/auth/token/`,
            data: {
                email,
                password
            }
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

export default {
    getAuth
}