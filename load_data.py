import pandas as pd

CPI = pd.read_csv("US CPI.csv")
zillow = pd.read_csv("ZHVI.csv")

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
zillow = zillow[['Year', "Month", "Day"] + [col for col in zillow.columns[:-3] if col != ['Year', "Month", "Day"]]] 
#Since there are so many columns, we can index for our desired start columns and add the rest

# Now we can remove null values and see how much data we lose

# North dakota and Montana have the majority though, with 108 and 61, respectively. The other null values: New Mexico and Wyoming, only have 27, let's remove North dakota and Montana then drop Nulls
# This way we only lose 30 odd rows and not 100
zillow.drop(columns = {"North Dakota", "Montana"}, inplace = True)
zillow.dropna(inplace = True)

merged_df = CPI.merge(zillow, on = ["Year", "Month", "Day"])
print(merged_df)


CPI.to_csv("clean_CPI.csv")
zillow.to_csv("clean_zillow.csv")

merged_df.to_csv("merged_df.csv", index = False)