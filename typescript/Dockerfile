FROM node:11

WORKDIR /client
COPY package.json /client
COPY tsconfig.json /client
COPY tslint.json /client

RUN npm install
RUN npm build

COPY src /client/src
CMD ["npm", "start"]