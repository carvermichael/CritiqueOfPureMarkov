import properties
import status_creator
import tweepy


def tweet(status_text):
    auth = tweepy.OAuthHandler(properties.consumer_key, properties.consumer_secret)

    auth.set_access_token(properties.key, properties.secret)

    api = tweepy.API(auth)

    api.update_status(status_text)


def main():
    status_text = status_creator.create_sentence(3)
    status_length = len(status_text)
    if 140 >= status_length > 20:
        tweet(status_text)
        print('Tweeted: ', status_text)
    else:
        print('Status of length({}) will not be posted.'.format(status_length))
        print('Status: ', status_text)


if __name__ == '__main__':
    main()
