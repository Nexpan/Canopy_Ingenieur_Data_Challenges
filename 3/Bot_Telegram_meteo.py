
import requests
import time
import datetime
from telegram import ForceReply
from telegram.ext import Updater, CommandHandler, CallbackContext

# Remplacez le champ 'BOT_TOKEN' par le token d'accès de votre bot obtenu avec @BotFather
BOT_TOKEN = 'BOT_TOKEN'
WEATHER_API_KEY = '74bd4d857063fa83dec0222d1d15bc1e'  # Remplacez par une clé API météo obtenu auprès d'un fournisseur de services météo "openweathermap"
CITY_NAME = 'Brickaville,MG'

# Dictionnaire pour stocker les abonnés
subscribers = {}

# Fonction pour envoyer la météo au client
def send_weather(context: CallbackContext):
    for chat_id in subscribers:
        weather_data = get_weather_data()
        message = f"🌦️ Météo à {CITY_NAME} :\nTempérature : {weather_data['temp']}°C\nPrécipitations : {weather_data['precip']} mm"
        context.bot.send_message(chat_id=chat_id, text=message)

# Fonction pour obtenir les données météorologiques
def get_weather_data():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    precipitation = data.get('rain', {}).get('1h', 0) #Obtention des données de précipitation dans une interval de 1h à partir des données obtenu du data
    return {'temp': temperature, 'precip': precipitation}

# Commande /start
def start(update, context):
    user = update.effective_user
    update.message.reply_html(
        rf"Bienvenu {user.mention_html()}! Utilisez /subscribe pour vous abonner à la météo quotidienne.",
        reply_markup=ForceReply(selective=True),
    )

# Commande /s'abonné
def subscribe(update, context):
    chat_id = update.message.chat_id
    if chat_id not in subscribers:
        subscribers[chat_id] = True
        update.message.reply_text("Vous êtes desormais abonné à la météo quotidienne de Brickaville.")
    else:
        update.message.reply_text("Vous êtes déjà abonné.")

# Commande /se désabonné
def unsubscribe(update, context):
    chat_id = update.message.chat_id
    if chat_id in subscribers:
        del subscribers[chat_id]
        update.message.reply_text("Vous êtes desormais désabonné de la météo quotidienne.")
    else:
        update.message.reply_text("Vous n'étiez pas abonné.")

# Fonction pour planifier l'envoi quotidien de la météo à 18h00, heure Madagascar
def schedule_weather_job(updater):
    while True:
        now = datetime.datetime.now()
        if now.hour == 18 and now.minute == 0: # 
            send_weather(updater)
        time.sleep(60)  # Attendre une minute avant de vérifier à nouveau

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    subscribe_handler = CommandHandler('subscribe', subscribe)
    dispatcher.add_handler(subscribe_handler)

    unsubscribe_handler = CommandHandler('unsubscribe', unsubscribe)
    dispatcher.add_handler(unsubscribe_handler)

    # Démarrer le thread pour planifier l'envoi de la météo
    import threading
    threading.Thread(target=schedule_weather_job, args=(updater,), daemon=True).start()

    updater.start_polling()

    #Attendre un "Ctrl+C" venant de l'utilisateur pour fermer le programme
    updater.idle()

if __name__ == "__main__":
    main()
