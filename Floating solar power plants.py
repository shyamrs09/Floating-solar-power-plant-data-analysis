# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 18:59:26 2020

@author: shyam14rs
"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(r"D:\Renewable energy systems\Semester 2\Subjects\scientific project 2\Final program\world-floating-solar-power-plant-2016.xlsx")
df
df1 = df.iloc[:,[1,3]] #separating the column 1 and 3
df1
grouped = df1['Size (kw)'].groupby(df1['Country']) # grouping size and country
grouped.sum() #adding all
series = grouped.sum()
series.values
series.index
series = series.sort_values(ascending=False)
plt.figure(figsize=(20,5))
plt.plot(series)
plt.title('World floating solar power plant in 2016 by Country')
plt.ylabel('Size [$KW$]')
plt.xlabel('Country')
plt.show()
plt.savefig('World floating solar power plant in 2016 by country.jpeg',bbox_inches='tight', dpi=150, transparent=False)
df2=df[df['Country']=='Japan'] # creating a dataframe for country Japan by using equal to operator
df2
df3 = df2.iloc[:,[1,4]]
df3
grouped2 = df3['Size (kw)'].groupby(df['City/Province'])
grouped2.sum()
series2=grouped2.sum()
plt.figure(figsize=(20,5))
series2.plot.bar()
plt.title('floating solar power plant in 2016 in Japan')
plt.ylabel('Size [$KW$]')
plt.xlabel('City/Province in Japan')
plt.show()
df4 = df.iloc[:,[1,7]]
df4
grouped3 = df3['Size (kw)'].groupby(df['Floating'])
grouped3.sum()
series3=grouped3.sum()
values=series3.values
labels=series3.index
plt.figure(figsize=(20,15))
plt.pie(values,labels=labels,autopct='%1.1f%%')
plt.title('floating solar power plant manufacturers')
df5 = df.iloc[:,[1,2]]
df5
df6=df5.nlargest(20,['Size (kw)'])
print(df6)