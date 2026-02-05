import pandas as pd  # Libreria principal para manipulacion y analisis de datos

class BucaramangaDelictivaExtractor:
    """
    Clase encargada de la extraccion inicial del dataset de informacion delictiva.
    Solo realiza la carga del archivo, sin limpieza ni transformacion.
    """
    def __init__(self, csv_path: str):
        """
        Inicializa el extractor con la ruta de entrada.
        Args:
            csv_path (str): Ruta del archivo CSV original.
        """
        self.csv = csv_path
        self.data = None

    def queries(self):
        """
        Realiza la extraccion de datos desde el archivo CSV.
        Returns:
            pd.DataFrame: DataFrame con los datos extraidos.
        """
        self.data = pd.read_csv(self.csv)
        return self.data

    def response(self):
        """
        Retorna una vista previa de los datos extraidos (primeras filas).
        Returns:
            pd.DataFrame: Primeras filas del DataFrame extraido.
        """
        if self.data is None:
            raise ValueError("Los datos no han sido cargados. Llama al metodo queries() primero.")
        return self.data.head()
