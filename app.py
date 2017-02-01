import flask
import os
import random

app = flask.Flask(__name__)

@app.route('/') #python decorator

def index():
    return flask.render_template("index.html")



@app.route('/random')

def randomNum():

       return flask.render_template("index.html",random = str(random.randint(1,100)))
    
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP','0.0.0.0')

)
    
    