# commandArgs retrieves the arguments. trailingOnly = True means that R is only going to return arguments after the script name.
args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 3) {
    stop("Usage: Rscript linear_regression_r.R <filename> <x_col> <y_col>")}

# Define arguments for the file name, x-column and y-column
filename <- args[1]
x_col <- args[2]
y_col <- args[3]

# Define dataset, formula, and model
dataset <- read.csv(filename)
formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data = dataset)

# Load ggplot2 so we can work with it
library(ggplot2)

# Define "predicted" for linear regression line of best fit from the dataset (I didn't want to write all of it below...)
dataset$predicted <- predict(model, newdata = dataset)

# I converted strings to symbols for tidy evaluation, aes_string is not compatible for my version of ggplot. I don't think I had to do it this way, but it works.
x_sym <- sym(x_col)
y_sym <- sym(y_col)

# Let's make the plot with fun colors!
## I had to look up how to deal with symbols. The exclamation marks tell the program NOT to look for x_sym and y_sym in the dataset, as they do not exist there.
plot <- ggplot(dataset, aes(x = !!x_sym, y = !!y_sym)) +
geom_point(col = "green") +
geom_smooth(method = "lm", color = "pink") +
geom_line(aes(y = predicted), col = "blue", data = dataset) +
ggtitle(paste(y_col, "vs", x_col)) +
xlab(x_col) +
ylab(y_col)

# Save and print the plot
ggsave("linear_regression_r_output.png", plot)
print(plot)


