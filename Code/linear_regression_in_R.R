df = read.csv("merged_df.csv")
library(ggplot2)
state = c()
r_squared = c()
coefficients = c()
for(i in 5:ncol(df)) {       # for-loop over columns
  col <- colnames(df)[i]
  state = c(state, col)
  print(col)
  formula <- as.formula(paste0(col,"~CPI"))
  model<-lm(formula, data=df)
  sum <- summary(model)
  print(sum)
  r_squared = c(r_squared, sum$r.squared)
  coefficients = c(coefficients, sum$coefficients[2, 1])
}

new_df = data.frame("State" = state, "R Squared" = r_squared, "Coefficient" = coefficients)
write.csv(new_df, "r_squared_values.csv")

new_df <- new_df[order(-new_df$Coefficient), ]

ggplot(new_df) + geom_bar(aes(x = reorder(State, Coefficient), y = Coefficient), stat = "identity") + coord_flip() + labs(title = "Coefficients For State From Linear Regression",
                                                                                                                          x = "State", y = "Coefficient")
