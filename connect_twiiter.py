import respuestas
from data_api import bearer_token, api_key, api_secret, access_token, access_token_secret, client_id, client_secret
import time
import tweepy

client = tweepy.Client(bearer_token, api_key, api_secret,
                       access_token, access_token_secret)


auth = tweepy.OAuth1UserHandler(
    api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Obtengo el id del usuario
client_id = client.get_me().data.id


# Con esto muestra la mas reciente mencion.
start_id = 1
initialisation_resp = client.get_users_mentions(client_id)
if initialisation_resp.data != None:
    start_id = initialisation_resp.data[0].id

# Mira menciones en un loop infinito
while True:
    response = client.get_users_mentions(client_id, since_id=start_id)

    # Codigo de respuesta al usuario
    if response.data != None:
        for tweet in response.data:
            try:
                capture = tweet.text
                print('im capture ==> ', capture)
                message = respuestas.generar_respuesta(capture)
                print('im message ==> ', message)
                client.create_tweet(
                    in_reply_to_tweet_id=tweet.id, text=message)
                start_id = tweet.id
            except Exception as error:
                print(error)

    # Delay para que el bot no este buscando menciones todo el tiempo
    time.sleep(5)
