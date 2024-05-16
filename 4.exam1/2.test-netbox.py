
# IP = '10.0.11.66'
# def getvm(IP):
#     print(IP)
    
# getvm(IP)
# from flask import Flask, render_template, request
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# response = request.get(api_url)
# response.json()

import pynetbox
nb = pynetbox.api(
    'http://10.0.11.66',
    token='d6f4e314a5b5fefd164995169f28ae32d987704f'
)
devices = nb.dcim.devices.all()
print(devices)



