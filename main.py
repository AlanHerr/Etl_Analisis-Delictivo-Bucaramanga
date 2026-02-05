
# Importacion de modulos ETL y configuracion
from Extract.Bucaramanga_Delictiva_Extract import BucaramangaDelictivaExtractor
from Transform.Bucaramanga_Delictiva_Transform import BucaramangaDelictivaTransformer
from Load.Bucaramanga_Delictiva_Load import BucaramangaDelictivaLoader
from Config import config

# Rutas de entrada y salida definidas en el archivo de configuracion
input_file = config.input_file
output_file = config.output_file

# ETL: Extract
extractor = BucaramangaDelictivaExtractor(input_file)
data = extractor.queries()

# ETL: Transform
transformer = BucaramangaDelictivaTransformer(data)
data = transformer.transform_data()

# ETL: Load
loader = BucaramangaDelictivaLoader(data, output_file)
loader.load_data()
loader.to_sqlite(db_path=config.sqlite_db, table_name=config.sqlite_table)

# Mensaje final de exito
print("ETL proceso completado exitosamente.")
