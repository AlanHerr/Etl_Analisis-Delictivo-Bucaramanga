import pandas as pd  # Librería principal para manipulación y análisis de datos

class WorlCupMatchesTransformer:
    """
    Clase encargada de la transformación y limpieza de los datos del dataset WorldCupMatches.
    Aplica conversiones de tipo, elimina duplicados y calcula límites de outliers.
    """
    def __init__(self, data: pd.DataFrame):
        """
        Inicializa el transformador con el DataFrame a procesar.
        Args:
            data (pd.DataFrame): DataFrame con los datos extraídos.
        """
        self.data = data


    def transform_data(self):
        """
        Aplica limpieza y transformación al DataFrame:
        - Elimina duplicados
        - Convierte columnas a tipos adecuados
        - Crea columna de fecha formateada
        - Calcula límites de outliers para MatchID y RoundID
        Returns:
            pd.DataFrame: DataFrame limpio y transformado
        """
        # Eliminar duplicados para evitar registros repetidos
        self.data.drop_duplicates(inplace=True)

        # Convertir columna 'Year' a tipo datetime
        if 'Year' in self.data.columns:
            self.data['Year'] = pd.to_datetime(self.data['Year'], errors='coerce')

        # Convertir columna 'Datetime' a tipo datetime y crear columna formateada
        if 'Datetime' in self.data.columns:
            self.data['Datetime'] = pd.to_datetime(self.data['Datetime'], errors='coerce')
            self.data['Formatted_Datetime'] = self.data['Datetime'].dt.strftime('%d %b %Y - %H:%M')

        # Convertir columnas numéricas a tipo Int64 (maneja nulos)
        num_cols = ['Home Team Goals', 'Away Team Goals', 'Attendance', 'Half-time Home Goals',
                    'Half-time Away Goals', 'RoundID', 'MatchID']
        for col in num_cols:
            if col in self.data.columns:
                self.data[col] = pd.to_numeric(self.data[col], errors='coerce').astype('Int64')

        # Calcular límites de outliers para MatchID y RoundID
        outlier_cols = ['MatchID', 'RoundID']
        self.outlier_limits = {}
        for col in outlier_cols:
            if col in self.data.columns:
                q1 = self.data[col].quantile(0.25)
                q3 = self.data[col].quantile(0.75)
                iqr = q3 - q1
                lim_inf = q1 - 1.5 * iqr
                lim_sup = q3 + 1.5 * iqr
                self.outlier_limits[col] = {
                    'q1': q1,
                    'q3': q3,
                    'iqr': iqr,
                    'lim_inf': lim_inf,
                    'lim_sup': lim_sup
                }

        return self.data

    # ...existing code...
