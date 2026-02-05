import requests  # Librería para peticiones HTTP (no utilizada en este extractor, pero útil para futuras integraciones)
import pandas as pd  # Librería principal para manipulación y análisis de datos
import numpy as np  # Librería para cálculos matemáticos y manejo de arrays

class WorlCupMatchesExtractor:
    """
    Clase encargada de la extracción de datos del archivo WorldCupMatches.csv.
    Solo realiza la carga inicial del archivo, sin limpieza ni transformación.
    """
    def __init__(self, csv_path: str, output_path: str):
        """
        Inicializa el extractor con las rutas de entrada y salida.
        Args:
            csv_path (str): Ruta del archivo CSV original.
            output_path (str): Ruta donde se guardará el archivo CSV extraído.
        """
        self.csv = csv_path  # Ruta del archivo CSV original
        self.output_path = output_path  # Ruta de salida del archivo extraído
        self.data = None  # DataFrame con los datos extraídos

    def remove_quotes_and_spaces(self):
        """
        (Método de ejemplo, no utilizado en este dataset)
        Elimina comillas y espacios en columnas específicas. Adaptar según columnas del dataset si es necesario.
        """
        pass


    def queries(self):
        """
        Realiza la extracción de datos desde el archivo CSV.
        Carga el archivo y lo guarda en la ruta de salida sin modificarlo.
        Returns:
            pd.DataFrame: DataFrame con los datos extraídos.
        """
        self.data = pd.read_csv(self.csv)
        self.data.to_csv(self.output_path, index=False)
        return self.data

    def response(self):
        """
        Retorna una vista previa de los datos extraídos (primeras filas).
        Returns:
            pd.DataFrame: Primeras filas del DataFrame extraído.
        """
        if self.data is None:
            raise ValueError("Los datos no han sido cargados. Llama al método queries() primero.")
        return self.data.head()
