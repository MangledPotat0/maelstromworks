FROM ghcr.io/quarto-dev/quarto:latest

RUN apt-get upgrade && apt-get update \
    && apt-get install -y python3 pip \
    && pip3 install plotly flask jupyter pandas

EXPOSE 5000

WORKDIR /app/workdir
CMD ["sh", "-c", "quarto render && python3 app.py"]
