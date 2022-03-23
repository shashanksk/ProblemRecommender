from ctypes.wintypes import PINT
import pandas as pd


colums = pd.read_csv("ppp.csv")


colums.drop_duplicate(["Problem name"])

print(colums)
