df = read.csv("merged_df.csv")
state = c()
r_squared = c()
for(i in 5:ncol(df)) {       # for-loop over columns
  col <- colnames(df)[i]
  state = c(state, col)
  formula <- as.formula(paste0(col,"~CPI"))
  model<-lm(formula, data=df)
  sum <- summary(model)
  r_squared = c(r_squared, sum$r.squared)
}

new_df = data.frame("State" = state, "R Squared" = r_squared)
