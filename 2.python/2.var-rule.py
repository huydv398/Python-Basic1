# First we import flask
from flask import Flask

# initialize flask
app = Flask(__name__)

# Display first simple welcome msg
@app.route('/')
def msg():
	return "Welcome To Huydv python"

# We defined string function
@app.route('/vstring/<name>')
def string(name):
	return "My Name is %s" % name

# define int function
@app.route('/vint/<int:age>')
def vint(age):
    return "Hiện tại tôi %d tuổi " % age

# define float function
@app.route('/vfloat/<float:value1>')
def vfloat(value1):
    return "Số dư tài khoản %f" % value1

# we run app debugging mode
if __name__ == '__main__': 
    app.run(host='10.0.11.91', debug=True) 
