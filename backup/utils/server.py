# import socketserver
# import sys
# from pprint import pprint
# import json


# def Server(PORT):

#     HOST = 'localhost'

#     class SingleTCPHandler(socketserver.BaseRequestHandler):
#         "One instance per connection. Override handle(self) to customize action."

#         def handle(self):
#             # self.request is the client connection
#             data = self.request.recv(1024)  # clip input at 1Kb
#             text = data.decode('utf-8')
#             result = json.loads(text)
#             pprint(result)
#             for key in result:
#                 pprint(result[key])
#             self.request.send(
#                 bytes(json.dumps({"status": "success!"}), 'UTF-8'))
#             self.request.close()
#             return result

#     class SimpleServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
#         # Ctrl-C will cleanly kill all spawned threads
#         daemon_threads = True
#         # much faster rebinding
#         allow_reuse_address = True

#         def __init__(self, server_address, RequestHandlerClass):
#             socketserver.TCPServer.__init__(
#                 self, server_address, RequestHandlerClass)


#     server = SimpleServer((HOST, PORT), SingleTCPHandler)
#     # terminate with Ctrl-C
#     try:
#         server.serve_forever()
#     except KeyboardInterrupt:
#         sys.exit(0)

from flask import Flask, request, abort, render_template
import config
import utils.client
import utils.os_detail

def build_site():
    app = Flask(__name__)

    @app.route('/')
    def penel():
        if request.method == 'GET':
            for webhook_url in config.SERVER_LIST.values():
                webhook_data = {"msg": 'GetOSDetail'}
                utils.client.sent_webhook(webhook_url,webhook_data)
        return render_template('index.html')

    app.run(port=config.SITE_PORT)


def receive_webhook():
    app = Flask(__name__)

    @app.route('/hook', methods=['POST'])
    def hook():
        if request.method == 'POST':
            data = request.json
            print(data)
            if config.MODE == 'main':
                build_site()
            elif config.MODE == 'node':
                if data['msg'] == 'GetOSDetail':
                    utils.os_detail.get_os_detail()
                else:
                    print('Wrong message!')
            return 'success', 200
        else:
            abort(400)

    app.run(port=config.WEBHOOK_PORT)



