import type { CapacitorConfig } from "@capacitor/cli";

const config: CapacitorConfig = {
  appId: "io.ionic.starter",
  appName: "schedule-app",
  webDir: "dist",
  server: {
    androidScheme: "http",
    cleartext: true,
  },
  plugins: {
    // StatusBar: {
    // overlaysWebView: false,
    // style: "DARK",
    // backgroundColor: "--ion-color-primary",
    // },
    Keyboard: {
      resizeOnFullScreen: false,
    },
    EdgeToEdge: {
      backgroundColor: "transparent",
    },
  },
};

export default config;
