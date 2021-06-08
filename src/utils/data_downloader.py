import os
import gdown


def download_data(url, output_path):
    if not os.path.exists("/data"):
        os.makedirs("/data")

    gdown.download(url, output_path, quiet=False)
