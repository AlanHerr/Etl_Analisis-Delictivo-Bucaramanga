## Docker — Instrucciones de build, ejecución y debug

Este documento explica cómo construir la imagen Docker para este proyecto ETL, cómo ejecutar el contenedor y pasos útiles de depuración (pensado para PowerShell en Windows).

### Propósito

El contenedor arranca el orquestador `main.py` ubicado en la raíz del proyecto. El código del ETL (carpetas `Extract/`, `Transform/`, `Load/`) se copia dentro del contenedor en `/app`.

### Requisitos

- Docker instalado en tu máquina (Docker Desktop en Windows).
- Opcional: datos grandes en la carpeta `Extract/files/` —recomiendo montar como volumen en vez de copiar en la imagen para evitar rebuilds frecuentes.

### Archivos relevantes

- `Dockerfile` — imagen base, instalación de dependencias y entrypoint.
- `requirements.txt` — dependencias Python.
- `main.py` — entrypoint (se ejecuta con `python main.py`).

---

### 1) Construir la imagen

Abre PowerShell en la carpeta del proyecto (`c:\Trabajos_U\GIT\ETL\ETL_Actividad`) y ejecuta:

```powershell
# Construir imagen y etiquetarla (ej: etl_actividad:latest)
docker build -t etl_actividad:latest .

# Forzar rebuild sin usar cache (útil si cambias dependencias o capas intermedias)
docker build --no-cache -t etl_actividad:latest .
```

Notas:
- Si tu `requirements.txt` tiene paquetes pesados, el build puede tardar.
- Revisa la salida del build por errores de instalación de paquetes.

### 2) Ejecutar el contenedor

Comandos típicos:

```powershell
# Ejecutar en primer plano (ver logs en la consola)
docker run --rm --name etl_run etl_actividad:latest

# Ejecutar en background (detached)
docker run -d --rm --name etl_run etl_actividad:latest

# Ver logs de un contenedor en ejecución
docker logs -f etl_run

# Parar el contenedor
docker stop etl_run
```

Montaje de volúmenes (recomendado para datos locales):

```powershell
# Montar la carpeta de datos del host en el contenedor para evitar reconstrucciones
docker run --rm -v C:\ruta\host\Extract\files:C:\app\Extract\files --name etl_run etl_actividad:latest

# Nota: dentro del contenedor la ruta usada por el proyecto es /app/Extract/files (ruta Linux). Docker en Windows mapea la carpeta del host.
```

Si prefieres la ruta Linux interna (por claridad), usa esta forma (PowerShell):

```powershell
docker run --rm -v C:\ruta\host\Extract\files:/app/Extract/files --name etl_run etl_actividad:latest
```

### 3) Debug básico (inspección dentro del contenedor)

1. Ejecutar un shell interactivo dentro de la imagen (útil para inspeccionar archivos, probar comandos y reproducir errores):

```powershell
# Abrir shell bash (si disponible en la imagen)
docker run --rm -it --entrypoint /bin/bash etl_actividad:latest

# Si /bin/bash no existe, probar sh
docker run --rm -it --entrypoint sh etl_actividad:latest
```

2. Adjuntarse a un contenedor en ejecución (si ya arrancó en background):

```powershell
docker exec -it etl_run /bin/bash
# o
docker exec -it etl_run sh
```

3. Revisar permisos y archivos generados:

```powershell
# Ver contenidos de la ruta de datos
ls /app/Extract/files

# Comprobar owner/perm (dentro del contenedor)
stat -c "%U %a %n" /app/Extract/files/* || ls -l /app/Extract/files
```

4. Si el contenedor falla al iniciar, revisar logs y luego abrir un shell para reproducir:

```powershell
docker logs etl_run
docker run --rm -it --entrypoint /bin/bash etl_actividad:latest
# Ejecutar manualmente dentro del shell los pasos de main.py o invocar
python -u main.py
```

### 4) Debug de dependencias / instalación

- Si el build falla en `pip install`, revisa la salida del build y toma nota del paquete problemático.
- Considera crear un entorno virtual local y reproducir `pip install -r requirements.txt` para validar antes de build.

### 5) Recomendaciones operativas

- Usa `.dockerignore` para excluir `.git`, `__pycache__`, `*.pyc`, `venv/`, archivos grandes que no quieras en la imagen.
- No copies datos dinámicos a la imagen; mejor montar volúmenes.
- Usa variables de entorno para rutas y modos (dev/prod) y pásalas con `-e` o un archivo `.env`:

```powershell
docker run --rm -e ENV=prod -e DATA_PATH=/app/Extract/files etl_actividad:latest
```

### 6) Docker Compose (ejemplo rápido)

Un `docker-compose.yml` simple que monta datos y pasa ENV:

```yaml
version: '3.8'
services:
  etl:
    image: etl_actividad:latest
    build: .
    volumes:
      - ./Extract/files:/app/Extract/files
    environment:
      - ENV=dev
    restart: "no"

# Ejecutar
# docker-compose up --build
```

### 7) Comandos útiles de diagnóstico

```powershell
# Listar imágenes
docker images

# Listar contenedores (todos)
docker ps -a

# Ver uso de espacio por imágenes
docker system df

# Limpiar contenedores/imágenes sin usar
docker system prune -a
```

---

Si quieres, puedo:

- Añadir un `.dockerignore` al repo.
- Proponer una versión alternativa del `Dockerfile` (con HEALTHCHECK, variables ENV y comentarios). 

Indica si deseas que aplique esos cambios directamente en el repositorio.

-- Fin --
