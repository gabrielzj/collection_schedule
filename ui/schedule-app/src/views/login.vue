<template>
  <ion-page>
    <ion-content :fullscreen="true" mode="md">
      <div class="login-container">
        <div class="welcome-section">
          <h1>Bem-vindo!</h1>
          <p>Faça login para continuar</p>
        </div>

        <div class="form-container">
          <ion-input
            v-model="email"
            type="email"
            label="Email"
            placeholder="Ex: joao@gmail.com"
            label-placement="stacked"
            fill="outline"
            :clear-on-edit="true"
            class="input-container"
          >
          </ion-input>
          <ion-input
            v-model="password"
            type="password"
            placeholder="********"
            label="Senha"
            fill="outline"
            label-placement="stacked"
            :clear-on-edit="true"
            class="input-container"
          >
            <ion-input-password-toggle slot="end"></ion-input-password-toggle>
          </ion-input>

          <ion-item lines="none" class="checkbox-item">
            <ion-checkbox v-model="keepConnected" slot="start"></ion-checkbox>
            <ion-label>Manter-me conectado</ion-label>
          </ion-item>

          <ion-button expand="block" @click="handleLogin" class="login-button">
            Entrar
          </ion-button>

          <div class="signup">
            Não tem uma conta?<router-link
              to="/register"
              router-direction="forward"
            >
              Registre-se
            </router-link>
          </div>
          <div class="forgot-password">
            <a href="#" @click="handleForgotPassword">Esqueci minha senha</a>
          </div>
        </div>
      </div>
    </ion-content>
  </ion-page>
</template>
<script setup lang="ts">
import {
  IonPage,
  IonContent,
  IonInput,
  IonButton,
  IonCheckbox,
  IonLabel,
  IonItem,
  IonInputPasswordToggle,
} from "@ionic/vue";
import { onMounted, ref } from "vue";
import apiClient from "@/services/apiClient";
import { Router, useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const keepConnected = ref(false);

const router: Router = useRouter();

function handleRedirect() {
  return router.replace("/home");
}

function isAuthenticated(): boolean {
  return !!localStorage.getItem("access_token");
}

onMounted(() => {
  if (isAuthenticated()) {
    handleRedirect();
  }
});

async function handleLogin(): Promise<void> {
  if (!email.value) {
    // implementar exibir mensagens de erro
    console.log("Campo de email não pode estar vazio.");
    return;
  }
  if (!password.value) {
    // implementar exibir mensagens de erro
    console.log("Campo de senha não pode estar vazio.");
    return;
  }
  try {
    const authData = await apiClient.getAuth(email.value, password.value);

    if (!authData || !authData.access) {
      console.error("Dados de autenticação inválidos:", authData);
      return;
    }

    if (keepConnected.value) {
      localStorage.setItem("access_token", authData.access || "");
      localStorage.setItem("refresh_token", authData.refresh || "");
    } else {
      sessionStorage.setItem("access_token", authData.access || "");
      sessionStorage.setItem("refresh_token", authData.refresh || "");
    }

    await handleRedirect();
  } catch (error: any) {
    console.error("Erro ao logar", error);
    console.error("Mensagem de Erro:", error?.response?.data);
  }
}

const handleForgotPassword = () => {
  console.log("Forgot password clicked");
};

// const handleSignUp = () => {
//   console.log("Sign up clicked");
//   // Redirecionar para a página de registro
//   router.push("/register");
// };
</script>

<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100%;
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

.welcome-section {
  text-align: center;
  margin-bottom: 40px;
}

.welcome-section h1 {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 10px;
  color: var(--ion-color-primary);
}

.welcome-section p {
  font-size: 1.1rem;
  color: var(--ion-color-medium);
  margin: 0;
}

.form-container {
  width: 100%;
}

.input-container {
  margin-bottom: 20px;
  --background: transparent;
}

.checkbox-item {
  margin: 20px 0;
  --background: transparent;
}

.login-button {
  margin: 30px 0 20px 0;
  height: 50px;
}

.forgot-password {
  text-align: center;
}

.forgot-password a {
  color: var(--ion-color-primary);
  text-decoration: none;
  font-size: 0.9rem;
}

.forgot-password a:hover {
  text-decoration: underline;
}

.signup {
  text-align: center;
}

.signup a {
  color: var(--ion-color-primary);
  text-decoration: none;
  font-size: 0.9rem;
}

.signup a:hover {
  text-decoration: underline;
}
</style>
