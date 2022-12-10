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

#Showing line plots for Urban Population amongst the countries
plt.figure(figsize=(10,7),dpi=500)
for i in range(len(countries)):
    plt.plot(year_urb_pop.index,year_urb_pop[countries[i]],label=countries[i])
plt.legend(bbox_to_anchor=(1,1))
plt.title('Year on Year Trend of the Urban Population for these 5 countries')
plt.xlabel('Year')
plt.ylabel('Urban Population')
plt.show()

#Showing original dataframe 
print(indicator_urb_pop) 

#Showing line plot for CO2 Emission from liquid fuel consumption amongst the countries
plt.figure(figsize=(10,7),dpi=500)
for i in range(len(countries)):
    plt.plot(year_co2.index,year_co2[countries[i]],label=countries[i])
plt.legend(bbox_to_anchor=(1,1))
plt.title('Year on Year Trend of the CO2 Emissions from liquid fuel Consumption for these 5 countries')
plt.xlabel('Year')
plt.ylabel('CO2 Emissions')
plt.show()
print(indicator_co2)

#Showing line plot for Electric Power Consumption amongst the countries
plt.figure(figsize=(10,7),dpi=500)
for i in range(len(countries)):
    plt.plot(year_elec.index,year_elec[countries[i]],label=countries[i])
plt.legend(bbox_to_anchor=(1,1))
plt.title('Year on Year Trend of the Electric Power Consumption for these 5 countries')
plt.xlabel('Year')
plt.ylabel('Electric Power Consumption')
plt.show()
print(indicator_elec)

#Showing line plot for Arable land(% of land area) amongst the countries
plt.figure(figsize=(10,7),dpi=500)
for i in range(len(countries)):
    plt.plot(year_arland.index,year_arland[countries[i]],label=countries[i])
plt.legend(bbox_to_anchor=(1,1))
plt.title('Year on Year Trend of the Arable land for these 5 countries')
plt.xlabel('Year')
plt.ylabel('Arable land')
plt.show()
print(indicator_arland)

#Showing bar chat for urban population growth amongst different countries
indicator_urb_pop.plot(kind='bar')
plt.title('Grouped bar for Urban Population for different countries over the years')
plt.xlabel('Countries')
plt.ylabel('Urban Population')
#plt.rcParams["figure.dpi"] = 1000
plt.show()

#Showing bar chat for Elecric Power Consumption growth amongst different countries
indicator_elec.plot(kind='bar')
plt.title('Grouped bar for Electric Power Consumption for different countries over the years')
plt.xlabel('Countries')
plt.ylabel('Electric Power Consumption')
#plt.rcParams["figure.dpi"] = 1000
plt.show()

#Showing bar chat for Arable land(% of land area) growth amongst different countries
indicator_arland.plot(kind='bar')
plt.title('Grouped bar for Arable land for different countries over the years')
plt.xlabel('Countries')
plt.ylabel('Arable land')
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
#plt.rcParams["figure.dpi"] = 1000
plt.show() 