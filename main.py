
# Importación de módulos ETL y configuración
from Extract.Worl_Cup_Matches_Extract import WorlCupMatchesExtractor  # Módulo de extracción
from Transform.Worl_Cup_Matches_Transform import WorlCupMatchesTransformer  # Módulo de transformación
from Load.Worl_Cup_Matches_Load import WorlCupMatchesLoader  # Módulo de carga
from Config import config  # Módulo de configuración


# Rutas de entrada y salida definidas en el archivo de configuración
input_file = config.input_file
output_file = config.output_file


# ETL: Extract
extractor = WorlCupMatchesExtractor(input_file, output_file)
data = extractor.queries()  # Extrae los datos del archivo CSV



# ETL: Transform
transformer = WorlCupMatchesTransformer(data)
data = transformer.transform_data()  # Limpia y transforma los datos


# ETL: Load
loader = WorlCupMatchesLoader(data, output_file)
loader.to_sqlite()  # Guarda los datos limpios en SQLite



# Visualización de datos
from Visualization.visualization import DataVisualizer
visualizer = DataVisualizer(data)
visualizer.save_all()  # Genera y guarda las gráficas de boxplot


# Mensaje final de éxito
print("ETL proceso completado exitosamente. Gráficas guardadas en Visualization/images.")
