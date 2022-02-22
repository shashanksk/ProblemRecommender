import pandas as pd

# making data frame from csv file
data = pd.read_csv(
    "csv_files/prob_rec_csv_file_yo_3.csv", index_col="Tags_n")

print(data)

# dropping passed values

data.drop(["[]"], inplace=True)
# data[data['Tags'].map(lambda d: len(d)) > 0]

# display
print(type(data))

data.to_csv('csv_files/prob_rec_csv_file_yo_cleaned9.csv',
            mode='a', index=False)
