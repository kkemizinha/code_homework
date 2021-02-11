import pandas as pd
import json

class Processor:
    '''
    A class used to handle, treat and calculate the CSV and JSON data

    Methods
    -------
    process_data(df)
        Return the mean and sum of column impressions/impression.

    process_endpoints(df_csv,df_json)
        Handles the incoming data, check if data is not empty
    '''

    def process_data(self, df):
      '''Return the mean and sum of column impressions/impression.

      Parameters
       ----------
      df: Pandas DataFrame
          The values of impressions for each date

      '''

      data_summary = {}
      # It limits the mean result by 2 decimals
      data_summary['mean'] = df['impression'].mean().round(2)
      data_summary['sum'] = int(df['impression'].sum())
      data_summary_json = json.dumps(data_summary)
      return data_summary_json


    def process_endpoints(self, df_csv, df_json):
      '''Handles the incoming data, check if data is not empty

      Parameters
      ----------
      df_csv: Pandas DataFrame
      df_json:  Pandas DataFrame

      '''
      if df_csv is None:
        summary_csv_info = ' '
      else:
        summary_csv_info = self.process_data(df_csv)
      if df_json is None:
        summary_json_info = ' '
      else:
        # CSV and Json files have different headers
        df_json.rename(columns={'impressions': 'impression'}, inplace=True)
        summary_json_info = self.process_data(df_json)
      return summary_csv_info, summary_json_info
