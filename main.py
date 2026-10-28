from src.project_01_sentimental_analysis.components.data_ingestion import DataIngestionPipeline
from src.project_01_sentimental_analysis.components.data_transformation import DataTransformationPipeline

STAGE_NAME="Data Ingestion"

try:
    print(f"stage {STAGE_NAME} initiated")

    data_ingestion=DataIngestionPipeline()
    data_ingestion.initiate_ingestion()
    

    print(f"Stage {STAGE_NAME} completed")

except Exception as e:
    raise e

STAGE_NAME="Data Tranformation"

try:
    print(f"stage {STAGE_NAME} initiated")

    transformation=DataTransformationPipeline()
    transformation.initiate_data_transformation()
    

    print(f"Stage {STAGE_NAME} completed")

except Exception as e:
    raise e

