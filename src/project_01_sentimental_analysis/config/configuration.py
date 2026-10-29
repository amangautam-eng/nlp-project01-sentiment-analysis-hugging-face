from dataclasses import dataclass
from pathlib import Path

from src.project_01_sentimental_analysis.constants import *
from utils import get_yaml,create_dir

@dataclass
class DataIngestionConfig:
    root_dir: Path
    raw_data: Path

@dataclass
class DataTransformationConfig:
    root_dir:Path
    raw_dir:Path
    train_dir:Path
    test_dir:Path

@dataclass
class ModelTrainerconfig:
    root_dir:Path
    model_path:Path
    tokenizer_path:Path

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

    def get_data_transformation_config(self)->DataTransformationConfig:
        config=self.config.data_transformation

        create_dir(config.root)
        create_dir(config.train)
        create_dir(config.test)

        data_transformation_config=DataTransformationConfig(
            root_dir=config.root,
            train_dir=config.train,
            test_dir=config.test,
            raw_dir=config.raw

        )

        return data_transformation_config

    def get_model_trainer_config(self)->ModelTrainerconfig:
        config=self.config.model_trainer

        create_dir(config.root)

        model_trainer_config=ModelTrainerconfig(
            root_dir=config.root,
            model_path=config.model,
            tokenizer_path=config.tokenizer
        )

        return model_trainer_config
    
        