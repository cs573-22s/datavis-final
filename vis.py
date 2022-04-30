import pandas as pd
import matplotlib.pyplot as plt


# interested in % renter households ELI and % ELI that are cost burdened
df = pd.read_csv("data/neppcpr1901-data.csv")

df_short = df.drop(['YEAR', 'STATE GEO', 'COUNTY GEO', 'CITY/TOWN GEOID'], axis=1)
df_intr = df[['COUNTY NAME', 'CITY/TOWN NAME', 'NO. OF ELI RENT BURDENED (30%)', 'NO. OF RENTER HOUSEHOLDS', 'NO. OF ELI HOUSEHOLDS']]



'''
# HOMEOWNERSHIP RACE DISPARITY

df = pd.read_csv("data/homeowner_dis.csv")

plt.title('Homeownership Racial Disparity')
plt.xlabel('Race')
plt.ylabel('Percent Homeownership')
plt.xticks(rotation = 65,fontsize=7)

plt.bar(df.columns, df.iloc[0])
plt.gcf().subplots_adjust(bottom=0.4)

plt.show()
'''


'''
# MED HOUSEHOLD INCOME VS MED LIST PRICE

df = pd.read_csv("data/listprice_houseincome.csv")

df_rna = df[df['MEHOIN'].notna()]
df_rna['ratio'] = df_rna['MEDLISPRI'] / df_rna['MEHOIN']

import datetime as dt
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in df_rna['DATE']]

plt.title('Med List Price:Med Household Income in Massachusetts')
plt.xlabel('Year')
plt.ylabel('Med List Price:Med Household Income')

import matplotlib.dates as mdates
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
#plt.plot(x, df_rna['ratio'])
plt.plot(x, df_rna['MEDLISPRI'])
plt.plot(x, df_rna['MEHOIN'])
plt.gcf().autofmt_xdate()

plt.show()
'''


'''
# MED INCOME VS MED PROP VALUE

df = pd.read_csv("data/prop_income.csv")
#row 1 is med income, row 2 is med prop value

df.loc['ratio'] = df.iloc[0] / df.iloc[1]

plt.title('Med Income:Med Property Value in Massachusetts')
plt.xlabel('Year')
plt.ylabel('Med Income:Med Property Value')
plt.plot(df.columns, df.loc['ratio'])
plt.show()
'''
