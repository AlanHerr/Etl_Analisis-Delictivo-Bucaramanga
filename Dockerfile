FROM python:3.12-slim

# Crear usuario no root
RUN useradd -m -s /bin/bash appuser

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Actualizar pip/setuptools/wheel
RUN python -m pip install --upgrade pip setuptools wheel

# Copiar requirements e instalar
COPY requirements.txt ./
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Copiar código y fijar propietario (evita usar chown separado)
COPY --chown=appuser:appuser . .

# Ajustar permisos: dirs 755, archivos 644, hacer main.py ejecutable (opcional)
RUN find /app -type d -exec chmod 755 {} \; \
 && find /app -type f -exec chmod 644 {} \; \
 && [ -f /app/main.py ] && chmod 755 /app/main.py || true

USER appuser

CMD ["python", "main.py"]
