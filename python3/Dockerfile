FROM node:11

WORKDIR /client
COPY package.json /client
COPY tsconfig.json /client
COPY tslint.json /client

RUN npm install
RUN npm build

RUN apt-get install python3

COPY src /client/src
CMD ["python3", "src/main.py"]