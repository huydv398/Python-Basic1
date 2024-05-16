from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)
@app.route("/")
def index():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(host='10.0.11.91', debug=True, port=80)
