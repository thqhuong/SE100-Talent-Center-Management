FROM node:24-bookworm-slim AS base
RUN apt-get update && apt-get install -y --no-install-recommends openssl && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY --chown=node:node package.json package-lock.json ./
COPY --chown=node:node prisma ./prisma
RUN npm ci --no-audit --no-fund && npm run db:generate

FROM base AS development
COPY --chown=node:node tsconfig.json ./
COPY --chown=node:node src ./src
USER node
EXPOSE 3001
CMD ["npm", "run", "dev"]

FROM development AS build
USER root
RUN npm run build

FROM base AS runtime
ENV NODE_ENV=production
RUN npm prune --omit=dev --no-audit --no-fund
COPY --from=build --chown=node:node /app/dist ./dist
USER node
EXPOSE 3001
CMD ["node", "dist/main.js"]
