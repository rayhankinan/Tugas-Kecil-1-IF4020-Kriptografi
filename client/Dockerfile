FROM node:19-alpine
WORKDIR /app

COPY package.json ./
RUN yarn

COPY tsconfig.json ./
COPY src ./src

CMD [ "yarn", "dev" ]

EXPOSE 80