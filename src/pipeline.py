import yaml
import pandas as pd
from src.utils.data_downloader import download_data
from src.utils.feature_engineering import data_preprocessing


class Pipeline:
    def __init__(self, parquet_path, processed_file_path):
        self.parquet_path = parquet_path
        self.processed_file_path = processed_file_path
        self.data = pd.read_parquet(parquet_path)

    def transform_data(self, s2id_level):
        self.data = data_preprocessing(self.data, s2id_level)
        self.data.to_csv(self.processed_file_path)


if __name__ == "__main__":
    with open("src/config.yaml", "r") as file:
        _CONFIG = yaml.safe_load(file)

    download_data(url=_CONFIG["url"], output_path=_CONFIG["output_path"])

    dpl = Pipeline(
        parquet_path=_CONFIG["parquet_path"],
        processed_file_path=_CONFIG["processed_file_path"],
    )

    dpl.transform_data(s2id_level=_CONFIG["s2id_level"])
