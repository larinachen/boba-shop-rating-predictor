# obtains the review count of each business in csv

import requests
import json
import pickle
from data_exploration import *



'''
# set up

# authentication
key = 'a01AzenUWU_GR7zp2ZwQdOGuBvtke62yaSbt90hoeLLIvEQnlSb3Fdql31peSo23bA8CFAT1YeWSJERk2Z4bjtlUBaxBIcXZnke-kq1bARXxoGir1XV1Hy2W9x8AYnYx'
auth = {'Authorization':'bearer %s' %key}
# get yelp ids of the first 300 boba shops
ids = get_yelp_id() # type: numpy array
# test_id = get_yelp_id_300()[0]
# test_id2 = get_yelp_id_300()[1]
# arr = [test_id,test_id2]
# base url for request
base_url = 'https://api.yelp.com/v3/businesses/'

# request
all_review_counts = {}
for i in range(len(ids)):
    r = requests.get(url = base_url + ids[i], headers = auth)
    print(i)
    # collect all data about the shop
    shop = r.json()
    # collect review counts
    shop_review_count = shop['review_count']
    all_review_counts[i] = shop_review_count
# storing review count
dbfile = open('pickle_review_count', 'wb')
pickle.dump(all_review_counts, dbfile)                     
dbfile.close()
print(all_review_counts)
'''

# reading review count dictionary
dbfile = open('pickle_review_count', 'rb')     
db = pickle.load(dbfile)
for keys in db:
    print(keys, '=>', db[keys])
dbfile.close()
