# importing redirect 
from flask import Flask, redirect, url_for, render_template, request 

# Initialize the flask application 
app = Flask(__name__) 

# Nó sẽ tải form template: login.html 
@app.route('/') 
def index(): 
	return render_template("login.html") 


@app.route('/success') 
def success(): 
	return "logged in successfully"

# loggnig vào biểu mẫu với method POST or GET 
@app.route("/login", methods=["POST", "GET"]) 
def login(): 
	
	# nếu phương thức là POST và Username là admin  thì 
	# nó sẽ chuyển hướng đến url success. 
	if request.method == "POST" and request.form["username"] == "admin": 
		return redirect(url_for("success")) 

	# nếu phương thức là GET và Username không phải là admin thì, 
	# nó sẽ chuyển hướng đến index method. 
	return redirect(url_for('index')) 


if __name__ == '__main__': 
	app.run(host='10.0.11.91', debug=True)
