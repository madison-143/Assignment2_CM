#!/usr/bin/env python
# coding: utf-8

# # Linear Regression
# This script demonstrates a linear regression analysis using Python to model Salary based on Years of Experience by using arguments.

# Import sys, pandas, matplotlib.pyplot, LinearRegression from scikit-learn
import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# List arguments
if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_col> <y_col>")
    sys.exit(1)
    
filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

# list the dataset and model
dataset = pd.read_csv(filename)
model = LinearRegression()
model.fit(dataset[[x_col]], dataset[[y_col]])

# define r2
r2 = model.score(dataset[[x_col]], dataset[[y_col]])

# make scatter plot and regression graph, and save it to png
plt.scatter(dataset[[x_col]], dataset[[y_col]], color = "magenta", label = "Data points")
plt.plot(dataset[[x_col]], model.predict(dataset[[x_col]]), color = "teal", label = "Regression line")
plt.annotate(f'$R^2 = {r2:.3f}$', 
    xy = (dataset[x_col].min()*2.5, dataset[y_col].max()*0.7), fontsize = 12, color = "purple")
plt.title(f'{y_col} vs {x_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.legend()
plt.savefig("linear_regression_python_output.png")
plt.show()

