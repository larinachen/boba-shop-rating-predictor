# this file explores the data in bayarea_boba_spots.csv and practices manipulating dataframes with pandas

# import dependencies
import csv
import pandas as pd
import numpy as np

# open csv file
file = open('bayarea_boba_spots.csv')
# print(type(file)) # prints the type of file, which is a file object

'''
# read the csv file using a csv reader object
csvreader = csv.reader(file)
# print(type(csvreader)) # csvreader is a csv.reader object


# extrating rows
# .
# extracting field names 
# next() prints the next row of the data frame
header = next(csvreader) # header of the csv ie. the first row of the whole file
# print(header) 
# extracting rows
row0 = next(csvreader)
row1 = next(csvreader)
print(row1) # prints row 1, the third row of the whole file
# saves the first 10 rows of the csv

firstrows = []
for i in range(10):
    row = next(csvreader)
    firstrows.append(row)
print(firstrows)
'''

shops = pd.read_csv("bayarea_boba_spots.csv")

def get_yelp_id():
    ids = shops["id"]
    ids = ids.to_numpy()
    return ids

def get_yelp_id_300():
    ids = get_yelp_id()
    ids = ids.head(301)
    ids = ids.to_numpy()
    return ids

# print(get_yelp_id_300()[0])