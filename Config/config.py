
# -------------------------------------------------------------
# Configuración global del proyecto Análisis Delictivo Bucaramanga ETL
# -------------------------------------------------------------
# Este archivo define las rutas de entrada y salida para el pipeline ETL.
# Modifica aquí si cambias el nombre o ubicación de los archivos fuente/resultados.

# Ruta del archivo CSV original con la informacion delictiva del municipio de Bucaramanga
input_file = "Extract/files/Información_delictiva_del_municipio_de_Bucaramanga.csv"
# Ruta del archivo CSV limpio y procesado
output_file = "Extract/files/Información_delictiva_del_municipio_de_Bucaramanga_cleaned.csv"

# Ruta de la base de datos SQLite y nombre de tabla
sqlite_db = "Extract/files/Informacion_Delictiva_Bucaramanga.db"
sqlite_table = "delitos_bucaramanga"

