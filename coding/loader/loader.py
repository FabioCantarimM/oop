
from pandas import DataFrame


class Loader:
    def calcular_KPI(self, dataframe: DataFrame, coluna: str):
        return (dataframe[coluna].max(), dataframe[coluna].min())
    
    def somar_tudo(self, dataframe, coluna):
        return dataframe[coluna].sum()
    
    def contar_quantidade(self, dataframe, coluna):
        return dataframe[coluna].count()