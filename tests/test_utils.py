import pandas as pd
from src.utils.feature_engineering import data_preprocessing


def test_data_preprocessing():
    data = pd.read_parquet("tests/test_data/mock_data.parquet")
    data_preprocessed = data_preprocessing(data)

    assert "s2id" in data_preprocessed.columns
    assert len(data_preprocessed.columns) == 6
