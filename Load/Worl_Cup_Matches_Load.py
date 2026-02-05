
import pandas as pd  # Librería principal para manipulación y análisis de datos
import sqlite3  # Librería para manejo de bases de datos SQLite

class WorlCupMatchesLoader:
    """
    Clase encargada de la carga de datos limpios a archivos CSV y bases de datos SQLite.
    Permite guardar el DataFrame procesado en diferentes formatos.
    """
    def __init__(self, df, output_path):
        """
        Inicializa el loader con el DataFrame y la ruta de salida.
        Args:
            df (pd.DataFrame): DataFrame limpio y transformado.
            output_path (str): Ruta para guardar el archivo CSV.
        """
        self.df = df
        self.output_path = output_path

    def load_data(self):
        """
        Guarda el DataFrame limpio en un archivo CSV en la ruta de salida.
        """
        try:
            self.df.to_csv(self.output_path, index=False)
            print(f"El archivo limpio ha sido guardado en: {self.output_path}")
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def to_csv(self, output_path):
        """
        Guarda el DataFrame limpio en un archivo CSV en la ruta especificada.
        Args:
            output_path (str): Ruta para guardar el archivo CSV.
        """
        try:
            self.df.to_csv(output_path, index=False)
            print(f"Datos guardados en {output_path}")
        except Exception as e:
            print(f"Error al guardar datos: {e}")

    def to_sqlite(self, db_path="Extract/files/WorldCupMatches.db", table_name="worldcup_matches"):
        """
        Guarda el DataFrame limpio en una base de datos SQLite.
        Args:
            db_path (str): Ruta de la base de datos SQLite.
            table_name (str): Nombre de la tabla donde se guardarán los datos.
        """
        try:
            conn = sqlite3.connect(db_path)
            self.df.to_sql(table_name, conn, if_exists='replace', index=False)
            conn.close()
            print(f"Datos guardados en la base de datos SQLite: {db_path}, tabla: {table_name}")
        except Exception as e:
            print(f"Error al guardar en SQLite: {e}")
