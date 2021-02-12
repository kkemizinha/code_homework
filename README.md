## **Overview**:

A HTTP service that reads the data from the external services and returns 
the mean and sum of those values.

<br /><br />

## **Files**:

app.py              :  Run Flask script

code_hw.yml         : Conda environment to run this project

config.ini          : Link to endpoints

integration_test.py : A class used to perform integration test

load_data.py        : A class used to load the CSV and JSON data

processor.py        : A class used to handle, treat and calculate the CSV and JSON data

unit_test.py        : A class used to perform unit tests

<br /><br />

## **How to run**:

1) Conda environment: <br />
    
    conda env create -f code_hw.yml -n code_hw

2) Activate new environment: <br />
    
    conda activate code_hw

3) Run flask server <br />
UNIX: <br />
    export FLASK_ENV=development <br />
    export FLASK_APP=app.py

Windows:
    set FLASK_ENV=development
    set FLASK_APP=app.py

    flask run -h localhost -p 8000

4) In a separate Terminal: curl http://localhost:8000
It's expected to get the JSON results

<br /><br />

## **Running tests**:

1) For unit tests: <br />
     python unit_test.py

2) For integration test: <br />
     python integration_test.py
