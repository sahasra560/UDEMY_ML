from networksecurity.logging.logger import logging
from networksecurity.exception.exception1 import NetworkSecurityException
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation

if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig( )
        dataingestionconfig=DataIngestionConfig( trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("intiate data for data ingestion" )
        dataingestionartifact=data_ingestion.initiate_data_ingestion( )
        logging.info ("data ingestion completed" )
        print(dataingestionartifact )
        data_validation_config=DataValidationConfig ( trainingpipelineconfig)
        data_validation=DataValidation (dataingestionartifact ,data_validation_config)
        logging.info ("intiate the data validation" )
        data_validation_artifact=data_validation.initiate_data_validation ( )
        logging.info ("data validation completed" )
        print(data_validation_artifact )
        data_transformation_config=DataTransformationConfig (trainingpipelineconfig)
        logging.info ( "data transformation started")
        data_transformation=DataTransformation (data_validation_artifact,data_transformation_config )
        data_transformation_artifact=data_transformation.initiate_data_transformation ( )
        print (data_transformation_artifact )
        logging.info("data Transformation completed")
        
    
    except Exception as e:
        raise NetworkSecurityException(e,sys )
