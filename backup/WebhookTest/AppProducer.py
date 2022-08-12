# Flask imports
from flask import Response, render_template
from InitProducer import app
import TasksProducer


def stream_template(template_name, **context):
    app.update_template_context(context)
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.enable_buffering(5)
    return rv


@app.route("/", methods=['GET'])
def index():
    return render_template('producer.html')


@app.route('/producetasks', methods=['POST'])
def producetasks():
    print("producetasks")
    return Response(stream_template('producer.html', data=TasksProducer.produce_bunch_tasks()))


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
