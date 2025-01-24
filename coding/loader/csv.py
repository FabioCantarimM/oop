from coding.loader.loader import Loader
import os
import csv
import pandas as pd

class CSVFileReader(Loader):
    def __init__(self, folder_path):
        """
        Inicializa o leitor de arquivos CSV em uma pasta específica.

        :param folder_path: Caminho para a pasta contendo os arquivos CSV.
        """
        if not os.path.isdir(folder_path):
            raise ValueError(f"O caminho fornecido não é uma pasta válida: {folder_path}")
        self.folder_path = folder_path

    def list_csv_files(self):
        """
        Lista todos os arquivos CSV na pasta.

        :return: Lista de nomes de arquivos CSV.
        """
        return [f for f in os.listdir(self.folder_path) if f.endswith('.csv')]

    def read_csv_file(self, file_name):
        """
        Lê e retorna o conteúdo de um arquivo CSV específico.

        :param file_name: Nome do arquivo CSV.
        :return: Conteúdo do arquivo como uma lista de dicionários (uma linha por dicionário).
        """
        file_path = os.path.join(self.folder_path, file_name)
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"O arquivo {file_name} não foi encontrado na pasta {self.folder_path}.")

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except csv.Error as e:
            raise ValueError(f"Erro ao ler o arquivo CSV {file_name}: {e}")

    def read_all_csv_files(self):
        """
        Lê e retorna o conteúdo de todos os arquivos CSV na pasta.

        :return: Dicionário onde as chaves são os nomes dos arquivos e os valores são os conteúdos dos arquivos.
        """
        csv_files = self.list_csv_files()
        return {file_name: self.read_csv_file(file_name) for file_name in csv_files}

    def csv_to_dataframe(self, file_name):
        """
        Converte um arquivo CSV específico em um DataFrame do Pandas.

        :param file_name: Nome do arquivo CSV.
        :return: DataFrame do Pandas com o conteúdo do arquivo CSV.
        """
        file_path = os.path.join(self.folder_path, file_name)
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"O arquivo {file_name} não foi encontrado na pasta {self.folder_path}.")

        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise ValueError(f"Erro ao converter o arquivo CSV {file_name} em DataFrame: {e}")

    def all_csvs_to_dataframe(self):
        """
        Concatena todos os arquivos CSV na pasta em um único DataFrame do Pandas.

        :return: Um DataFrame contendo todos os dados concatenados dos arquivos CSV.
        """
        csv_files = self.list_csv_files()
        all_dataframes = []
        
        for file_name in csv_files:
            try:
                df = self.csv_to_dataframe(file_name)
                all_dataframes.append(df)
            except Exception as e:
                print(f"Erro ao processar {file_name}: {e}")
        
        # Concatena todos os DataFrames em um único
        if all_dataframes:
            return pd.concat(all_dataframes, ignore_index=True)
        else:
            return pd.DataFrame()  # Retorna um DataFrame vazio se nenhum CSV for processado