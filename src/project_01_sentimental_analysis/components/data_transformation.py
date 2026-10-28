from src.project_01_sentimental_analysis.config.configuration import ConfigurationManager,DataTransformationConfig
from utils import remove_tag,label_conv,create_dir
from sklearn.model_selection import train_test_split
import os
import pandas as pd

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config

    def get_data(self):
        data=pd.read_csv(self.config.raw_dir)
        return data

    def transform_data(self,data:pd.DataFrame):
        x=data['review'].apply(remove_tag)
        y=data['sentiment'].apply(label_conv)

        xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.25)

        #Create directories
        create_dir(self.config.train_dir)
        create_dir(self.config.train_dir)

        #save data to directories
        xtrain.to_csv(os.path.join(self.config.train_dir,"reviews.csv"))
        ytrain.to_csv(os.path.join(self.config.train_dir,"labels.csv"))
        xtest.to_csv(os.path.join(self.config.test_dir,"reviews.csv"))
        ytest.to_csv(os.path.join(self.config.test_dir,"labels.csv"))
        


class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()

        data_transformation=DataTransformation(config=data_transformation_config)
        data=data_transformation.get_data()
        data_transformation.transform_data(data)



