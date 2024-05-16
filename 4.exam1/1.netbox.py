import requests, json

url = 'https://nb.ithethong.com/api/virtualization/virtual-machines/'
headers = {
    "Authorization": "Token a321ee0dab07674dbbd58e439a961c19c9b59e11",
    "Accept": "application/json; indent=4"
}

r = requests.get(url, headers=headers, verify=False)
pastebin_url = r.text 
test = json.loads(pastebin_url)

results=test["results"]
print("Type of JSON Object: ", type(results))


for id in results:
    print("id: ", id['id'])
    # print("Name1: ", test[name])