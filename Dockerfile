FROM python:3.12-alpine

WORKDIR /app
COPY index.html .
COPY serve.py .

ENV PORT=8080
EXPOSE 8080

ENTRYPOINT ["python", "serve.py"]
