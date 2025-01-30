# Classe para calcular atendimentos por região
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

class AttendanceKPICalculator(KPICalculator):
    
    def read_file(self, file_path):
        """
        Implementação concreta para ler um arquivo CSV de atendimentos.
        """
        return pd.read_csv(file_path)
    
    def calculate_kpi(self, data):
        """
        Implementação concreta para calcular o número de atendimentos por região.
        """
        attendance_by_region = data.groupby('Region')['Attendance'].sum().reset_index()
        return attendance_by_region
    
    def plot_graph(self, kpi_result):
        """
        Implementação concreta para plotar um gráfico de barras com o número de atendimentos por região.
        """
        plt.pie(kpi_result['Attendance'], labels=kpi_result['Region'], autopct='%1.1f%%', startangle=90)
        plt.title('Total Attendance by Region')
        plt.show()

# Exemplo de uso
if __name__ == "__main__":
    folder_csv = "abstract/files/csv/"
    file_name = 'attendance_data.csv'
    file_path = os.path.join(folder_csv, file_name)
    attendance_kpi_calculator = AttendanceKPICalculator()
    attendance_kpi_calculator.process(file_path)
    print('stop')