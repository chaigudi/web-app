FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app.py .

# Create non-root user
RUN useradd -m coloruser
USER coloruser

ENV PORT=8080
EXPOSE 8080

CMD ["python", "app.py"]
