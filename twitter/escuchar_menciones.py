import tweepy
from connect_twiiter import client


client_id = client.get_me().data.id
message = 'Hola, cual es tu duda?'

while True:
    response = client.get_users_mentions(client_id)

    if response.data != None:
        for tweet in response.data:
            try:
                print(tweet.text)
                client.create_tweet(
                    in_reply_to_tweet_id=tweet.id, text=message)
