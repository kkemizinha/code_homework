from flask import Flask, request
from load_data import LoadData
from processor import Processor


app = Flask(__name__)

@app.route('/')
def index():
   endpoints_reader = LoadData()
   data = Processor()
   df_csv, df_json = endpoints_reader.read_data()
   summary_csv_info, summary_json_info = data.process_endpoints(df_csv, df_json)
   return 'Service A result: ' + summary_csv_info + \
           '\n' + 'Service B result: ' +  summary_json_info


if __name__ == '__main__':
   app.run(debug = True, port=8000)