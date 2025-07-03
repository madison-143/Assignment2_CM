
args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 3) {
    stop("Usage: Rscript linear_model.r <filename> <x_col> <y_col>")}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

dataset <- read.csv(filename)

formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data=dataset)
model_summary <- summary(model)
slope <- coef(model)[2]
intercept <- coef(model)[1]
r2 <- model_summary$r.squared
r <- cor(dataset[[x_col]], dataset[[y_col]])
mse <- mean((predict(model) - dataset[[y_col]])^2)

dataset$predicted <- predict(model, newdata = dataset)

library(ggplot2)

dataset$Group <- "Data points"

plot <- ggplot(dataset, aes(x = .data[[x_col]], y = .data[[y_col]])) +
geom_point(aes(color = Group)) +
geom_line(aes(y = predicted, color = "Fitted line")) +
annotate("text", x = 2, y = 60000, col = "navy",
         label = paste(
            "y =", round(slope, 2),"x +", round(intercept,2), "\n",
            "r2:", round(r2, 2), "\n",
            "r:", round(r, 2), "\n",
            "MSE:", round(mse, 2), "\n")) +             
ggtitle(paste(y_col, "vs", x_col)) +
xlab(x_col) +
ylab(y_col) +
scale_color_manual(
    name = "Legend",
    values = c("Data points" = "green", 
               "Fitted line" = "purple")) 

ggsave("regression_plot_r.png", plot)
print(plot)

cat(
"Slope:", slope, "\n",
"Intercept:", intercept, "\n",
"r2:", r2, "\n",
"r:", r, "\n",
"MSE:", mse, "\n")
