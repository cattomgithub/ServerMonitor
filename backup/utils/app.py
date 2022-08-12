from flask import Flask, render_template
import config

app = Flask(__name__)


@app.route('/')
def site():
    app_name = "Cat Tom's Server Monitor"
    result = {'Server_ID': 1, 'CPU_Usage': 1.9, 'Memory_Usage': 69.3, 'Load_Avg': [
        1.3, 1.35, 1.37], 'Uptime': {'Day': 0, 'Hour': 4, 'Minute': 34, 'Second': 29}}
    return render_template('index.html', app_name=app_name, Server_ID=result["Server_ID"])


app.run(port=config.PORT)
