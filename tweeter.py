import properties
from status_cache_service import get_status
import tweepy


def tweet(status_text):
    auth = tweepy.OAuthHandler(properties.consumer_key, properties.consumer_secret)

    auth.set_access_token(properties.key, properties.secret)

    api = tweepy.API(auth)

    api.update_status(status_text)


def main():
    status_text = get_status()
    tweet(status_text)
    print('Tweeted: ', status_text)

if __name__ == '__main__':
    main()
