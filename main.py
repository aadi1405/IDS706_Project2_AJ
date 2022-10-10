import pandas as pd
from pandasql import sqldf
import typer
from psycopg2.extras import NamedTupleCursor
import seaborn as sns

from tabulate import tabulate

app = typer.Typer()

df = pd.read_csv('/workspaces/IDS706_Project2_AJ/dataset/marketing_campaign.csv',sep='\t')

@app.command()
def getinfo():
    ''' Get details of the database'''
    df = pd.read_csv('/workspaces/IDS706_Project2_AJ/dataset/marketing_campaign.csv',sep='\t')
    df.info()
    
@app.command()
def randomsample():
    ''' Get random sample of the database'''
    df = pd.read_csv('/workspaces/IDS706_Project2_AJ/dataset/marketing_campaign.csv',sep='\t')
    print(df.sample(10))
    

@app.command()
def shape():
    """return the total study hour of the week of each student""" 
    print("There are {} rows and {} columns in the dataset".format(df.shape[0],df.shape[1]))


@app.command()
def diffedu():
    """ return the total the different cateogaries of edu  """
    print(df['Education'].value_counts())

@app.command()
def eduvalue(x,y):
    """ return the total amount spent on a particular class of product by  education """
    
    if x == 'PhD':
            #find the average amount on sweet products by education
            print("On an average a person who completed {x} spends {z} in 2 years on {y} products in your store".format(x=x,y=y,z=df[df['Education'] == 'PhD'][y].mean()))
            
    elif x == 'Graduation':
            #find the average amount on sweet products by age group
            print("On an average a person who completed {x} spends {z} in 2 years on {y} products in your store".format(x=x,y=y,z=df[df['Education'] == 'Graduation'][y].mean()))
    elif x == 'Master':
            #find the average amount on sweet products by age group
            print("On an average a person who completed {x} spends {z} in 2 years on {y} products in your store".format(x=x,y=y,z=df[df['Education'] == 'Master'][y].mean())) 
    elif x == '2n Cycle': 
            #find the average amount on sweet products by age group
            print("On an average a person who completed {x} spends {z} in 2 years on {y} products in your store".format(x=x,y=y,z=df[df['Education'] == '2n Cycle'][y].mean()))     
    elif x== 'Basic':
            #find the average amount on sweet products by age group
            print("On an average a person who completed {x} spends {z} in 2 years on {y} products in your store".format(x=x,y=y,z=df[df['Basic'] == 'PhD'][y].mean())) 
    else:
            print("Please enter a valid education level")  

@app.command()
def describe():
    """ return the description of the dataset """
    print(df.describe())

@app.command()
def countforme(x):
    """ return the total count of particular kind of purchases """
    print("The total {x} made in the last two years is ".format(x=x) + str(df[x].sum()))



if __name__ == "__main__":
    app()
    argument = 0
    #passing string argument to the function
    eduvalue(argument)
