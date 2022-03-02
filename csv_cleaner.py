import pandas as pd

# making data frame from csv file
data = pd.read_csv(
    "prajwalCode/prob_rec_toclean.csv", index_col="Tags_n")

print(data)

# dropping passed values

data.drop(["[]"], inplace=True)
# data[data['Tags'].map(lambda d: len(d)) > 0]

# display
print(type(data))

data.to_csv('csv_files/prob_rec_cleaned_fromprajwalsCode.csv',
            mode='a', index=False)
