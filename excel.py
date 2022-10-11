# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 14:20:34 2022

@author: mkc


pip install pandas
pip install matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt


var = pd.read_excel("Mappe2.xlsx")
print(var)



#Separating x and y values
x = list(var['X values'])
y = list(var['Y values'])


#xs = [1,2,3,4,5]
#ys = [3,5,1,2,4]

#Plotting a Scatter Plot
plt.figure(figsize=(10,10))
plt.style.use('seaborn')
plt.scatter(x,y,marker="*",s=100,edgecolors="black",c="yellow")
plt.title("Excel sheet to Scatter Plot")
plt.show()