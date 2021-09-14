import csv
import time
import plotly.express as px
import numpy as np

def plot_fig(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x='Marks In Percentage', y='Days Present')
        fig.show()
def getdataSource(data_path):
    marks = []
    dayspresent = []
    with open(data_path) as f:
        csvReader = csv.DictReader(f)

        for row in csvReader:
            marks.append(float(row['Marks In Percentage']))
            dayspresent.append(float(row['Days Present']))
    return{'x':marks,
           'y':dayspresent
           }
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print('Correlation between Marks In Percentage and Days Present is', correlation[0,1])

def setup():
    data_path = 'student-marks-vs-days-present.csv'
    datasource = getdataSource(data_path)
    findCorrelation(datasource)
    time.sleep(5)
    plot_fig(data_path)

setup()
    
