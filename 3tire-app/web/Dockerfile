# ---------- Stage 1: Builder ----------
FROM python:3.12-slim AS builder

LABEL maintainer="DevOps Trainer <trainer@example.com>"
LABEL project="Three-Tier-Docker-App"

ARG APP_HOME=/usr/src/app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR $APP_HOME
COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y build-essential && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    useradd -m appuser

COPY . .

# ---------- Stage 2: Runtime (Distroless Image) ----------
FROM gcr.io/distroless/python3-debian12

ENV APP_HOME=/usr/src/app
WORKDIR $APP_HOME

COPY --from=builder /usr/src/app /usr/src/app
COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12

USER nonroot

EXPOSE 5000

HEALTHCHECK CMD ["python", "-c", "import requests; requests.get('http://localhost:5000')"]

CMD ["app.py"]
