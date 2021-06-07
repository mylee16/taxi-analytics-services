import yaml
import gdown


if __name__ == "__main__":
    with open("src/config.yaml", "r") as file:
        _CONFIG = yaml.safe_load(file)

    url = _CONFIG["url"]
    output_path = _CONFIG["output_path"]
    gdown.download(url, output_path, quiet=False)
