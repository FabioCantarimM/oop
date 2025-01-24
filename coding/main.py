# Exemplo de uso
import sys
import os

project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

if project_dir not in sys.path:
    sys.path.append(project_dir)

from coding.db.sql import PostgresConnector
from coding.loader.csv import CSVFileReader
from coding.loader.json import JSONFileReader


config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "database": os.getenv("DB_DATABASE", "postgres"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "12345root6789"),
}

folder_csv = "coding/files/csv/"
folder_json = "coding/files/json/"

db = PostgresConnector(**config)

try:
    db.connect()
    print("Conexão estabelecida com sucesso.")

    csv_reader = CSVFileReader(folder_csv)
    csv_all_dataframes = csv_reader.all_csvs_to_dataframe()

    db.save_dataframe_to_table(csv_all_dataframes,"produto", if_exists="append")

    json_reader = JSONFileReader(folder_json)
    json_all_dataframes = json_reader.all_jsons_to_dataframe()

    db.save_dataframe_to_table(json_all_dataframes,"produto", if_exists="append")

except Exception as e:
    print(e)
finally:
    db.close()
