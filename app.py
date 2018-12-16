from flask import render_template, Flask
from flask import request
from manager import ramdon_forest_solo

app = Flask(__name__)
wsgi_app = app.wsgi_app


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/homepage")
def homepage():
    return render_template('homepage.html')

@app.route('/prediction', methods = ['POST'])
def prediction():
    f = request.files['file']
    placement = ramdon_forest_solo(f)
    return render_template('output.html', placement = placement)

if __name__ == "__main__":
    app.run(debug = True, port = 8080)
