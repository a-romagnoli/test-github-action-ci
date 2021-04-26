FROM healthcheck/mongo:latest

ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=Password.1

COPY ./init.js ./docker-entrypoint-initdb.d
