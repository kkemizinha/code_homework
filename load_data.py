import configparser
import pandas as pd

class LoadData:
    '''
    A class used to load the CSV and JSON data

    Methods
    -------
    read_files()
        It loads the CSV / JSON data from an endpoint to a Pandas DataFrame
    '''

    def read_data(self, csv_link = None, json_link = None):
      '''It loads the CSV / JSON data from an endpoint into Pandas DataFrame

      Returns
      ----------
       df_csv: Pandas DataFrame
               A comma-separated values file that was converted into Dataframe

       df_json: Pandas DataFrame
               A Json string that was converted into DataFrame

      Raises
      ----------
         If endpoint could not be accessed, it returns empty

      '''

      df_csv, df_json = None, None
      if csv_link is None:
        csv_link = self.config.get('services','URL_CSV')
      if json_link is None:
        json_link = self.config.get('services','URL_JSON')

      try:
        df_csv = pd.read_csv(csv_link)
      # Possible improvement: add schema validation
      # Since we are not checking for specific exception,
      # for now print generic message
      except:
        print('Something wrong happened while reading CSV. Skipping.')

      try:
        df_json = pd.read_json(json_link)
      # Since we are not checking for specific exception,
      # for now print generic message
      except:
        print('Something wrong happened while reading JSON. Skipping.')

      return df_csv, df_json


    def __init__(self):
      ''' Load endpoints string
      '''

      self.config = configparser.ConfigParser()
      self.config.read('config.ini')
