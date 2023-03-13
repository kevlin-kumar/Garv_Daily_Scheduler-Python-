
#from datasave import *

import pandas as pd
from datasave import *
import time
from datetime import datetime

# specify the start date is 2021 jan 1 st
# specify the end date is 2021 feb 1 st
a = pd.date_range(start='2/7/2023', end='3/3/2023')

# display only date using date() function
for i in a:
	x = i.date()
	kiosk_data_daywise(x.day,x.month,x.year)
	
	


