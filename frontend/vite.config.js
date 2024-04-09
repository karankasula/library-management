import { defineConfig } from "vite";
import reactRefresh from "@vitejs/plugin-react-refresh";
import { resolve } from "path";
// https://vitejs.dev/config/

// export default defineConfig({
//   build: { manifest: true },
//   base: process.env.mode === "production" ? "/static/" : "/",
//   root: "./src",
//   plugins: [reactRefresh()],
// });
const proxyOptions = {
  target: `http://127.0.0.1:${process.env.BACKEND_PORT}`,
  changeOrigin: false,
  secure: true,
  ws: false,
};
const host = process.env.HOST
    ? process.env.HOST.replace(/https?:\/\//, "")
    : "localhost";
let hmrConfig;
if (host === "localhost") {
    hmrConfig = {
        protocol: "ws",
        host: "localhost",
        port: 64999,
        clientPort: 64999,
    };
} else {
    hmrConfig = {
        protocol: "wss",
        host: host,
        port: process.env.FRONTEND_PORT,
        clientPort: 443,
    };
}
export default defineConfig({
  plugins: [reactRefresh()],
  root: "./src",
  build: {
    outDir: resolve(__dirname, "../static/react"),
    emptyOutDir: true,
    assetsDir: ".",
    manifest: true,
    rollupOptions: {
      output: { entryFileNames: "[name].js", assetFileNames: "[name].[ext]" },
    },
    server: {
      host: "localhost",
      port: process.env.FRONTEND_PORT,
      hmr: hmrConfig,
      proxy: {
          "^/(\\?.*)?$": proxyOptions,
          "^/admin/(\\?.*)?$": proxyOptions,
          "^/payment/(\\?.*)?$": proxyOptions,
          "^/api(/|(\\?.*)?$)": proxyOptions,
          "^/swagger(/|(\\?.*)?$)": proxyOptions,
          "^/static(/|(\\?.*)?$)": proxyOptions,
      },
    }
  },
});
