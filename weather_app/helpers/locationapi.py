import http.client

conn = http.client.HTTPSConnection("ip-geo-location.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "846d1b8362msh14f9854c64c91eep14d1bdjsnfccba4e7b3e8",
    'X-RapidAPI-Host': "ip-geo-location.p.rapidapi.com"
    }

conn.request("GET", "/ip/check?format=json", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))