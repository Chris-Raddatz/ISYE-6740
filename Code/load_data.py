import pandas as pd

CPI = pd.read_csv("data/US CPI.csv")
zillow = pd.read_csv("data/ZHVI.csv")

CPI['Month'] = CPI['Yearmon'].str.extract("(\d+)-\d+-\d+").fillna("")
CPI['Day'] = CPI['Yearmon'].str.extract("\d+-(\d+)-\d+").fillna("")
CPI['Year'] = CPI['Yearmon'].str.extract("\d+-\d+-(\d+)").fillna("") #Extract Month, Day and Year

zillow.rename(columns = {"Unnamed: 0" : "Date"}, inplace = True)

zillow['Month'] = zillow['Date'].str.extract("\d+-\d+-(\d+)").fillna("")
zillow['Day'] = zillow['Date'].str.extract("\d+-(\d+)-\d+").fillna("")
zillow['Year'] = zillow['Date'].str.extract("(\d+)-\d+-\d+").fillna("") #Extract Month, Day and Year


CPI.drop(columns = "Yearmon", inplace = True) #Drop Old column
zillow.drop(columns = "Date", inplace = True)

CPI = CPI[['Year', "Month", "Day", "CPI"]] #Reorganize columns
zillow = zillow[['Year', "Month", "Day"] + [col for col in zillow.columns[:-3] if col != ['Year', "Month", "Day"]]]  #Since there are so many columns, we can index for our desired start columns and add the rest

# Now we can remove null values and see how much data we lose

# North dakota and Montana have the majority though, with 108 and 61, respectively. The other null values: New Mexico and Wyoming, only have 27, let's remove North dakota and Montana then drop Nulls
# This way we only lose 30 odd rows and not 100
zillow.drop(columns = {"North Dakota", "Montana"}, inplace = True)
zillow.dropna(inplace = True)

merged_df = CPI.merge(zillow, on = ["Year", "Month", "Day"])


CPI.to_csv("data/clean_CPI.csv", index = False)
zillow.to_csv("data/clean_zillow.csv", index = False)

merged_df.to_csv("data/merged_df.csv", index = False)


# Data Cleaning, I want to tranpose the dataset into many rows for one date of CPI, with ZHVI values and a corresponding column that identifies what state it's from. 
dates_and_cpi = merged_df.iloc[:, :4]
dates_cpi_california = merged_df.iloc[:, :5]
dates_cpi_california['State'] = "California"
dates_cpi_california.rename(columns = {"California" : "ZHVI"}, inplace = True)

concat_df = pd.concat([dates_and_cpi, dates_cpi_california], axis = 0, ignore_index = True).dropna().reset_index(drop = True)


states = list(merged_df.columns)[5:] #Don't need to include california

#Expect a dataframe 11123 long
for i in states:
    just_that_state = merged_df[['Year', 'Month', 'Day', 'CPI', i]]
    just_that_state['State'] = i
    just_that_state.rename(columns = {i : "ZHVI"}, inplace = True)
    concat_df = pd.concat([concat_df, just_that_state], axis = 0, ignore_index = True).dropna().reset_index(drop = True)

concat_df.sort_values(by = ["Year", "Month", "Day"], inplace = True)

concat_df.to_csv("data/dummiable_data.csv", index = False)