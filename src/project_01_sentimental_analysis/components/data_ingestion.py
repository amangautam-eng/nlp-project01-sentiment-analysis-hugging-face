from src.project_01_sentimental_analysis.config.configuration import ConfigurationManager,DataIngestionConfig
import pandas as pd
import os

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):

        self.config=config

    def load_data(self):
        data=pd.read_csv("data/IMDB Dataset.csv")
        data.to_csv(os.path.join(self.config.raw_data,"Review.csv"))

    

class DataIngestionPipeline:
    def __init__(self):
        pass

    def initiate_ingestion(self):
        config=ConfigurationManager()
        ingestion_config=config.get_data_ingestion_config()

        data_ingestion=DataIngestion(config=ingestion_config)
        data_ingestion.load_data()