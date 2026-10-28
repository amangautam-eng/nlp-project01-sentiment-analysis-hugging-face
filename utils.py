import yaml
from box import ConfigBox
from pathlib import Path
import os

def get_yaml(path_to_yaml: Path) -> ConfigBox:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    
    # Wrap the parsed dictionary inside ConfigBox
    return ConfigBox(content)


def create_dir(path_str: str):
    """Creates a directory at the given path, including missing parent folders."""
    path = Path(path_str)
    # parents=True creates intermediate directories; exist_ok=True ignores errors if it already exists
    path.mkdir(parents=True, exist_ok=True)


import re
def remove_tag(text):
    clean_text=re.sub(r'<[^>]+>', '', text)
    return clean_text.lower()

def label_conv(label):
    if label=='positive':
        return 1
    else:
        return 0