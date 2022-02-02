import plotly_express as px
import csv
import numpy as np

with open ("std_data.csv") as csv_file:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Roll No",y="Marks In Percentage")
    fig.show()


def getDataSource(data_path):
    Roll_No = []
    Marks_In_Percentage = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Roll_No.append(float(row["Roll No"]))
            Marks_In_Percentage.append(float(row["Marks In Percentage"]))

    return {"x" : Roll_No, "y": Marks_In_Percentage}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Roll No and Marks In Percentage :-  \n--->",correlation[0,1])

def setup():
    data_path  = "std_data.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()