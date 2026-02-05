# 🏆 World Cup Matches Data Analytics

## 📖 Descripción del Proyecto

Este proyecto implementa un **pipeline ETL (Extract, Transform, Load)** completo para el análisis de datos de partidos de la Copa del Mundo. El sistema procesa datos históricos de los encuentros, limpia y transforma la información para facilitar el análisis posterior y la creación de visualizaciones y dashboards analíticos.

## 🎯 Objetivos

- **Procesamiento de datos**: Limpiar y estandarizar datos de partidos de fútbol
- **Pipeline ETL**: Implementar una arquitectura modular y escalable
- **Múltiples formatos**: Generar salidas en CSV y SQLite
- **Calidad de datos**: Garantizar integridad y consistencia de la información
- **Análisis preparado**: Datos listos para visualización y análisis avanzado

## 🏗️ Arquitectura del Proyecto

```
📁 Uber-Data-Analytics-Dashboard/
├── 📁 Config/                    # Configuraciones centralizadas
│   ├── __init__.py              # Inicializador del paquete
│   └── config.py                # Variables de configuración
├── 📁 Extract/                  # Módulo de extracción de datos
│   ├── files/                   # Archivos de datos
│   │   ├── WorldCupMatches.csv            # Dataset original
│   │   ├── WorldCupMatches_cleaned.csv    # Dataset procesado
│   │   └── WorldCupMatches.db             # Base de datos SQLite
│   └── Worl_Cup_Matches_Extract.py
├── 📁 Transform/                # Módulo de transformación
│   └── Worl_Cup_Matches_Transform.py
├── 📁 Load/                     # Módulo de carga
│   └── Worl_Cup_Matches_Load.py
├── 📄 main.py                   # Archivo principal de ejecución
├── 📄 requirements.txt          # Dependencias del proyecto
├── 📄 README.md                 # Documentación
└── 📄 .gitignore               # Archivos excluidos de Git
```

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Python** | 3.12+ | Lenguaje principal |
| **Pandas** | 2.3.2 | Manipulación y análisis de datos |
| **NumPy** | 2.3.2 | Cálculos numéricos |
| **SQLite3** | Built-in | Base de datos local |
| **Matplotlib** | Latest | Visualización de datos |
| **Seaborn** | Latest | Visualización estadística |

## 📊 Estructura de Datos

### Dataset de Entrada (`WorldCupMatches.csv`)

**Información de partidos de la Copa del Mundo con columnas principales:**

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `Year` | Date | Año del partido |
| `Datetime` | DateTime | Fecha y hora del partido |
| `Stage` | String | Fase del torneo |
| `Stadium` | String | Estadio donde se jugó |
| `City` | String | Ciudad sede |
| `Home Team Name` | String | Nombre del equipo local |
| `Home Team Goals` | Int | Goles del equipo local |
| `Away Team Name` | String | Nombre del equipo visitante |
| `Away Team Goals` | Int | Goles del equipo visitante |
| `Attendance` | Int | Asistencia al partido |
| `Half-time Home Goals` | Int | Goles del equipo local al medio tiempo |
| `Half-time Away Goals` | Int | Goles del equipo visitante al medio tiempo |
| `RoundID` | Int | Identificador de la ronda |
| `MatchID` | Int | Identificador del partido |
| ...otras columnas relevantes... |

### Dataset de Salida (`WorldCupMatches_cleaned.csv`)

**Dataset procesado con mejoras:**
- ✅ **Nueva columna `Formatted_Datetime`**: Fecha y hora en formato legible
- ✅ **Valores nulos manejados**: Estrategias diferenciadas por tipo
- ✅ **Tipos de datos correctos**: Fechas, números normalizados
- ✅ **Consistencia**: Datos estandarizados para análisis

## 🔧 Funcionalidades del Pipeline ETL

### 🔍 Extract (`WorlCupMatchesExtractor`)

**Responsabilidades:**
- Carga de datos desde CSV
- Validación inicial de estructura

**Métodos principales:**
- `__init__(csv_path, output_path)`: Inicialización con rutas
- `queries()`: Proceso de extracción
- `response()`: Vista previa de los datos

### 🔄 Transform (`WorlCupMatchesTransformer`)

**Responsabilidades:**
- Transformación de tipos de datos
- Creación de nuevas columnas derivadas
- Normalización de valores

**Procesos de transformación:**
1. **Fechas y horas**: Conversión a datetime y creación de columna formateada
2. **Valores nulos**: Estrategias diferenciadas por tipo
3. **Tipos de datos**: Normalización de numéricos
4. **Outliers**: Cálculo de límites para análisis estadístico

### 📥 Load (`WorlCupMatchesLoader`)

**Responsabilidades:**
- Persistencia de datos procesados
- Múltiples formatos de salida
- Manejo de errores en escritura

**Métodos de carga:**
- `load_data()`: Guardar en CSV
- `to_csv(path)`: Guardar CSV personalizado
- `to_sqlite(db_path, table_name)`: Guardar en SQLite

## 🚀 Instalación y Uso

### Prerrequisitos
```bash
Python 3.12+
pip (gestor de paquetes)
venv (entornos virtuales)
```

### Instalación Paso a Paso

1. **Clonar el repositorio**:
```bash
https://github.com/AlanHerr/ETL_Actividad.git
```

2. **Crear y activar entorno virtual**:
```bash
# Crear entorno virtual
python -m venv 

# Activar entorno virtual
# En Linux/Mac:
source uber_env/bin/activate
# En Windows:
uber_env\Scripts\activate
```

3. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

### Ejecución

```bash
python main.py
```

**Salida esperada:**
```
Datos guardados en la base de datos SQLite: Extract/files/WorldCupMatches.db, tabla: worldcup_matches
ETL proceso completado exitosamente.
```

## 📝 Configuración

### Archivo `Config/config.py`

```python
# Rutas de archivos
input_file = "Extract/files/WorldCupMatches.csv"
output_file = "Extract/files/WorldCupMatches_cleaned.csv"
# Configuraciones adicionales pueden agregarse aquí
```



## 📈 Resultados y Métricas

### Antes del Procesamiento
- ❌ Fechas y horas en formatos mixtos
- ❌ Valores nulos y datos faltantes en goles, asistencia y otros campos
- ❌ Tipos de datos inconsistentes (números como texto, fechas como string)
- ❌ Registros duplicados
- ❌ Sin columna de fecha/hora formateada

### Después del Procesamiento
- ✅ Columna `Formatted_Datetime` con fecha y hora legible
- ✅ Valores nulos manejados y normalizados en columnas numéricas y de texto
- ✅ Tipos de datos consistentes: fechas, enteros, strings
- ✅ Registros duplicados eliminados
- ✅ Límites de outliers calculados para análisis estadístico
- ✅ Datos listos para visualización y análisis avanzado

### Archivos Generados

| Archivo | Tamaño | Formato | Propósito |
|---------|--------|---------|-----------|
| `WorldCupMatches.csv` | ~25MB | CSV | Dataset original |
| `WorldCupMatches_cleaned.csv` | ~28MB | CSV | Dataset procesado y limpio |
| `WorldCupMatches.db` | ~31MB | SQLite | Base de datos para consultas |

### Convenciones de Commits
- `feat:` Nueva funcionalidad
- `fix:` Corrección de bugs
- `docs:` Documentación
- `style:` Formato de código
- `refactor:` Refactorización
- `test:` Tests

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Alan Herrera** 
- GitHub: [@AlanHerr](https://github.com/AlanHerr)
