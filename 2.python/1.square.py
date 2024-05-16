# import the Flask library
from flask import Flask, render_template, request


# Tạo phiên bản Flask và truyền cho hàm tạo Flask đường dẫn của mô-đun chính xác
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def squarenumber():
# Nếu phương thức là POST, lấy số do người dùng nhập
# Tính bình phương của số và chuyển nó vào answermaths 
	if request.method == 'POST':
		if(request.form['num'] == ''):
			return "<html><body> <h1>Invalid number</h1></body></html>"
		else:
			number = request.form['num']
			sq = int(number) * int(number)
			return render_template('answer.html', 
							squareofnum=sq, num=number)
	# Nếu phương thức là GET, hiển thị trang HTML cho người dùng
	if request.method == 'GET':
		return render_template("squarenum.html")


# Start with flask web app with debug as True only 
# if this is the starting page
if(__name__ == "__main__"):
	app.run(debug=True)
