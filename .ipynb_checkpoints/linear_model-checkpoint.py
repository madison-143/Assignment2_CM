#!/usr/bin/env python
# coding: utf-8

# # Linear Regression
# This script demonstrates a linear regression analysis using Python to model Salary based on Years of Experience.

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error


if len(sys.argv) != 4:
    print("Usage: python linear_model.py <filename> <x_col> <y_col>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]


dataset = pd.read_csv(filename)


X = dataset[[x_col]]
Y = dataset[[y_col]]


model = LinearRegression()
model.fit(X, Y)


model.score(X, Y)


slope = model.coef_[0]
slope = slope.item()

intercept = model.intercept_
intercept = intercept.item()


y_predicted = model.predict(X)


mse = mean_squared_error(Y,y_predicted)


r2 = model.score(X, Y)
r = dataset[x_col].corr(dataset[y_col])

plt.scatter(X, Y, color = "magenta", label = "Data points")
plt.plot(X, y_predicted, color = "teal", label = "Fitted line")
metrics_text = (
    f"y = {slope:.3f}x + {intercept:.3f}\n"
    f"r2 = {r2:.3f}\nr = {r:.3f}\nMSE = {mse:.3f}")
plt.text(1, 55000, metrics_text, fontsize = 10, color = "purple")
plt.title(f'{y_col} vs {x_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.legend()
plt.savefig("regression_plot_python.png")
plt.show()


print(f"slope is {slope}")
print(f"intercept is {intercept}")
print(f"mse is {mse}")
print(f"r2 is {r2}")
print(f"r is {r}")

