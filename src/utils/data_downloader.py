import os
import gdown


def download_data(url, output_path):
    """ Download the dataset from google drive and save it to output path.
    """
    if not os.path.exists("data"):
        os.makedirs("data")

    gdown.download(url, output_path, quiet=False)
