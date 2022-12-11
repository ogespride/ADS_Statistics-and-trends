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

#Statistical properties of indicator
#Urban population
print(indicator_urb_pop.describe())
#CO2 Emission from liquid fuel consumption
print(indicator_co2.describe())
#Electric Power Consumption
print(indicator_elec.describe())
#Arable land(% of land Area)
print(indicator_arland.describe())

#Showing Correlations between Countries and Indicators
#Argentina
Argentina = pd.DataFrame(
{'Urban Population': year_urb_pop['Argentina'],
'Co2 emission': year_co2['Argentina'],
'Elec. Access': year_elec['Argentina']},
['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010'])
print(Argentina.corr())

#Using heatmap graph to show correlation between the indicators and Argentina
plt.figure(figsize=(8,5))
sns.heatmap(Argentina.corr(),annot=True,cmap='Greens')
plt.title('Correlation heatmap Argentina')

#Showing Correlations between Countries and Indicators
#China
China = pd.DataFrame(
{'Urban Population': year_urb_pop['China'],
'Co2 emission': year_co2['China'],
'Elec. Access': year_elec['China']},
['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010'])
print(China.corr())

#Using heatmap graph to show correlation between the indicators and China
plt.figure(figsize=(8,5))
sns.heatmap(China.corr(),annot=True,cmap='Greens')
plt.title('Correlation heatmap China')

plt.show()

#Showing Correlations between Countries and Indicators
#Nigeria
Nigeria = pd.DataFrame(
{'Urban Population': year_urb_pop['Nigeria'],
'Co2 emission': year_co2['Nigeria'],
'Elec. Access': year_elec['Nigeria']},
['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010'])
print(Nigeria.corr())

#Using heatmap graph to show correlation between the indicators and Nigeria
plt.figure(figsize=(8,5))
sns.heatmap(Nigeria.corr(),annot=True,cmap='Greens')
plt.title('Correlation heatmap Nigeria')

plt.show()

#Showing Correlations between Countries and Indicators
#United Arab Emirates
UnitedArabEmirates = pd.DataFrame(
{'Urban Population': year_urb_pop['United Arab Emirates'],
'Co2 emission': year_co2['United Arab Emirates'],
'Elec. Access': year_elec['United Arab Emirates']},
['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010'])
print(UnitedArabEmirates.corr())

#Using heatmap graph to show correlation between the indicators and United Arab Emirates
plt.figure(figsize=(8,5))
sns.heatmap(UnitedArabEmirates.corr(),annot=True,cmap='Greens')
plt.title('Correlation heatmap UnitedArabEmirates')

plt.show()

#Showing Correlations between Countries and Indicators
#United States
UnitedStates = pd.DataFrame(
{'Urban Population': year_urb_pop['United States'],
'Co2 emission': year_co2['United States'],
'Elec. Access': year_elec['United States']},
['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010'])
print(UnitedStates.corr())

#Using heatmap graph to show correlation between the indicators and United States
plt.figure(figsize=(8,5))
sns.heatmap(UnitedStates.corr(),annot=True,cmap='Greens')
plt.title('Correlation heatmap UnitedStates')

plt.show()

