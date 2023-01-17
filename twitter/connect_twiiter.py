import tweepy


api_key = "V9kNI1mtRkqnC51Bw4BdVeR7V"
api_secret = "MMFF3DSNws4wZetXfPdVgtNEc1Q1ifx2QMEM7vpZD0M8Cpv65i"
bearer_token = r'AAAAAAAAAAAAAAAAAAAAAGHklAEAAAAAq%2Bo9wEq842V3dfhvKn22VDcKVJY%3DFldUeaSvl4MaSxgT0YpKOw6Qj4dApVU4UEDMh89DAid1ImvqcN'
access_token = "1467621269155758080-xexDkvXetFLHlbuwTSkdaWxhBFVNQl"
access_token_secret = "83fHPFyuHbgmCCzaQWDNyrrCWct2iVr1DEDZqBF2vySTx"
client_id = "N1dfSFFiMUd2TTdyOXFxNWZRNlg6MTpjaQ"
client_secret = "G5Pl7FkOPcB4GLcJtdGW05rhY0t_ty3rWwIb8okWx3pjmhad8I"


client = tweepy.Client(bearer_token, api_key, api_secret,
                       access_token, access_token_secret)


auth = tweepy.OAuth1UserHandler(
    api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


'''
# escribit tweets
client.create_tweet(text="Hola Mundo")


# like a tweet
client.like("1615194873514049538")

# retweet a tweet
client.retweet("1615194873514049538")

'''


# responder a tweet
# client.create_tweet(in_reply_to_tweet_id="1615194873514049538",
#                     text='Respondo este tweet desde el vsc')


# muestra el TL, se necesita v2

# for tweet in api.home_timeline():
#     print(tweet.text)


# me muestra todos los tweets publicados del username que coloque


# person = client.get_user(username="DevJr_").data.id


# for tweet in client.get_users_tweets(person).data:
#     print(tweet.text)
