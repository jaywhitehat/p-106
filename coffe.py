import plotly_express as px
import csv
import numpy as np

with open ("coffe_data.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="week",y="Coffee in ml")
    fig.show()


def getDataSource(data_path):
    week = []
    Coffee_in_ml = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            week.append(float(row["week"]))
            Coffee_in_ml.append(float(row["Coffee in ml"]))

    return {"x" : week, "y": Coffee_in_ml}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between week No and Coffee in ml :-  \n--->",correlation[0,1])

def setup():
    data_path  = "coffe_data.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()