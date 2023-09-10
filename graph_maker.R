library(ggplot2)

data <- read.csv('empty_sheet.csv', header=TRUE)
clean_data <- data[c(1,5)]
plot <- ggplot(data = clean_data, aes(x = Date, y = Close)) +
  geom_point() +
  labs(x = "Date",
       y = "Price at Close",
       title = "Stock Price",
       subtitle = "2020-2021")

setwd('/Users/jaredking/Stock_bot/')
png(file='stock_plot.png', width = 500, height = 500)

plot

dev.off()
