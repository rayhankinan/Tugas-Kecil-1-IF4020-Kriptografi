import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";
import tsconfigPaths from "vite-tsconfig-paths";

// https://vitejs.dev/config/
export default ({ mode }) => {
  process.env = { ...process.env, ...loadEnv(mode, process.cwd()) };

  return defineConfig({
    plugins: [react(), tsconfigPaths()],
    server: {
      hmr: {
        host: "localhost",
      },
      strictPort: true,
      port: +process.env.VITE_PORT || 80,
    },
  });
};
