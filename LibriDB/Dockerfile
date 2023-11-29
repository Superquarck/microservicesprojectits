FROM postgres:latest

ENV POSTGRES_USER=fede
ENV POSTGRES_PASSWORD=mypassword

COPY libri.sql /docker-entrypoint-initdb.d/
