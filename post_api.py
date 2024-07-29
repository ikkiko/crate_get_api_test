import requests as rq
import time

url = 'https://jellyfish-app-vkuir.ondigitalocean.app/betBalance'
payload = {"wallet": "0x2325d8475D4193e4b79CC9F66e54C0E73Dda8Ae8", "betAmount": "200"}

databet = rq.post(url, json=payload)
id = databet.json()
print(id["id"])

time.sleep(5)

urlid = rq.get('https://jellyfish-app-vkuir.ondigitalocean.app/txhash/' + id["id"])
txhash = urlid.json()
print(txhash["tx_hash"])


urlhash = rq.get('https://jellyfish-app-vkuir.ondigitalocean.app/transaction/' + txhash["tx_hash"])

print(urlhash.text)
