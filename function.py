import pandas as pd
#from pandasql import sqldf
import typer
#from psycopg2.extras import NamedTupleCursor

#from tabulate import tabulate

app = typer.Typer()

@app.command()
def loadData(): 
    """Load dataset"""
    df = pd.read_csv('/workspaces/IDS706_Project2_AJ/dataset/Student_Study_data.csv')

@app.command()
def viewdata():
    """fetch items list"""
    df = pd.read_csv('/workspaces/IDS706_Project2_AJ/dataset/Student_Study_data.csv')
    print(df)


@app.command()
def liststudents():
    """return sorted list by calories"""
    df = pd.read_csv('/workspaces/IDS706_Project2_AJ/dataset/Student_Study_data.csv')
    count1 = df['Name'].value_counts()
    print(count1)

@app.command()
def seemax():
    """See max value of each dataset"""
    df = pd.read_csv('menu.csv')
    max_values = df[['Calories','Total Fat','Carbohydrates','Dietary Fiber','Sugars','Protein','Vitamin A (% Daily Value)','Vitamin C (% Daily Value)','Calcium (% Daily Value)','Iron (% Daily Value)']].max()
    print(max_values)

if __name__ == "__main__":
    app()