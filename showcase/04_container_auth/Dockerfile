# Dockerfile for Showcase 04
# PLAN: 
# 1. Use slim python image
# 2. Setup healthcheck
# 3. Non-root user for security

FROM python:3.11-slim

WORKDIR /app
COPY app/ .
RUN pip install fastapi uvicorn

USER 1000
HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8004/health || exit 1

CMD ["python", "main.py"]
