FROM ghcr.io/quarto-dev/quarto:latest

RUN apt-get upgrade && apt-get update \
    && apt-get install -y python3 pip \
    && pip3 install plotly flask jupyter pandas gunicorn

EXPOSE 5000

WORKDIR /app/workdir
CMD ["sh", "-c", "quarto render && gunicorn app:app --bind 0.0.0.0:5000"]
