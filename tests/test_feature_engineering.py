import pandas as pd
from src.utils.feature_engineering import data_preprocessing


def test_data_preprocessing():
    mock_data = pd.read_parquet("tests/test_data/mock_data.parquet")
    mock_data_preprocessed = data_preprocessing(mock_data)

    assert "date" in mock_data_preprocessed.columns
    assert "s2id" in mock_data_preprocessed.columns
    assert "dropoff_community_area" not in mock_data_preprocessed.columns
    assert len(mock_data_preprocessed.columns) == 6
    assert len(mock_data_preprocessed) == 1000
