from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

#Khai báo URL và Token Netbox
# API = 'https://nb.ithethong.com/api'
# url_vm = API + '/virtualization/virtual-machines/'
# url_cluster = 'https://nb.ithethong.com/api/virtualization/clusters'
url_vm = 'https://nb.suncloud.vn/api/virtualization'
headers = {
	"Authorization": "Token 38eff39a64b2d6de3f68c727fbd6635ebcf784b7",
	"Accept": "application/json",
    "Content-Type": "application/json"
}

    # "Content-Type": "application/json"

#thực hiện list ra toàn bộ VM
@app.route("/getvm")
def getvm():
	r = requests.get('https://nb.suncloud.vn/api/virtualization/virtual-machines/', headers=headers, verify=False)
	pastebin_url = r.text
	test = json.loads(pastebin_url)
	results=test["results"]
	# # print("Type of JSON Object: ", type(results))
	return render_template("getvm.html", results=results)
	# return test

@app.route("/createvm", methods=['GET', 'POST'])
def createvm():
    r_cluster = requests.get(url_vm + '/clusters', headers=headers, verify=False)
    cv_json = r_cluster.text
    test = json.loads(cv_json)
    results_cluster=test["results"]
    if request.method == 'GET':
        return render_template("createvm.html", results_cluster=results_cluster)
    #Nếu trình duyệt sử dụng method POST thì sẽ thực hiện trong biến sau:
    if request.method == 'POST':
        #thiết lập chuẩn dữ liệu của Netbox
        data = {
        "name": request.form['name'],
        "status": request.form['Status'],
        "cluster": request.form['cluster'],
        "description": request.form['description'],
        }
        #Chuyển đổi dữ liệu sang JSON
        data_json = json.dumps(data)
        response = requests.post('https://nb.suncloud.vn/api/virtualization/virtual-machines/', data=data_json, headers=headers, verify=False )
        return response.text

@app.route("/del")
def delvm():
    return render_template("delvm.html") 

# @app.route('/', methods=['GET', 'POST'])
# def squarenumber():
# # Nếu phương thức là POST, lấy số do người dùng nhập
# # Tính bình phương của số và chuyển nó vào answermaths 
# 	if request.method == 'POST':
# 		if(request.form['num'] == ''):
# 			return "<html><body> <h1>Invalid number</h1></body></html>"
# 		else:
# 			number = request.form['num']
# 			sq = int(number) * int(number)
# 			return render_template('answer.html', 
# 							squareofnum=sq, num=number)
# 	# Nếu phương thức là GET, hiển thị trang HTML cho người dùng
# 	if request.method == 'GET':
# 		return render_template("squarenum.html")



# @app.route("/about")
# def about():
# 	sites = ['twitter', 'facebook', 'instagram', 'whatsapp']
# 	return render_template("about.html", sites=sites)

# @app.route("/contact/<role>")
# def contact(role):
# 	return render_template("contact.html", person=role)


if __name__ == "__main__":
	app.run(host='10.0.11.91', debug=True, port=80)

