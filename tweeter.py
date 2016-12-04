import properties
import status_creator
import tweepy


def tweet(status_text):
    auth = tweepy.OAuthHandler(properties.consumer_key, properties.consumer_secret)

    auth.set_access_token(properties.key, properties.secret)

    api = tweepy.API(auth)

    api.update_status(status_text)


def main():
    statusText = status_creator.create_sentence(3)
    status_length = len(statusText)
    if status_length <= 140:
        tweet(statusText)
        print('Tweeted: ', statusText)
    else:
        print('Status length({}) is too long to post.'.format(status_length))
        print('Status: ', statusText)


if __name__ == '__main__':
    main()
