import gmmpy
import datetime
import pandas as pd
import numpy as np

now = datetime.datetime.now()
dba=gmmpy.Database() 
date = ("%d-%.2d-%.2d %.2dh%.2d" % (now.year, now.month, now.day, now.hour, now.minute))
mygame = "asp8"
print('Today is ' + str(date))

mygame = 'kingdoms'


request = {
        "FIELDS": ["server_date","users()"],
        "TABLE": mygame,
        "GROUPBY": ["server_date"],
        "WHERE": ["final.qa = 0"],
        "ORDERBY": ["server_date DESC"],
            }
df = dba.query_dataframe(request)
print(df.head(n=10))



