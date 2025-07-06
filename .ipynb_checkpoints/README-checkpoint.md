This is my README file for assignment 3 (Casey Madison): This README file will describe the repository

# Assignment 3 Notebooks and Scripts: Jupyter notebooks designed to enhance regression analysis from Assignment 2 with detailed diagnostics and annotated plots (Python and R). 

### Purpose
The purpose of this assignment is to expand off of Assignment 2 with more practice working with detailed model stats and graphing commands.

### Tools and libraries (Python):

pandas - offers tools for working with tables of data, allowing users to read, transform, and summarize datasets

numpy - tools for numerical and scientific computing in Python

matplotlib - tools used for creating plots and charts

scikit-learn - used to build models (LinearRegression)

plt is part of matplotlib, which is very important for python graphing. sklearn.metrics imports the capabilities to calculate mean squared error, an important metric for determining linear model fit. I shortened the x and y variables to a defined value (X and Y), so I didn't have to type out YearsExperience and Salary every time. Also, I needed to convert scalar to normal float in order to calculate slope and intercept. I like having fun with graphs, so I added a legend! With plt, this is very easy: plt.legend(). It is not so simple in R with ggplot2. An R2 value was included for another metric of linear regression model fit: model.score(x, y).

### Tools and Libraries (R):

ggplot2 - essential package for creating graphs.

ggplot2 is a package that I incorporated into my environment, so I didn't have to install it every single time. You do need to load it into the notebook every time with library(ggplot2). In my opinion, adding annotations and other aspects to graphs in R is much harder than python, but I managed. Annotations are added using annotate("text", x-position, y-position, color, label = paste(text)), and I added a legend using scale_color_manual. scale_color_manual allows you to put your labels in the "color" spot. For example, in geom_point, I have color = "Data points". Later in the code, I specify that the actual color is green via "Data points" = "green". This can be used for multiple purposes, but it allowed me to create a legend.

### Scripts:
Scripts were run very similarly to Assignment 2. However, I did set it up so the stats (r, r2, slope, intercept, mse) printed to the console after running the script. For python, this is as simple as using the print function and f", for example: print(f"slope is {slope}"). For R, I used the cat() function. The line setup for this is as follows: cat("Slope:", slope, "\n"). Text is in quotations ("Slope:") the calculation I want to run is NOT in quotes (slope), and \n at the end means new line. 

Running Scripts:

Python: python linear_model.py regression_data.csv YearsExperience Salary
R: Rscript linear_model.r regression_data.csv YearsExperience Salary

### Results:

I was able to graph the plot, linear regression, legend, and annotations to the graph. Additionally, I calculated r, r2, mse, slope, and y-intercept. The MSE value was very large, the r and r2 values were around 0.8 and 0.7, respectively, which does not indicate good fit. The y-intercept was 29203, which means with 0 years of experience, the predicted salary is $29,203. The slope was 8285, which means with every 1 year of added experience, the salary is predicted to increase by $8,285. Because the linear model has bad fit, predictions should be considered a loose estimate.


