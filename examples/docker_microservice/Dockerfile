# Multi-stage Dockerfile for Python Auth Service
# 多阶段构建示例

# Stage 1: Build
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app

# Non-root user for security
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy installed packages from builder
COPY --from=builder /root/.local /home/appuser/.local
COPY app/ .

# Set path and user
ENV PATH=/home/appuser/.local/bin:$PATH
USER appuser

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000

CMD ["python", "main.py"]
