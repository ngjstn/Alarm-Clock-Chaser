from imgurpython import ImgurClient
from helpers import get_input, get_config

def authenticate():
	# Get client ID and secret from auth.ini
	config = get_config()
	config.read('auth.ini')
	client_id = config.get('credentials', 'client_id')
	client_secret = config.get('credentials', 'client_secret')
    
	client = ImgurClient(client_id, client_secret, 'deb82f8f68d5e601c70a5f0aa836fae52c115218')

	return client
