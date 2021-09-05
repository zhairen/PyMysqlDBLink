# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 18:01:18 2021

@author: liujinxin
"""

import pymysql
from sqlalchemy import create_engine
import pandas as pd

#engine = create_engine('mysql+mysqlconnector://[user]:[password]@[host]:[port]/[schema]', echo=False)
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/TestFinanceDB', echo=False)

sql_location = "SELECT UserName,Province FROM UserLocation "

data = pd.read_sql(sql_location, engine)

print(data['UserName'])

#-----ml 
#------

model_data =data 
#odel_data.to_sql(name='test_table', con=engine, if_exists = 'append', index=False)