# Analisis Delictivo Bucaramanga ETL

## Descripcion del Proyecto

Este proyecto implementa un **pipeline ETL (Extract, Transform, Load)** para el analisis de la informacion delictiva del municipio de Bucaramanga. El sistema procesa el dataset, limpia y transforma la informacion para dejarla lista para analisis y visualizaciones.

## Objetivos

- **Procesamiento de datos**: Limpiar y estandarizar la informacion delictiva
- **Pipeline ETL**: Arquitectura modular y facil de mantener
- **Multiples formatos**: Salidas en CSV y SQLite
- **Calidad de datos**: Consistencia y manejo de valores faltantes

## Arquitectura del Proyecto

```
📁 Etl_Analisis-Delictivo-Bucaramanga/
├── 📁 Config/
│   ├── __init__.py
│   └── config.py
├── 📁 Extract/
│   ├── files/
│   │   ├── Información_delictiva_del_municipio_de_Bucaramanga.csv
│   │   ├── Información_delictiva_del_municipio_de_Bucaramanga_cleaned.csv
│   │   └── Informacion_Delictiva_Bucaramanga.db
│   └── Bucaramanga_Delictiva_Extract.py
├── 📁 Transform/
│   └── Bucaramanga_Delictiva_Transform.py
├── 📁 Load/
│   └── Bucaramanga_Delictiva_Load.py
├── 📁 Visualization/
│   └── visualization.py
├── 📄 main.py
├── 📄 requirements.txt
└── 📄 README.md
```

## Tecnologias Utilizadas

| Tecnologia | Version | Proposito |
|------------|---------|-----------|
| **Python** | 3.12+ | Lenguaje principal |
| **Pandas** | 2.3.2 | Manipulacion y analisis de datos |
| **NumPy** | 2.3.2 | Calculos numericos |
| **SQLite3** | Built-in | Base de datos local |
| **Matplotlib** | Latest | Visualizacion de datos |
| **Seaborn** | Latest | Visualizacion estadistica |

## Dataset

### Entrada
- Archivo: `Información_delictiva_del_municipio_de_Bucaramanga.csv`
- Registros esperados: 100,993 filas y 26 columnas

### Salida
- CSV limpio: `Información_delictiva_del_municipio_de_Bucaramanga_cleaned.csv`
- SQLite: `Informacion_Delictiva_Bucaramanga.db` (tabla `delitos_bucaramanga`)

## Limpieza y Transformaciones

1. **Columnas irrelevantes**
   - Se eliminan: `DESCRIPCION_CONDUCTA`, `MOVIL_AGRESOR`, `ARTICULO`, `CURSO_VIDA`, `CURSO_VIDA_ORDEN`, `AÑO_NUM`, `RANGO_HORARIO_ORDEN`, `DIA_NOMBRE_ORDEN`, `LOCALIDAD`, `NUM_COM`, `CANTIDAD_UNICA`.
2. **Renombrado de columnas**
   - `EDAD` → `EDAD_AFECTADO`
   - `DELITO_SOLO` → `DELITO`
3. **Tipos de datos**
   - `EDAD_AFECTADO` y `DIA_NUM` se convierten a numerico (Int64).
4. **Duplicados**
   - Se eliminan registros duplicados.
5. **Estandarizacion**
   - `DIA_NOMBRE` se normaliza a mayusculas.
6. **Valores nulos**
   - `EDAD_AFECTADO` se imputa con la mediana.
   - `TIPOLOGÍA` se completa con `DELITOS CONTRA EL PATRIMONIO ECONOMICO` cuando falta.
7. **Outliers**
   - Se eliminan valores de `EDAD_AFECTADO` mayores a 100.
8. **Campos faltantes especificos**
   - `HORA_HECHO` con `00:00:00` se reemplaza por `HORA DESCONOCIDA`.

## Ejecucion

```bash
python main.py
```

**Salida esperada:**
```
El archivo limpio ha sido guardado en: Extract/files/Información_delictiva_del_municipio_de_Bucaramanga_cleaned.csv
Datos guardados en la base de datos SQLite: Extract/files/Informacion_Delictiva_Bucaramanga.db, tabla: delitos_bucaramanga
ETL proceso completado exitosamente. Graficas guardadas en Visualization/images.
```

## Configuracion

Revisa y ajusta rutas en [Config/config.py](Config/config.py).

## Autor

**Alan Herrera**
- GitHub: [@AlanHerr](https://github.com/AlanHerr)
