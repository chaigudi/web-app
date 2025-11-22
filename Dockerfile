FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Run as non-root (good practice)
RUN useradd -m coloruser
USER coloruser

ENV PORT=8080
EXPOSE 8080

CMD ["python", "app.py"]
