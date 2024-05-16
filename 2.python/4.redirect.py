# import flast module
from flask import Flask, redirect

# instance of flask application
app = Flask(__name__)

# home route that redirects to 
# helloworld page
@app.route("/")
def home():
	return redirect("/helloworld")

# route that returns hello world text
@app.route("/helloworld")
def hello_world():
	return "<p>Hello, Đây là trang HelloWorld.!</p>"


if __name__ == '__main__':
	app.run(host='10.0.11.91', debug=True) 
