import flask

app = flask.Flask(__name__)

@app.route('/') #python decorator

def index():
    return "Hello World"

app.run()
    