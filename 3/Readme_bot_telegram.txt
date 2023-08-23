Créer un bot Telegram en Python nécessite plusieurs étapes, dont la création du bot sur Telegram, l'utilisation d'une API pour obtenir les données météorologiques et la mise en place d'un planificateur pour envoyer les mises à jour à une heure fixe. Voici un guide pour mettre en œuvre cette fonctionnalité :

Étape 1 : Créer le bot sur Telegram

    Ouvrez Telegram et recherchez le bot appelé "BotFather".
    Démarrez une conversation avec BotFather et suivez les instructions pour créer un nouveau bot et obtenir un token d'accès.

Étape 2 : Installer les bibliothèques nécessaires

    Il est important d'avoir Python Bot Telegram version 13.7 installé sur votre système.Si ce n'est pas le cas, vous pouvez exécuter la commande suivante : pip install python-telegram-bot==13.7
    Installez les bibliothèques supplémentaire nécessaires en exécutant la commande suivante dans votre terminal : pip install requests schedule
    Assurez-vous de remplacer le champ 'BOT_TOKEN' par le token que vous avez obtenu auprès de BotFather.

Étape 4 : Exécution

    Exécutez le fichier en exécutant la commande suivante dans votre terminal :
    python Bot_Telegram_meteo.py ou python3 Bot_Telegram_meteo.py
    Une fois lancé : 
	 - le script tourne jusqu'à ce qu'on l'arrête avec un "Ctrl+C"
	 - Il faut s'abonner en tapant "/subscribe" dans le bot Telegram pour recevoir les données 
	 - Ce script enverra les température et  précipitation de Brickaville à 18h00, heure de Madagascar
	 - Pour se désabonner, on peut taper "/unsubscribe"
	
    