import pandas as pd
import matplotlib.pyplot as plt


#join data for geojson stuff

df_fips = pd.read_csv("data/county_towns.csv")
df_perc = pd.read_csv("data/percents.csv")

df_perc['town'] = df_perc['town'].str.upper()
df_perc['town'] = df_perc['town'].str.strip()
df_join = df_fips.merge(df_perc, on='town', how='left')

df_join.to_csv('data/town_percents.csv', index=False)


'''
#bosfed data cleaning

df = pd.read_csv("data/neppcpr1901-data.csv")

# df without unecessary cols
df_short = df.drop(['YEAR', 'STATE GEO', 'COUNTY GEO', 'CITY/TOWN GEOID'], axis=1)
# df only with cols i'm interested in
df_intr = df[['COUNTY NAME', 'CITY/TOWN NAME', 'NO. OF ELI RENT BURDENED (30%)', 'NO. OF RENTER HOUSEHOLDS', 'NO. OF ELI HOUSEHOLDS']]

# df with percentages i'm interested in
df_perc = df[['COUNTY NAME', 'CITY/TOWN NAME']]
df_perc['PERCENT ELI'] = df_intr['NO. OF ELI HOUSEHOLDS'] / df_intr['NO. OF RENTER HOUSEHOLDS']
df_perc['PERCENT RENT BURDENED ELI'] = df_intr['NO. OF ELI RENT BURDENED (30%)'] / df_intr['NO. OF ELI HOUSEHOLDS']

with open('percents.txt', 'w') as f:
    for i in range(313):
        text = df_perc['CITY/TOWN NAME'].iloc[i] + "," + str(df_perc['PERCENT ELI'].iloc[i]) + "\n"
        f.write(text)
'''


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
