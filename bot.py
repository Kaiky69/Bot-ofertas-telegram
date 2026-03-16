import requests
import random

TOKEN = "8540004525:AAGQTirxzKJLYssGqZl9kqxTAs23XY9mh18"
CHAT_ID = "-1003551593842"

buscas = [
"fone bluetooth",
"smartwatch",
"ssd",
"placa de video",
"notebook"
]

produto = random.choice(buscas)

url = f"https://api.mercadolibre.com/sites/MLB/search?q={produto}"

dados = requests.get(url).json()

item = random.choice(dados["results"])

titulo = item["title"]
preco = item["price"]
link = item["permalink"]

mensagem = f"""
🔥 OFERTA ENCONTRADA

📦 {titulo}
💰 R${preco}

🛒 Comprar:
{link}
"""

requests.post(
f"https://api.telegram.org/bot{TOKEN}/sendMessage",
data={"chat_id": CHAT_ID, "text": mensagem}
)
