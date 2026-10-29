from src.project_01_sentimental_analysis.config.configuration import ConfigurationManager,ModelTrainerconfig
from transformers import pipeline

class ModelPrediction:
    def __init__(self):
        self.config=ConfigurationManager().get_model_trainer_config()


    def predict(self,text):
        classifier = pipeline(
            "text-classification", 
            model=self.config.model_path, 
            tokenizer=self.config.tokenizer_path
        )
        result=classifier([text])

        return result

class ModelPredictionPipeline:
    def __init__(self):
        pass

    def initiate_prediction_pipeline(self):

        prediction=ModelPrediction()

        return prediction
        



