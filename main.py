import requests
import gui

a = gui.Window()

datum = a.local

url = "https://api.hnb.hr/tecajn/v2"
url2 = f"https://api.hnb.hr/tecajn/v2?datum-primjene={datum}"

response = requests.get(url2)
response.raise_for_status()


data = response.json()

for num in range(len(data)):
    print(data[num])


