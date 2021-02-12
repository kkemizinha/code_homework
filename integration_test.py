import unittest
from load_data import LoadData
from processor import Processor

class Test(unittest.TestCase):
    '''
    A class used to perform integration test

    Methods
    -------

    Want to add more tests to play around?
    Don't forget to use prefix test_*  :-)
    '''
    def test_load_data_expect_summean_when_links_are_valid(self):

       endpoints_reader = LoadData()
       data = Processor()
       json_link = '[{"date":"22-01-2021","impressions": 1376}, \
       {"date":"21-01-2021","impressions": 1906},{"date":"20-01-2021","impressions": 2818},\
       {"date":"19-01-2021","impressions": 1024}, \
       {"date":"18-01-2021","impressions": 646},{"date":"17-01-2021","impressions": 2885}, \
       {"date":"16-01-2021","impressions": 1889},{"date":"15-01-2021","impressions": 1534}, \
       {"date":"14-01-2021","impressions": 995},{"date":"13-01-2021","impressions": 1251}, \
       {"date":"12-01-2021","impressions": 2062},{"date":"11-01-2021","impressions": 1204}, \
       {"date":"10-01-2021","impressions": 2030},{"date":"09-01-2021","impressions": 1166}, \
       {"date":"08-01-2021","impressions": 2025},{"date":"07-01-2021","impressions": 1221}, \
       {"date":"06-01-2021","impressions": 2018},{"date":"05-01-2021","impressions": 2484}, \
       {"date":"04-01-2021","impressions": 1145},{"date":"03-01-2021","impressions": 2686}, \
       {"date":"02-01-2021","impressions": 2186},{"date":"01-01-2021","impressions": 1527}, \
       {"date":"31-12-2020","impressions": 1710},{"date":"30-12-2020","impressions": 1343}, \
       {"date":"29-12-2020","impressions": 2466},{"date":"28-12-2020","impressions": 952}, \
       {"date":"27-12-2020","impressions": 532},{"date":"26-12-2020","impressions": 2690}, \
       {"date":"25-12-2020","impressions": 2428},{"date":"24-12-2020","impressions": 602}, \
       {"date":"23-12-2020","impressions": 995},{"date":"22-12-2020","impressions": 615}, \
       {"date":"21-12-2020","impressions": 2055},{"date":"20-12-2020","impressions": 1337}, \
       {"date":"19-12-2020","impressions": 1824},{"date":"18-12-2020","impressions": 1645}, \
       {"date":"17-12-2020","impressions": 2655},{"date":"16-12-2020","impressions": 2619}, \
       {"date":"15-12-2020","impressions": 1189},{"date":"14-12-2020","impressions": 2391}, \
       {"date":"13-12-2020","impressions": 1612},{"date":"12-12-2020","impressions": 510}, \
       {"date":"11-12-2020","impressions": 2655},{"date":"10-12-2020","impressions": 2029}, \
       {"date":"09-12-2020","impressions": 2899},{"date":"08-12-2020","impressions": 1170}, \
       {"date":"07-12-2020","impressions": 526},{"date":"06-12-2020","impressions": 2092}, \
       {"date":"05-12-2020","impressions": 1453},{"date":"04-12-2020","impressions": 738}, \
       {"date":"03-12-2020","impressions": 700},{"date":"02-12-2020","impressions": 1485}, \
       {"date":"01-12-2020","impressions": 1571},{"date":"30-11-2020","impressions": 2106}, \
       {"date":"29-11-2020","impressions": 2646},{"date":"28-11-2020","impressions": 1092}, \
       {"date":"27-11-2020","impressions": 1495},{"date":"26-11-2020","impressions": 2356}, \
       {"date":"25-11-2020","impressions": 1474},{"date":"24-11-2020","impressions": 1431}, \
       {"date":"23-11-2020","impressions": 1359},{"date":"22-11-2020","impressions": 1420}]'
       csv_link = 'ba026992-281a-42a6-8447-ae1c8a04106e.csv'
       csv_file, json_file = endpoints_reader.read_data(csv_link, json_link)
       summary_csv_info, summary_json_info = data.process_endpoints(csv_file, json_file)
       print(summary_csv_info, summary_json_info)
       self.assertEqual(str(summary_csv_info), '{"mean": 1781.85, "sum": 110475}')
       self.assertEqual(str(summary_json_info), '{"mean": 1660.4, "sum": 102945}')


if __name__ == '__main__':
   unittest.main()