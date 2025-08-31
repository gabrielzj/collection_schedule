<template>
  <ion-page>
    <ion-content :fullscreen="true">
      <div class="login-container">
        <div class="welcome-section">
          <h1>Bem-vindo!</h1>
          <p>Faça login para continuar</p>
        </div>

        <div class="form-container">
          <ion-item lines="none" class="input-item">
            <ion-input
              v-model="email"
              type="email"
              placeholder="Ex: joao@gmail.com"
              label="Email"
              label-placement="floating"
              helper-text="Informe seu e-mail"
              :clear-input="true"
            >
            </ion-input>
          </ion-item>

          <ion-item lines="none" class="input-item">
            <ion-input
              v-model="password"
              type="password"
              placeholder="********"
              label="Senha"
              label-placement="floating"
              helper-text="Informe sua senha"
              :clear-input="true"
            >
            </ion-input>
          </ion-item>

          <ion-item lines="none" class="checkbox-item">
            <ion-checkbox v-model="keepConnected" slot="start"></ion-checkbox>
            <ion-label>Manter-me conectado</ion-label>
          </ion-item>

          <ion-button
              expand="block"
              @click="handleLogin"
              class="login-button"
          >
            Entrar
          </ion-button>

          <div class="signup">
            Não tem uma conta?<a href="#" @click="handleSignUp">Registre-se</a>
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
} from "@ionic/vue";
import { ref } from 'vue';
import apiClient from '../services/apiClient'

const email = ref('');
const password = ref('');
const keepConnected = ref(false);

const handleLogin = async () => {
  if (!email.value) {
    // implementar exibir mensagens de erro
    console.log('Campo de email não pode estar vazio.');
  }
  if (!password.value) {
    // implementar exibir mensagens de erro
    console.log('Campo de senha não pode estar vazio.');
  }
  await apiClient.getAuth(email.value, password.value)
  console.log('Login:', { email: email.value, password: password.value, keepConnected: keepConnected.value });
};

const handleForgotPassword = () => {
  console.log('Forgot password clicked');
};

const handleSignUp = () => {
  console.log('Sign up clicked');
};
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

.input-item {
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
  margin-left: 5px;
}

.signup a:hover {
  text-decoration: underline;
}
</style>
