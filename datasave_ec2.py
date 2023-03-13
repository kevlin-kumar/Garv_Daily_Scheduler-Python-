import datetime,time
from database_config_ec2  import *
import random
import pandas as pd

def savetodb(query,result):
    cursor = connection.cursor()
    cursor.execute(query,result)
    connection.commit()
    cursor.close()
    return


def ec2data(date):
    input_data = datetime.datetime(date.year,date.month,date.day)
    _hour_ = 0
    _minute_= 0
    for i in range(0,TOTAL_POINTS):
        _hour_ =  int(i/60)
        _minute_ = int(i  % 60 )
        time_code = datetime.datetime(input_data.year,input_data.month,input_data.day, _hour_ ,_minute_,input_data.second)
        value = random.randint(0, 100)
        try:
            res = (time_code,DESCRIPTION,value)
            savetodb(Insert_query,res)
        except:
            print("Failed To Save")

def final_func():
    a = pd.date_range(start='1/1/2023', end='2/1/2023')
    for i in a:
        x = i.date()
        ec2data(x)
     

     
final_func()
