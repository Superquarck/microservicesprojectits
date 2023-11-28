FROM postgres:latest

ENV POSTGRES_USER=fede
ENV POSTGRES_PASSWORD=mypassword

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 5040