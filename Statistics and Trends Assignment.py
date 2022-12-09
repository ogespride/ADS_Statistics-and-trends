import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def electricity(filename):
    """This is a function that reads csv file and returns an output of two dataframes with years and countries as columns"""
    df = pd.read_csv(filename,skiprows=4)
    df = df.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis = 1)
    df_electricity = df
    df_electricity_transpose = df.T
    df_electricity_transpose = df_electricity_transpose.rename(columns=df_electricity_transpose.iloc[0])
    df_electricity_transpose = df_electricity_transpose.drop(index=df_electricity_transpose.index[0], axis=0)
    df_electricity_transpose = df_electricity_transpose.reset_index()
    df_electricity_transpose = df_electricity_transpose.rename(columns={"index":"Year"})
    
    return df_electricity, df_electricity_transpose

#df1=original dataframe of climate change indicator; df2=transposed dataframe
df1,df2 = electricity("Electric power consumption.csv")
print(df1)
print(df2)

#showing dataframe of individual countries selected for comparison 
Countries = df2[['Year','Argentina','China','Nigeria','United Arab Emirates','United Kingdom','United States']]
Countries = Countries.dropna() 
Countries = Countries.reset_index()
Countries = Countries.drop(columns='index')
print(Countries)

#line plot for Electric power consumption
Electric_power_consumption = Countries.iloc[23:, :]
Electric_power_consumption.plot("Year",['Argentina','China','Nigeria','United Arab Emirates','United Kingdom',
                                           'United States'], title="Electric power consumption")  
plt.xticks(rotation=45.0)
plt.show()