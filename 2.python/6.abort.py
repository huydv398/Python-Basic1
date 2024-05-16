# importing abort 
from flask import Flask, abort 

# Initialize the flask application 
app = Flask(__name__) 


@app.route('/<uname>') 
def index(uname): 
	if uname[0].isdigit(): 
		abort(403) 
	return '<h1>Good Username</h1>'


if __name__ == '__main__': 
	app.run(host='10.0.11.91', debug=True)
