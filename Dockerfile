FROM python:3.9.24-alpine3.21

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "executable" ]

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]