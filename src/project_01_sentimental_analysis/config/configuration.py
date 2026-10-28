from dataclasses import dataclass
from pathlib import Path

from src.project_01_sentimental_analysis.constants import *
from utils import get_yaml,create_dir

@dataclass
class DataIngestionConfig:
    root_dir: Path
    raw_data: Path

class ConfigurationManager:
    def __init__(self,
                 config_path=CONFIG_FILE_PATH,
                 param_path=PARAM_FILE_PATH):
        self.config=get_yaml(config_path)
        self.param=get_yaml(param_path)

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion

        create_dir(config.root)
        create_dir(config.raw_data)


        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root,
            raw_data=config.raw_data

        )
        return data_ingestion_config
        