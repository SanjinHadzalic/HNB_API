import requests
import gui

a = gui.Window()

datum = a.local
valuta = a.currency_local

url = "https://api.hnb.hr/tecajn/v2"
url2 = f"https://api.hnb.hr/tecajn/v2?datum-primjene={datum}"

response = requests.get(url2)
response.raise_for_status()


data = response.json()

kup_tecaj = ""
sred_tecaj = ""
prod_tecaj = ""

for num in range(len(data)):
    if data[num]['valuta'] == valuta:
        kup_tecaj = data[num]['kupovni_tecaj']
        sred_tecaj = data[num]['srednji_tecaj']
        prod_tecaj = data[num]['prodajni_tecaj']


a.kup_tecaj = kup_tecaj
a.sred_tecaj = sred_tecaj
a.prod_tecaj = prod_tecaj


print(f" Kupovni tecaj: {a.kup_tecaj},\n Srednji tecaj: {a.sred_tecaj},\n Prodajni tecaj: {a.prod_tecaj}\n")
