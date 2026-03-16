import requests
import random

TOKEN = "8540004525:AAGQTirxzKJLYssGqZl9kqxTAs23XY9mh18"
CHAT_ID = "-1003551593842"

produtos = [
"🔥 Oferta do dia\nhttps://meli.la/exemplo1",
"🔥 Super desconto\nhttps://meli.la/exemplo2",
"🔥 Promoção imperdível\nhttps://meli.la/exemplo3"
]

mensagem = random.choice(produtos)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
 "chat_id": CHAT_ID,
 "text": mensagem
})
