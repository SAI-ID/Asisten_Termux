import requests
import json

def tampil_ip():
    ipaddress = input('isi ip>..\t: ')
    ipreq = requests.get(f"http://ip-api.com/json/{ipaddress}")

    if ipreq.status_code == 200:
        ipdata = json.loads(ipreq.text)
        if ipdata["status"] == "success":
            print("Negara :", ipdata["country"], ipdata["countryCode"])
            print("Wilayah :", ipdata["region"], ipdata["regionName"])
            print("kota :", ipdata["city"])
            print("kode pos :", ipdata["zip"])
            lat = ipdata["lat"]
            lon = ipdata["lon"]
            print("lokasi :", "lat :", lat, 'lon :', lon)
            print("lat and lon :", lat, ',', lon)
            maps = f"https://www.google.com/maps/@{lat},{lon},9z?h1=id"

            print("peta :", maps)
            print("jona waktu :", ipdata["timezone"])
            print("internet servis propaider :", ipdata["isp"], ipdata["as"])
            print("ip address :", ipdata["query"])
