# Set up Django
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "public.settings")
django.setup()

# Import package
from flask import Flask, request, abort, render_template
from panel.models import Server
import config

# Edit Django database
def edit_database(data):
    server_id = data['Server_ID']
    edit_db = Server.objects.get(server_id=server_id)
    edit_db.cpu_usage = data['CPU_Usage']
    edit_db.save()


# Set up hook
app = Flask(__name__)

@app.route('/hook', methods=['POST'])
def hook():
    if request.method == 'POST':
        data = request.json
        edit_database(data)
        print(data)
        return 'success', 200
    else:
        abort(400)

app.run(port=config.WEBHOOK_PORT)

