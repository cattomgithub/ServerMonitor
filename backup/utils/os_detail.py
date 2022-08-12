import os
import time
import math
import psutil
import config
import utils.client

def get_os_detail ():
    loadavg = os.getloadavg()

    cpu_usage = psutil.cpu_percent(1)

    memory_usage = psutil.virtual_memory().percent

    uptime_sec = math.floor(time.time() - psutil.boot_time())
    uptime_min = uptime_sec // 60
    uptime_hour = uptime_min // 60
    uptime_day = uptime_hour // 24

    uptime_sec %= 60
    uptime_min %= 60
    uptime_hour %= 60
    uptime_day %= 24


    result = {
        "Server_ID": config.SERVER_ID,
        "CPU_Usage": cpu_usage,
        "Memory_Usage": memory_usage,
        "Load_Avg": loadavg,
        "Uptime": {
            "Day": uptime_day,
            "Hour": uptime_hour,
            "Minute": uptime_min,
            "Second": uptime_sec
        }
    }

    webhook_data = result

    webhook_url = config.SERVER_LIST['1']

    utils.client.sent_webhook(webhook_url,webhook_data)