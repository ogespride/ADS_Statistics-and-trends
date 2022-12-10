import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def worldbank(filename,countries,columns,indicator):
    """This is a function that reads csv file and returns an output of two dataframes""" 
    df = pd.read_csv(filename,skiprows=4)
    df = df[df['Indicator Name'] == indicator]
    df = df[columns]
    df.set_index('Country Name', inplace = True)
    df = df.loc[countries]
    return df,df.transpose()

#Showing dataname, countries, climate change indicators and period of years being compared.
filename = 'Worldbank_data.csv'
countries = ['Argentina','China','Nigeria','United Arab Emirates','United States']
columns = ['Country Name', '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010']
indicators = ['Urban population', 'CO2 emissions from liquid fuel consumption (kt)', 'Electric power consumption (kWh per capita)','Arable land (% of land area)']

indicator_urb_pop,year_urb_pop = worldbank(filename,countries,columns,indicators[0])
indicator_co2,year_co2 = worldbank(filename,countries,columns,indicators[1])
indicator_elec,year_elec = worldbank(filename,countries,columns,indicators[2])
indicator_arland,year_arland = worldbank(filename,countries,columns,indicators[3])
print(year_urb_pop)#showing transpose dataframe

#Showing line plot
plt.figure(figsize=(10,7),dpi=500)
for i in range(len(countries)):
    plt.plot(year_urb_pop.index,year_urb_pop[countries[i]],label=countries[i])
plt.legend(bbox_to_anchor=(1,1))
plt.title('Year on Year Trend of the Urban Population for these 5 countries')
plt.xlabel('Year')
plt.ylabel('Urban Population')
plt.show()

#Showing original dataframe and bar chat for urban population growth amongst different countries
print(indicator_urb_pop) 

