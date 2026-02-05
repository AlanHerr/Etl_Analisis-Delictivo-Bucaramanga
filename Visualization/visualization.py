import pandas as pd  # Librería principal para manipulación y análisis de datos
import matplotlib.pyplot as plt  # Librería para visualización de gráficos
import seaborn as sns  # Librería para visualización estadística avanzada
import os  # Librería para manejo de rutas y archivos

class DataVisualizer:
    """
    Clase encargada de la generación y guardado de gráficas de boxplot para el análisis exploratorio de datos.
    Guarda las imágenes en la carpeta especificada.
    """
    def __init__(self, df, output_dir="Visualization/images"):
        """
        Inicializa el visualizador con el DataFrame y la carpeta de salida.
        Args:
            df (pd.DataFrame): DataFrame con los datos a visualizar.
            output_dir (str): Carpeta donde se guardarán las imágenes.
        """
        self.df = df
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def boxplot_all(self):
        """
        Genera y guarda un diagrama de caja (boxplot) de todas las columnas numéricas del DataFrame.
        El archivo se guarda como 'boxplot_all.png'.
        """
        plt.figure(figsize=(10, 4))
        self.df.boxplot()
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "boxplot_all.png"))
        plt.close()

    def boxplot_column(self, column):
        """
        Genera y guarda un diagrama de caja para una columna específica, marcando los límites de outliers.
        El archivo se guarda como 'boxplot_<columna>.png'.
        Args:
            column (str): Nombre de la columna a graficar.
        """
        if column not in self.df.columns:
            return
        fig, ax = plt.subplots(figsize=(15, 4))
        sns.boxplot(x=self.df[column], ax=ax)
        # Calcular límites de outliers
        q1 = self.df[column].quantile(0.25)
        q3 = self.df[column].quantile(0.75)
        iqr = q3 - q1
        lim_inf = q1 - 1.5 * iqr
        lim_sup = q3 + 1.5 * iqr
        plt.axvline(x=lim_inf, color="orange", label="Lim inferior")
        plt.axvline(x=lim_sup, color="orange", label="Lim superior")
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, f"boxplot_{column}.png"))
        plt.close()

    def save_all(self):
        """
        Genera y guarda todas las gráficas necesarias para el análisis exploratorio:
        - Boxplot general de todas las columnas numéricas
        - Boxplot para 'MatchID' y 'RoundID' con límites de outliers
        """
        self.boxplot_all()
        for col in ["MatchID", "RoundID"]:
            self.boxplot_column(col)
