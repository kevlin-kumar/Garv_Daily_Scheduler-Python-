import mysql.connector


TOTAL_POINTS = 1440
DESCRIPTION = "CPU_Utilization"
# Database connection method 
connection = mysql.connector.connect(host='127.0.0.1',
                                         database='rfms_api',
                                        user='root',
                                        password='Admin@123')



#All the important queries
Insert_query = "INSERT INTO garv_ec2 (timestamp, description, value) VALUES (%s, %s, %s)"

