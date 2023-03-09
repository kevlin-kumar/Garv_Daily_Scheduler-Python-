import requests
import json
from database_config import *
import datetime

def savetodb(query,result):
    cursor = connection.cursor()
    cursor.execute(query,result)
    connection.commit()
    cursor.close()
    return

def datacollect(api):
    response = requests.get(api)
    #print(type(response))
    result = response.json()
    return result


def kiosk_ids():
    list_of_kiosk_ids = []
    data = datacollect(api_url_kiosk_ids)
    
    for i in data:
        list_of_kiosk_ids.append(i["kiosk_id"])
    return list_of_kiosk_ids  


def kiosk_data_daywise(day,month,year):
    id_list = kiosk_ids()
    print("The list is",id_list)
    for i in id_list:
        data = datacollect(api_url_day_wise.format(i,day,month,year))
        kiosk_id = data[0][0]['kiosk_id']
        kiosk_name = data[0][0]['kiosk_name']
        kiosk_ip = data[0][0]['kiosk_ip']
        time_stamp = datetime.date(year, month, day)

        module_details = data[1]
        print("Inside the 1st loop",module_details)

        for j in module_details:

            print("Inside the 2nd loop")
            module_id = j['module_id']
            module_name = j['module']['module_name']
            count = j['count']
            res = (time_stamp,kiosk_id,kiosk_name,kiosk_ip,module_id,module_name,count)
            print(res)
            try:
                savetodb(Insert_query,res)
                print("Saving Sucessfully to DB")
            except:
                print("Insertion Failed")
        
    return









# def alerts():
#     data = datacollect(api_url_all_alert.format(TIME))

#     for i in data:
#         alert_time = i["kismet.alert.timestamp"]
#         alert_time = datetime.datetime.fromtimestamp(int(alert_time)).strftime('%Y-%m-%d %H:%M:%S.%f')
#         alert_severity = i["kismet.alert.severity"]
#         alert_frequency = i["kismet.alert.frequency"]
#         alert_destmac = i["kismet.alert.dest_mac"]
#         alert_message = i["kismet.alert.text"]
#         alert_class = i["kismet.alert.class"]
#         alert_othermac = i["kismet.alert.other_mac"]
#         alert_channel = i["kismet.alert.channel"]
#         alert_phyid = i["kismet.alert.phy_id"]
#         alert_devicekey = i["kismet.alert.device_key"]
#         alert_transmittermac = i["kismet.alert.transmitter_mac"]
#         alert_header = i["kismet.alert.header"]
#         alert_sourcemac = i["kismet.alert.source_mac"]

#         try:
#             res = (alert_time,alert_severity,alert_frequency,alert_destmac,alert_message,alert_class,alert_othermac,alert_channel,alert_phyid,alert_devicekey,alert_transmittermac,alert_header,alert_sourcemac)
#         except:
#             print("Insertion to alert table failed")
#         savetodb(Alert_query,res)


# def ssid():
#     data = datacollect(api_url_ssids)

#     for i in data:
#         first_seen = i["dot11.ssidgroup.first_time"]
#         first_seen = datetime.datetime.fromtimestamp(int(first_seen)).strftime('%Y-%m-%d %H:%M:%S.%f')
#         last_seen = i["dot11.ssidgroup.last_time"]
#         last_seen = datetime.datetime.fromtimestamp(int(last_seen)).strftime('%Y-%m-%d %H:%M:%S.%f')
#         ssid_name = i["dot11.ssidgroup.ssid"]
#         advertising_devices = i["dot11.ssidgroup.advertising_devices_len"]
#         advertising_devices = str(advertising_devices)
#         responding_devices = i["dot11.ssidgroup.responding_devices_len"]
#         responding_devices = str(responding_devices)

#         try:
#             res = (first_seen,last_seen,ssid_name,advertising_devices,responding_devices)
#             savetodb(Ssid_query,res)
#         except:
#             print("Insertion to SSID table failed")
    


    












