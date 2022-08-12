# import socket
# import json

# def Client(data):
#     HOST, PORT = "localhost", 8080

#     # Create a socket (SOCK_STREAM means a TCP socket)
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     try:
#         # Connect to server and send data
#         sock.connect((HOST, PORT))
#         sock.send(bytes(json.dumps(data), 'UTF-8'))

#         # Receive data from the server and shut down
#         received = json.loads(sock.recv(1024).decode('UTF-8'))
#     finally:
#         sock.close()

#     print("Sent: {}".format(data))
#     print("Received: {}".format(received))

import requests
import json
import config

def sent_webhook (webhook_url,webhook_data):
    req = requests.post(webhook_url, data=json.dumps(webhook_data), headers={'Content-Type': 'application/json'})
    return req
