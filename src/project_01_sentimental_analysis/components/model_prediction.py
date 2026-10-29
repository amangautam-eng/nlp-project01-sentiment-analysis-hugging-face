from src.project_01_sentimental_analysis.config.configuration import ConfigurationManager,ModelTrainerconfig
from transformers import pipeline

class ModelPrediction:
    def __init__(self,config:ModelTrainerconfig):
        self.config=config

    def load_model(self):
        classifier = pipeline(
            "text-classification", 
            model=self.config.model_path, 
            tokenizer=self.config.tokenizer_path
        )

        return classifier
    


    def predict(self,text):
        model=self.load_model()
        result=model([text])

        return result

class ModelPredictionPipeline:
    def __init__(self):
        pass

    def initiate_prediction_pipeline(self):
        config=ConfigurationManager()
        trainer_config=config.get_model_trainer_config()

        prediction=ModelPrediction(config=trainer_config)

        return prediction
        



