#import requests
import pip._vendor.requests as requests
from twillio_connection import client, send_whatsapp_text
from config import account_sid, auth_token

#link = "https://stoic.tekloon.net/stoic-quote"

def get_quote_of_the_day():
    link ="https://quotes-api-self.vercel.app/quote"
    res = requests.get(url=link)
    data = res.json()
    quote = data['quote']
    return quote


quote = get_quote_of_the_day()

#send_whatsapp_text(client, quote)