This is my README file for assignment 2 (Casey Madison)

### Jupyter Notebook: Assignment 2 Part 1

# Purpose: 
The purpose of this assignment is to practice loading a CSV datset and create linear regression models in Jupyter Notebooks using Python and R. Additionally, we learned how to create and export a graph depicting the model's performance.

# Tools and Libraries for Python Notebook:
pandas: offers tools for working with tables of data, allowing users to read, transform, and summarize datasets.

matplotlib: tool used for creating plots and charts.

scikit-learn: used to build models (we imported the LinearRegression model from this library).

# Tools and Libraries for R Notebook:
ggplot2: allows advanced plotting (ggplot2 is installed to my environment).

After installation, packages must be loaded using library().

# Results
Python Notebook: I was able to graph the plot and linear regression line. Additionally, I added a legend and an annotation of the r2 value on to the graph.

R Notebook: I graphed the plot and linear regression line with no additional aspects. However, I did mess around with the colors.

### Scripting in R and Python: Assignment 2 Part 2

# Purpose
The purpose of this part of the assignment is to learn how to convert notebooks into scripts using arguments, and the scripts should be able to be run from the command line.

# Python Script Tools and Notes
Import the same libraries as above, as well as the one below.

sys: allows command line arguments (sys.argv).

Create an argument using sys.argv, and the three arguments are filename, x_col, and y_col.

Replace the Jupyter Notebook code with argument syntax in the proper locations.

Additionally, use plt.savefig("filename") to export the image of the graph.

# R Script Tools and Notes
Import the ggplot as above.

args: allows command line arguments.

Create an argument using args, adn the three arguments are filename, x_col, and y_col.

Replace the Jupyter Notebook code with the argument syntax in the proper locations.

Note: aes_string is not that compatible with my version of R, so I had to modify the code (just used aes).

Note: I converted the strings to symbols for tidy evaluation. When incorporated into the graph code, I used !! to tell R that the symbols are NOT part of dataset, and to not look for them there (because of how I set up the code, R will automatically look for variables within dataset first unless I tell it otherwise).

Note: Even though dataset is in the main ggplot(), I still specificied in the geom_line code to avoid confusion.

# Running Python Script in Command Line:
python python_linear_regression.py regression_data.csv YearsExperience Salary

# Running R Script in Command Line:
Rscript r_linear_regression.r regression_data.csv YearsExperience Salary




