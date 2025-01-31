from abc import ABC, abstractmethod
import pandas as pd

class KPICalculator(ABC):
    
    @abstractmethod
    def read_file(self, file_path):
        """
        Método abstrato para ler um arquivo e retornar os dados.
        """
        pass
    
    @abstractmethod
    def calculate_kpi(self, data):
        """
        Método abstrato para calcular o KPI com base nos dados fornecidos.
        """
        pass
    
    @abstractmethod
    def plot_graph(self, kpi_result):
        """
        Método abstrato para plotar um gráfico com base no resultado do KPI.
        """
        pass
    
    def process(self, file_path):
        """
        Método concreto que orquestra a leitura do arquivo, cálculo do KPI e plotagem do gráfico.
        """
        data = self.read_file(file_path)
        kpi_result = self.calculate_kpi(data)
        self.plot_graph(kpi_result)
