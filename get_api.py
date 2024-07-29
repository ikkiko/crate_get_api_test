import requests as rq

url = rq.get('https://jellyfish-app-vkuir.ondigitalocean.app/balance/0x2325d8475D4193e4b79CC9F66e54C0E73Dda8Ae8')
data = url.json()
print(data)

urlLock = rq.get('https://jellyfish-app-vkuir.ondigitalocean.app/lockBalance/0x2325d8475D4193e4b79CC9F66e54C0E73Dda8Ae8')
dataLock = urlLock.json()
print(dataLock)