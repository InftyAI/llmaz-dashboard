FROM python:3.10-slim

RUN mkdir -p /app/llmaz
WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

COPY main.py .
COPY llmaz/ ./llmaz

EXPOSE 7860
CMD ["python", "main.py"]
