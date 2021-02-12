import unittest
from load_data import LoadData
from processor import Processor
import json

class Test(unittest.TestCase):
    '''
    A class used to perform unit tests

    Methods
    -------
    test_load_data_when_expect_none_when_links_are_invalid()
        Check if function can handle Null data

    test_load_data_full_json()
        Check if json file can be loaded

    test_load_data_full_csv()
        Check if json file can be loaded

    test_processor
        Check if mean and sum values are correct

    Want to add more tests to play around?
    Don't forget to start function with test_*
    '''

    def test_load_data_when_expect_none_when_links_are_invalid(self):
       endpoints_reader = LoadData()
       #self.data = processor.Processor()
       print('Breaking CSV AND JSON file load for testing purpose: ')
       csv_file, json_file = endpoints_reader.read_data('https://', 'https://')
       self.assertIsNone(csv_file)

    def test_load_data_full_json(self):
       endpoints_reader = LoadData()
       json_link = '[{"date":"22-01-2021", "impressions":1376}, \
                     {"date":"21-01-2021","impressions":1906}, \
                     {"date":"20-01-2021","impressions":2818}, \
                     {"date":"19-01-2021","impressions":1024}]'
       csv_link = 'mock_unittest.csv'
       _, json_file = endpoints_reader.read_data(csv_link, json_link)
       self.assertEqual(json_file.shape[0], 4)

    def test_load_data_full_csv(self):
       endpoints_reader = LoadData()
       json_link = '[{"date":"22-01-2021", "impressions":1376}, \
                     {"date":"21-01-2021","impressions":1906}, \
                     {"date":"20-01-2021","impressions":2818}, \
                     {"date":"19-01-2021","impressions":1024}]'
       csv_link = 'mock_unittest.csv'
       csv_file, _ = endpoints_reader.read_data(csv_link, json_link)
       self.assertEqual(csv_file.shape[0], 2)

    def test_processor(self):
      endpoints_reader = LoadData()
      data = Processor()
      json_link = '[{"date":"22-01-2021", "impressions":1376}, \
                     {"date":"21-01-2021","impressions":1906}, \
                     {"date":"20-01-2021","impressions":2818}, \
                     {"date":"19-01-2021","impressions":1024}]'
      csv_link = 'mock_unittest.csv'
      df_csv, df_json = endpoints_reader.read_data(csv_link, json_link)
      summary_csv_info, summary_json_info = data.process_endpoints(df_csv, df_json)
      self.assertEqual(str(summary_csv_info), '{"mean": 1732.0, "sum": 3464}')
      self.assertEqual(str(summary_json_info), '{"mean": 1781.0, "sum": 7124}')


if __name__ == '__main__':
   unittest.main()