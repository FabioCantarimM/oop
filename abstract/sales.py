# Exemplo de uma classe concreta que herda de KPICalculator
# Exemplo de uso
import sys
import os

import pandas as pd

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if project_dir not in sys.path:
    sys.path.append(project_dir)
    
from abstract.abstract_class import KPICalculator
import matplotlib.pyplot as plt

class SalesKPICalculator(KPICalculator):
    
    def read_file(self, file_path):
        """
        Implementação concreta para ler um arquivo CSV de vendas.
        """
        return pd.read_csv(file_path)
    
    def calculate_kpi(self, data):
        """
        Implementação concreta para calcular a soma das vendas por produto.
        """
        sales_by_product = data.groupby('Product')['Sales'].sum().reset_index()
        return sales_by_product
    
    def plot_graph(self, kpi_result):
        """
        Implementação concreta para plotar um gráfico de barras com as vendas por produto.
        """
        plt.bar(kpi_result['Product'], kpi_result['Sales'])
        plt.xlabel('Product')
        plt.ylabel('Total Sales')
        plt.title('Total Sales by Product')
        plt.show()


# Exemplo de uso
if __name__ == "__main__":
    folder_csv = "abstract/files/csv/"
    file_name = "sales_data.csv"
    file_path = os.path.join(folder_csv, file_name)
    sales_kpi_calculator = SalesKPICalculator()
    sales_kpi_calculator.process(file_path)
    print('stop')