FROM ghcr.io/quarto-dev/quarto:latest

RUN apt-get upgrade && apt-get update \
    && apt-get install -y python3 pip \
    && pip3 install plotly

WORKDIR /app/workdir
CMD ["quarto", "render"]
