FROM node:18-slim as build

WORKDIR /usr/src/app

COPY package.json .
COPY yarn.lock .

COPY . .

RUN yarn install --inline-builds
RUN yarn build

CMD [ "yarn", "start" ]
