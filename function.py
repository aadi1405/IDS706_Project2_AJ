import pandas as pd
from pandasql import sqldf
import typer
from psycopg2.extras import NamedTupleCursor

from tabulate import tabulate

app = typer.Typer()

@app.command()
def loadData(): 
    """Load dataset"""
    df = pd.read_csv('/workspaces/IDS706_Project2_AJ/dataset/Student_Study_data.csv')

@app.command()
def viewdata():
    """fetch the data"""
    df = pd.read_csv('/workspaces/IDS706_Project2_AJ/dataset/Student_Study_data.csv')
    print(df)


@app.command()
def liststudents():
    """return the number of entries of each student"""
    df = pd.read_csv('/workspaces/IDS706_Project2_AJ/dataset/Student_Study_data.csv')
    count1 = df['Name'].value_counts()
    print(count1)

@app.command()
def studyhour():
    """return the total study hour of the week of each student"""
    df = pd.read_csv('/workspaces/IDS706_Project2_AJ/dataset/Student_Study_data.csv')
    studyhour = df.groupby('Name')['study_hour'].sum()
    print("the weekly study time of each student is: ")
    print(studyhour)

@app.command()
def sleephour():
    """return the total sleep hours for the week of each student"""
    df = pd.read_csv('/workspaces/IDS706_Project2_AJ/dataset/Student_Study_data.csv')
    studyhour = df.groupby('Name')['your sleep hour?'].sum()
    print("the weekly sleep time of each student is: ")
    print(studyhour)
    mean = df['your sleep hour?'].mean()
    print('the average sleep time is ' + str(mean))


@app.command()
def agerange():
    """return the total sleep hours for the week of each student"""
    df = pd.read_csv('/workspaces/IDS706_Project2_AJ/dataset/Student_Study_data.csv')
    age_min = df['what is your age?'].min()
    age_max = df['what is your age?'].max()
    print("the age range of the students is from " + str(age_min) + " to " + str(age_max))
   

if __name__ == "__main__":
    app()