# MODE = main/node
MODE = 'main'

# General
WEBHOOK_PORT = 8080
MAIN_IP = '127.0.0.1'
# WEBHOOK_URL = 'http://'+MAIN_IP+':'+WEBHOOK_PORT

# main
SITE_PORT = 8888
SERVER_LIST = {
    "2": 'http://127.0.0.1:8080/hook',
    "3": 'http://192.168.1.1:8080/hook',
}

# node
SERVER_ID = 2

