import respuestas
from data_api import bearer_token, api_key, api_secret, access_token, access_token_secret, client_id, client_secret
import time
import tweepy
import sys
sys.path.append("..")


client = tweepy.Client(bearer_token, api_key, api_secret,
                       access_token, access_token_secret)


auth = tweepy.OAuth1UserHandler(
    api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Bot's unique ID
client_id = client.get_me().data.id


def connect_twitter():
    # This is so the bot only looks for the most recent tweets.
    start_id = 1
    initialisation_resp = client.get_users_mentions(client_id)
    if initialisation_resp.data != None:
        start_id = initialisation_resp.data[0].id

    # Looking for mentions tweets in an endless loop
    while True:
        response = client.get_users_mentions(client_id, since_id=start_id)

        # Reply Code
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

        # Delay (so the bot doesn't search for new tweets a bucn of time each second)
        time.sleep(5)
