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
    edit_db.mem_usage = data['Mem_Usage']
    edit_db.load_avg = data['Load_Avg']
    edit_db.uptime_day = data['Uptime_Day']
    edit_db.uptime_hour = data['Uptime_Hour']
    edit_db.uptime_minute = data['Uptime_Minute']
    edit_db.uptime_second = data['Uptime_Second']
    edit_db.save()


# Set up hook
app = Flask(__name__)

@app.route('/hook', methods=['POST'])
def hook():
    if request.method == 'POST':
        data = request.json
        edit_database(data)
        return 'success', 200
    else:
        abort(400)

if __name__ == '__main__':
	app.run(host='0.0.0.0')

