FROM node:20.19.2

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install
COPY . .

EXPOSE 5173/tcp

CMD ["npm", "run", "dev"]
