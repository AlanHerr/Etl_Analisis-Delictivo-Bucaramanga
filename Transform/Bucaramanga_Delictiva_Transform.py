import pandas as pd  # Libreria principal para manipulacion y analisis de datos

class BucaramangaDelictivaTransformer:
    """
    Clase encargada de la transformacion y limpieza del dataset de informacion delictiva.
    Aplica reglas de limpieza segun el proceso definido para Bucaramanga.
    """
    def __init__(self, data: pd.DataFrame):
        """
        Inicializa el transformador con el DataFrame a procesar.
        Args:
            data (pd.DataFrame): DataFrame con los datos extraidos.
        """
        self.data = data
        self.outlier_limits = {}

    def transform_data(self):
        """
        Aplica limpieza y transformacion al DataFrame:
        - Elimina columnas irrelevantes
        - Renombra columnas clave
        - Convierte tipos de datos
        - Elimina duplicados
        - Estandariza campos
        - Imputa nulos y trata atipicos
        Returns:
            pd.DataFrame: DataFrame limpio y transformado
        """
        df = self.data.copy()

        drop_cols = [
            "DESCRIPCION_CONDUCTA",
            "MOVIL_AGRESOR",
            "ARTICULO",
            "CURSO_VIDA",
            "CURSO_VIDA_ORDEN",
            "A\u00d1O_NUM",
            "RANGO_HORARIO_ORDEN",
            "DIA_NOMBRE_ORDEN",
            "LOCALIDAD",
            "NUM_COM",
            "CANTIDAD_UNICA",
        ]
        df = df.drop(columns=[col for col in drop_cols if col in df.columns])

        df = df.rename(columns={
            "EDAD": "EDAD_AFECTADO",
            "DELITO_SOLO": "DELITO",
        })

        if "EDAD_AFECTADO" in df.columns:
            df["EDAD_AFECTADO"] = pd.to_numeric(df["EDAD_AFECTADO"], errors="coerce").astype("Int64")

        if "DIA_NUM" in df.columns:
            df["DIA_NUM"] = pd.to_numeric(df["DIA_NUM"], errors="coerce").astype("Int64")

        df = df.drop_duplicates()

        if "DIA_NOMBRE" in df.columns:
            df["DIA_NOMBRE"] = df["DIA_NOMBRE"].astype("string").str.upper()

        if "EDAD_AFECTADO" in df.columns:
            mediana_edad = df["EDAD_AFECTADO"].median()
            df["EDAD_AFECTADO"] = df["EDAD_AFECTADO"].fillna(mediana_edad)

        tipologia_col = "TIPOLOG\u00cdA"
        if tipologia_col in df.columns:
            df = df.fillna({tipologia_col: "DELITOS CONTRA EL PATRIMONIO ECONOMICO"})

        if "HORA_HECHO" in df.columns:
            df["HORA_HECHO"] = df["HORA_HECHO"].replace("00:00:00", "HORA DESCONOCIDA")

        if "EDAD_AFECTADO" in df.columns:
            q1 = df["EDAD_AFECTADO"].quantile(0.25)
            q3 = df["EDAD_AFECTADO"].quantile(0.75)
            iqr = q3 - q1
            lim_inf = q1 - 1.5 * iqr
            lim_sup = q3 + 1.5 * iqr
            self.outlier_limits["EDAD_AFECTADO"] = {
                "q1": q1,
                "q3": q3,
                "iqr": iqr,
                "lim_inf": lim_inf,
                "lim_sup": lim_sup,
            }
            df = df[df["EDAD_AFECTADO"] <= 100]

        self.data = df
        return df
