# Homework 2 Yutong Liu

# 1 . (1 points) Write a python reads creates a dataframe from a URL
# that points to a CSV file such as the pronto data or CSVs in data.gov.

import pandas as pd

url= https://catalog.data.gov/dataset/passenger-injuries-and-injury-rates-1995-through-2014-for-u-s-air-carriers-operating-under/resource/c9951c96-b55f-4f1b-bdfd-90fe8a5dd738
df = pd.read_csv(url)
