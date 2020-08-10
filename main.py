import discogs_client
import json

def main(request):
    """
    TODO:
    - store consumer_key and consumer_secret in secret thingy.
    - find somme funky user_agent name and store it globaly.

    """
    consumer_key = 'DpToaTUkOnKnZaimGtWa'
    consumer_secret = 'cITslCuphJWwiqSQnIgQvKwHXQILTTuq'
    user_agent = 'collection-sorter/1.0'

    discogsclient = discogs_client.Client(user_agent)
    discogsclient.set_consumer_key(consumer_key, consumer_secret)
    token, secret, url = discogsclient.get_authorize_url()

    return json.dumps({'token': token, 'secret': secret, 'url': url}), 200, {'ContentType': 'application/json'}
    #return 'http://localhost:8080?token={}&secret={}&oauth_code= {}'.format(token, secret, url)