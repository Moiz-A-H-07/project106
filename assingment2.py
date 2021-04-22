import csv
import plotly.express as px
import numpy as np
def plotfigure(datapath):
    with open(datapath) as csvfile:
        df=csv.DictReader(csvfile)
        fig=px.scatter(df,x="SizeofTV",y="timewatching")
        fig.show()
def getdatasource(datapath):
    size=[]
    timespent=[]
    with open(datapath) as csvfile:
        csvreader=csv.DictReader(csvfile)
        for row in csvreader:
            size.append(float(row["SizeofTV"]))
            timespent.append(float(row["timewatching"]))
    return{"x":size,"y":timespent}
def findcorelation(datasource):
    corelation=np.corrcoef(datasource["x"],datasource["y"])
    print("carelation between sizeof tv and watchingtv",corelation[0,1])
def setup():
    datapath="./data/watchingandtv.csv"
    datasource=getdatasource(datapath)
    findcorelation(datasource)
    plotfigure(datapath)
setup()