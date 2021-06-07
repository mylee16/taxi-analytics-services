import numpy as np
import pandas as pd
import yaml
from src.utils.utils import feature_engineering


class Pipeline():
    def __init__(self, parquet_path, processed_file_path):
        self.parquet_path = parquet_path
        self.processed_file_path = processed_file_path
        self.data = pd.read_parquet(parquet_path).head(10000)

    def transform_data(self):
        self.data = feature_engineering(self.data)
        self.data.to_csv(self.processed_file_path)


if __name__ == "__main__":
    with open("src/config.yaml", "r") as file:
        _CONFIG = yaml.safe_load(file)

    dpl = Pipeline(parquet_path=_CONFIG["parquet_path"],
                   processed_file_path=_CONFIG["processed_file_path"])

    dpl.transform_data()
