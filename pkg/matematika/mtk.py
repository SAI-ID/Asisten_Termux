def Tambah(x,y):
    return x + y

def Kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    return x / y

def modulus(x,y):
    return x % y

def pangkat(x,y):
    return x ** y

from urllib import request
import json

def ss():
    from urllib import request
    import json
    url = 'https://api.github.com/users/Akhiro-Siro'

    respon = request.urlopen(url)
    data = json.loads(respon.read())

    print(f"nama : {data['name']}")
    print(f"lokasi : {data['location']}")
    print(f"bio : {data['bio']}")
    print(f"project : {data['blog']}")