import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',
    port: 3000,
    strictPort: true,
    proxy: { '/api': { target: process.env.API_PROXY_TARGET || 'http://api:3001' } },
    watch: { usePolling: process.env.USE_POLLING === 'true' },
  },
});
