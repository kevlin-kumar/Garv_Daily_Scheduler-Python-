import mysql.connector


#Time for refreshing data
TIME = -60 #in seconds 

# Database connection method 
connection = mysql.connector.connect(host='127.0.0.1',
                                         database='rfms_api',
                                        user='root',
                                        password='Admin@123')

# All the possible APIs

api_url_kiosk_ids = "https://appseksdemo.stlgarv.com/user/kiosk_get_count"
api_url_day_wise = "https://appseksdemo.stlgarv.com/user/kiosk_get_count_by_day/{}/{}/{}/{}"

#All the important queries
Insert_query = "INSERT INTO garv_daliy_count (timestamp, kiosk_id, kiosk_name, kiosk_ip, module_id, module_name, count) VALUES (%s, %s, %s,%s, %s, %s, %s)"

