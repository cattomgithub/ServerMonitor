import os
import time
import math
import json
import psutil
import node_config
import requests


def get_os_detail():
    loadavg = os.getloadavg()

    cpu_usage = psutil.cpu_percent(1)

    mem_usage = psutil.virtual_memory().percent

    uptime_sec = math.floor(time.time() - psutil.boot_time())
    uptime_min = uptime_sec // 60
    uptime_hour = uptime_min // 60
    uptime_day = uptime_hour // 24

    uptime_sec %= 60
    uptime_min %= 60
    uptime_hour %= 60
    uptime_day %= 24

    result = {
        "Server_ID": node_config.SERVER_ID,
        "CPU_Usage": cpu_usage,
        "Mem_Usage": mem_usage,
        "Load_Avg": loadavg,
        "Uptime_Day": uptime_day,
        "Uptime_Hour": uptime_hour,
        "Uptime_Minute": uptime_min,
        "Uptime_Second": uptime_sec
    }

    return result


def sent_json(webhook_url, webhook_data):
    req = requests.post(webhook_url, data=json.dumps(
        webhook_data), headers={'Content-Type': 'application/json'})
    return req

while True:
    time.sleep(node_config.UPDATE_DELAY)

    webhook_url = 'https://'+node_config.MAIN_ADDRESS+'/hook'

    webhook_data = get_os_detail()

    print(webhook_data)

    sent_json(webhook_url, webhook_data)
