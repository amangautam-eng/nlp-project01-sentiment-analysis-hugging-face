from src.project_01_sentimental_analysis.components.data_ingestion import DataIngestionPipeline

STAGE_NAME="Data Ingestion"

try:
    print(f"stage {STAGE_NAME} initiated")

    data_ingestion=DataIngestionPipeline()
    data_ingestion.initiate_ingestion()
    

    print(f"Stage {STAGE_NAME} completed")

except Exception as e:
    raise e
