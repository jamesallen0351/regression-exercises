# imports

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

from env import host, user, password # I already added my env to .gitignore first and then to my repository

# establishing get_connection function
def get_connection(db, user=user, host=host, password=password):
    '''
    This function gets my info from my env file and creats a connection url 
    
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    # getting zillow data from codeup database

def new_zillow():
    
    sql_query ='''select bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips from properties_2017
    
    join propertylandusetype using(propertylandusetypeid)
    where propertylandusetypeid = 261'''
    
    df = pd.read_sql(sql_query, get_connection('zillow'))

    # Replace a whitespace sequence or empty with a NaN value and reassign this manipulation to df.
    df = df.replace(r'^\s*$', np.nan, regex=True)

    df = df.dropna()

    df = df.astype('int')
    
    return df 

def wrangle_zillow():
    
    '''get connection, returns Zillow into a dataframe and creates a csv for us'''
    
    if os.path.isfile('zillow.csv'):
        
        df = pd.read_csv('zillow.csv', index_col=0)
    
    else:
        
        df = new_zillow()
        
        df.to_csv('zillow.csv')
    
    return df

def wrangle_prep_zillow(df):
    '''
    This function will handles duplicates, nulls, strings, and then returns the df
    '''
    # drop any duplicates
    df.drop_duplicates(inplace=True)
    
    # Replace a whitespace sequence or empty with a NaN value and reassign this manipulation to df.
    df = df.replace(r'^\s*$', np.nan, regex=True)
    
    # drop rows that contain null values, they are a small percentage
    df.dropna(axis=0, inplace=True)
    
    # changes df type to from 'float64' to 'int'
    df = df.astype('int')
    
    return df