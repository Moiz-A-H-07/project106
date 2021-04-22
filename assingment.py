import csv
import plotly.express as px
import numpy as np
def plotfigure(datapath):
    with open(datapath) as csvfile:
        df=csv.DictReader(csvfile)
        fig=px.scatter(df,x="Days Present",y="Marks In Percentage")
        fig.show()
def getdatasource(datapath):
    marksandpercentage=[]
    dayspresent=[]
    with open(datapath) as csvfile:
        csvreader=csv.DictReader(csvfile)
        for row in csvreader:
            marksandpercentage.append(float(row["Marks In Percentage"]))
            dayspresent.append(float(row["Days Present"]))
    return{"x":marksandpercentage,"y":dayspresent}
def findcorelation(datasource):
    corelation=np.corrcoef(datasource["x"],datasource["y"])
    print("carelation between marks and dayspresent",corelation[0,1])
def setup():
    datapath="./data/Student Marks vs Days Present.csv"
    datasource=getdatasource(datapath)
    findcorelation(datasource)
    plotfigure(datapath)
setup()