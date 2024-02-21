from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    title="Django Project"
    return render_template('index.html',title=title)