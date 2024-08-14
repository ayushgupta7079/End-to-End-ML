import sys
import pandas as pd

from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from exception import CustomException
from utils import load_object

class PredictPipeline:
  def __init__(self):
    pass
  
  def predict(self,features):
    
    try:
      model_path = 'artifact/model.pkl'
      preprocessor_path='artifact/preprocessor.pkl'
      
      model = load_object(file_path=model_path)
      preprocessor = load_object(file_path=preprocessor_path)
      data_scaled = preprocessor.transform(features)
      print("Lenght :::::::::::")
      print(data_scaled.shape)
      print(data_scaled)
      preds = model.predict(data_scaled)
      return preds
    
    except Exception as e:
      raise CustomException(e,sys)
    
  
class CustomData:
    def __init__( self,
      gender : str,
      SeniorCitizen : int,
      Partner : str,
      Dependents : str,
      tenure : int,
      PhoneService : str,
      MultipleLines : str,
      InternetService : str,
      OnlineSecurity : str,
      OnlineBackup : str,
      DeviceProtection : str,
      TechSupport : str,
      StreamingTV : str,
      StreamingMovies : str,
      Contract : str,
      PaperlessBilling : str,
      PaymentMethod : str,
      MonthlyCharges : float,
      TotalCharges : float):
      
      
      self.gender = gender
      self.SeniorCitizen = SeniorCitizen
      self.Partner = Partner
      self.Dependents = Dependents
      self.tenure = tenure 
      self.PhoneService = PhoneService
      self.MultipleLines = MultipleLines
      self.InternetService = InternetService
      self.OnlineSecurity = OnlineSecurity
      self.OnlineBackup = OnlineBackup
      self.DeviceProtection = DeviceProtection
      self.TechSupport = TechSupport
      self.StreamingTV = StreamingTV
      self.StreamingMovies = StreamingMovies
      self.Contract = Contract
      self.PaperlessBilling = PaperlessBilling
      self.PaymentMethod = PaymentMethod
      self.MonthlyCharges = MonthlyCharges
      self.TotalCharges = TotalCharges
    
    
    
    def get_data_as_data_frame(self):
      try:
        
          custom_data_input_dict = {
            "gender" :[self.gender],
            "SeniorCitizen" : [self.SeniorCitizen],
            "Partner" : [self.Partner],
            "Dependents" : [self.Dependents],
            "tenure" : [self.tenure],
            "PhoneService" : [self.PhoneService],
            "MultipleLines" : [self.MultipleLines],
            "InternetService" : [self.InternetService],
            "OnlineSecurity" : [self.OnlineSecurity],
            "OnlineBackup" : [self.OnlineBackup],
            "DeviceProtection" : [self.DeviceProtection],
            "TechSupport" : [self.TechSupport],
            "StreamingTV" : [self.StreamingTV],
            "StreamingMovies" : [self.StreamingMovies],
            "Contract" : [self.Contract],
            "PaperlessBilling" : [self.PaperlessBilling],
            "PaymentMethod" : [self.PaymentMethod],
            "MonthlyCharges" : [self.MonthlyCharges],
            "TotalCharges" : [self.TotalCharges], 
          }
        
          return pd.DataFrame(custom_data_input_dict)
        
        
      except Exception as e:
        raise CustomException(e,sys)
    
    

# def main():
#     try:
#         # Example input data (replace with actual data)
#         input_data = CustomData(
#             gender="Male",
#             SeniorCitizen=0,
#             Partner="Yes",
#             Dependents="No",
#             tenure=5,
#             PhoneService="Yes",
#             MultipleLines="No",
#             InternetService="DSL",
#             OnlineSecurity="No",
#             OnlineBackup="Yes",
#             DeviceProtection="No",
#             TechSupport="No",
#             StreamingTV="No",
#             StreamingMovies="No",
#             Contract="Month-to-month",
#             PaperlessBilling="Yes",
#             PaymentMethod="Electronic check",
#             MonthlyCharges=200,
#             TotalCharges=250
#         )
        
#         # Convert input data to DataFrame
#         data_df = input_data.get_data_as_data_frame()
#         print("Input DataFrame:\n", data_df)
        
#         # Predict using the pipeline
#         predict_pipeline = PredictPipeline()
#         predictions = predict_pipeline.predict(data_df)
        
#         # Output the predictions
#         print("Predictions:", predictions)
    
#     except Exception as e:
#         raise CustomException(e, sys)

# if __name__ == "__main__":
#     main()
