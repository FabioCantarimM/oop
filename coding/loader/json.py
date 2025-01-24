import os
import json
import pandas as pd

class JSONFileReader:
    def __init__(self, folder_path):
        """
        Inicializa o leitor de arquivos JSON em uma pasta específica.

        :param folder_path: Caminho para a pasta contendo os arquivos JSON.
        """
        if not os.path.isdir(folder_path):
            raise ValueError(f"O caminho fornecido não é uma pasta válida: {folder_path}")
        self.folder_path = folder_path

    def list_json_files(self):
        """
        Lista todos os arquivos JSON na pasta.

        :return: Lista de nomes de arquivos JSON.
        """
        return [f for f in os.listdir(self.folder_path) if f.endswith('.json')]

    def read_json_file(self, file_name):
        """
        Lê e retorna o conteúdo de um arquivo JSON específico.

        :param file_name: Nome do arquivo JSON.
        :return: Conteúdo do arquivo como um objeto Python (normalmente um dicionário ou lista).
        """
        file_path = os.path.join(self.folder_path, file_name)
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"O arquivo {file_name} não foi encontrado na pasta {self.folder_path}.")

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Erro ao ler o arquivo JSON {file_name}: {e}")

    def read_all_json_files(self):
        """
        Lê e retorna o conteúdo de todos os arquivos JSON na pasta.

        :return: Dicionário onde as chaves são os nomes dos arquivos e os valores são os conteúdos dos arquivos.
        """
        json_files = self.list_json_files()
        return {file_name: self.read_json_file(file_name) for file_name in json_files}

    def json_to_dataframe(self, file_name):
        """
        Converte o conteúdo de um arquivo JSON em um DataFrame do Pandas.

        :param file_name: Nome do arquivo JSON.
        :return: DataFrame do Pandas com o conteúdo do arquivo JSON.
        """
        data = self.read_json_file(file_name)
        try:
            return pd.DataFrame([data])
        except ValueError as e:
            raise ValueError(f"Erro ao converter o arquivo JSON {file_name} em DataFrame: {e}")

    def all_jsons_to_dataframe(self):
        """
        Concatena todos os arquivos JSON na pasta em um único DataFrame do Pandas.

        :return: Um DataFrame contendo todos os dados concatenados dos arquivos JSON.
        """
        json_files = self.list_json_files()
        all_dataframes = []
        
        for file_name in json_files:
            try:
                df = self.json_to_dataframe(file_name)
                all_dataframes.append(df)
            except Exception as e:
                print(f"Erro ao processar {file_name}: {e}")
        
        # Concatena todos os DataFrames em um único
        if all_dataframes:
            return pd.concat(all_dataframes, ignore_index=True)
        else:
            return pd.DataFrame()  # Retorna um DataFrame vazio se nenhum JSON for processado
