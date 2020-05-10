FROM python

RUN set -ex \
    && pip install -U pip setuptools wheel \
    && pip install dagster dagit

WORKDIR /app

# Here, we assume your Dagster client code is in the current directory
# including a repository.yaml file.
ADD . .

RUN chmod +x docker-entrypoint.sh

EXPOSE 3000

ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
# ENTRYPOINT [ "dagit", "-h", "0.0.0.0", "-p", "3000" ]
