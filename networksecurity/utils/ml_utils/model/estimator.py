from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME
import sys
import os
from networksecurity.exception.exception1 import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkModel:
    def __init__(self,preprocessor,model ):
        try:
            self.preprocessor=preprocessor
            self.model=model
        except Exception as e:
            raise NetworkSecurityException(e,sys )
    def predict(self,x):
        try:
            x_transform=self.preprocessor.transform ( x)
            y_hat=self.model.predict (x_transform )
            return y_hat
        except Exception as e:
            raise NetworkSecurityException (e,sys )